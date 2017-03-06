# coding=gbk
import time
import requests


class WatchDog(object):
    def __init__(self, filename):
        self.file = open(filename, 'r')
        l = self.file.readline()
        while l:
            l = self.file.readline()

    def watch(self):
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


w = WatchDog('/home/admin/logs/certdoccenter/certdoccenter-biz.log')
w.watch()