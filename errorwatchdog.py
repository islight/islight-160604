# coding=gbk
import os
import time
import requests

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class WatchDog(FileSystemEventHandler):
    def __init__(self, filename):
        self.filename = filename;
        self.file = open(filename, 'r')
        l = self.file.readline()
        while l:
            l = self.file.readline()

    def on_created(self, event):
        super(WatchDog, self).on_created(event)

        if self.filename == event.src_path:
            self.file = open(self.filename, 'r')
            print 'reload '+ self.filename

    def watch(self):
        observer = Observer()
        observer.schedule(self, os.path.dirname(self.filename), recursive=False)
        observer.start()

        while True:
            l = self.file.readline()
            if not l:
                time.sleep(1)
                continue
            if l.find('ERROR') != -1:
                self.notify(l)

    def notify(self, msg):
        print msg
        res = requests.post(
            'https://oapi.dingtalk.com/robot/send?access_token=cffd481966d399a8f3df743295ee4d5c9842e95021447e272565b21211a8c696',
            json={"msgtype": "text", "text": {"content": msg.decode('gb2312')}})
        print res.text

wd = WatchDog('/tmp/a.log')
wd.watch()
