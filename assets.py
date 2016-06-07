from flask import render_template
from settings import settings

def get_page(pageName):
    for i in settings['pages']:
        if(pageName == i['uri']):
            return render_template(settings['paths']['pages']+i['path']+'.jinja2')

    return '404 not found'

def get_info():
    raise NotImplemented

if __name__ == '__main__':
    import psycopg2
    conn = psycopg2.connect("dbname='opeteth' user='postgres' host='localhost' password='N0PLZeFLEv'")
    cur= conn.cursor()
    cur.execute('SELECT * FROM "user"')
    rows=cur.fetchall()
    for row in rows:
        print(row)

def generate_menu_links():
    data=[]
    temp={}
    for i in settings['menu']:
        temp={}
        temp['name']=i['name']
        temp['url']='not found'
        for j in settings['pages']:
            if j['id']== i['link-to']:
                temp['url']=j['path']

        data.append(temp)
    print(data)
    return data
