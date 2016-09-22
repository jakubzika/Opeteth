import threading
from time import sleep

#should spawn new thred which fires after done period

def job(time,function):
    while True:
        sleep(time)
        function()

def spawnThread(time,function):
    thread = threading.Thread(target=job,args=(time,function))
    thread.daemon = True
    thread.start()