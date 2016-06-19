import psycopg2
import hashlib
import os
from base64 import b64encode
import time
import datetime

error = 300


class User:
    def __init__(self):
        self.conn = psycopg2.connect("dbname='opeteth' user='postgres' host='localhost' password='N0PLZeFLEv'")

    def exists(self, email):
        if (self.get_id(email)):
            return True
        else:
            return False

    def authenticate(self, email, password, ip):
        if (self.exists(email)):
            id = self.get_id(email)
            info = self.get_info(id)
            if (info['password'] == self.hash_password(password)):
                session = self.new_session(id, ip)
                return error + 10, session
            else:
                return error + 2, ''
        else:
            return error + 1, ''

    def logout(self, session):
        cur = self.get_cursor()
        id= self.get_session_id(session)
        data = self.get_session_info(id)

        sql = '''UPDATE "sessions" SET valid = {valid} WHERE id = {id} '''.format(valid='FALSE',id=id)
        cur.execute(sql)
        print(sql)
        self.conn.commit()

    def get_id(self, email):
        cur = self.get_cursor()
        sql = '''SELECT * FROM "user" WHERE email = '{email}' '''.format(email=email)
        cur.execute(sql)
        data = cur.fetchall()
        if (len(data) == 0):
            return None
        return data[0][0]

    def get_info(self, id):
        cur = self.get_cursor()
        sql = '''SELECT * FROM "user" WHERE id = '{id}' '''.format(id=id)
        cur.execute(sql)
        data = cur.fetchall()
        if (len(data) == 0):
            return None
        return {
            'id': data[0][0],
            'name': data[0][1].rstrip(),
            'email': data[0][2].rstrip(),
            'password': data[0][3],
            'permission': data[0][4],
        }

    def create_user(self, name, email, password, permissions):
        cur = self.get_cursor()
        if (not self.exists(email)):
            sql = '''INSERT INTO "user" (name,email,password,permissions) VALUES ('{name}','{email}','{password}',{permissions})''' \
                .format(name=name, email=email, password=self.hash_password(password), permissions=permissions)
            foo = cur.execute(sql)
            self.conn.commit()

    def get_cursor(self):
        return self.conn.cursor()

    def new_session(self, id, ip):
        session = self.generate_session_key()
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        sql = '''INSERT INTO "sessions" (user_id,session,ip,expiration,login_time) VALUES ({id},'{session}','{ip}','{expiration}','{time}')'''.format(
            id=id, session=session, ip=ip, expiration=int(time.time()) + 3600, time=st)

        cur = self.get_cursor()
        cur.execute(sql)
        self.conn.commit()
        return session

    def generate_session_key(self):
        cur = self.get_cursor()
        session = ''
        isUnique = False
        while not isUnique:
            bytes = os.urandom(48)
            session = b64encode(bytes).decode('utf-8')
            if (self.get_session_id(session) == None):
                isUnique = True
        return session

    def get_session_id(self, session):
        cur = self.get_cursor()
        sql = '''SELECT id FROM "sessions" WHERE session = '{session}' '''.format(session=session)
        cur.execute(sql)
        data = cur.fetchall()
        if (data == []):
            return None
        return data[0][0]

    def get_session_info(self, id):
        cur = self.get_cursor()
        sql = '''SELECT * FROM "sessions" WHERE id = '{id}' '''.format(id=id)
        cur.execute(sql)
        data = cur.fetchall()
        if (data == []):
            return None
        return {
            'id': data[0][0],
            'user_id': data[0][1],
            'session': data[0][2],
            'ip': data[0][3],
            'expiration': data[0][4],
            'valid': data[0][5]
        }

    def valid_session(self, session):
        id = self.get_session_id(session)
        if (id != None):
            info = self.get_session_info(id)
            if (info['expiration'] > int(time.time()) and info['valid']):
                self.extend_session(id)
                return error + 9
            return error + 8
        return error + 7

    def extend_session(self, id):
        cur = self.get_cursor()
        sql = '''UPDATE "sessions" SET expiration = {expiration} WHERE id = {id} '''.format(
            expiration=int(time.time()) + 3600, id=id)
        cur.execute(sql)
        self.conn.commit()

    def is_logged_in(self, session):
        if (session != None):
            if (self.valid_session(session) == error + 9):
                return True
            return False
        return False

    def info_by_session(self, session):
        id = self.get_session_id(session)
        sessionInfo = self.get_session_info(id)
        info = self.get_info(sessionInfo['user_id'])
        return info

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()


if __name__ == '__main__':
    user = User()
    # a=user.authenticate('kuba.zika@email.cz','abc123','94.142.236.100')
    a = user.is_logged_in('o0uTV4IEF3KgsWungJ+/vfsPLm6Btyya9SCKGDCEp4bMeuAEmtwW5nHJsM/3FLfd')
    print(a)
