import eventlet
eventlet.monkey_patch()
import tasks

from urllib2 import urlopen

def fetch(url):
    f = open('/home/ramakishore', 'w')
    body = urlopen(url).read()
    f.write(body)
    f.close()

tasks.set_func(fetch)
tasks.main()
