# -*- coding: utf-8 -*-

import traceback
import jinja2

from flask import Flask
from flask import request

from model import KvData

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/save',methods=['get'])
def saveForm():
    try:
        jjenv = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'),extensions=["jinja2.ext.do",'jinja2.ext.i18n'])
        html = jjenv.get_template('save.html').render(title=u'测试', name='aa')
        return html
    except:
        traceback.print_exc()

@app.route('/save',methods=['post'])
def saveData():
    try:
        k = request.form['k']
        v = request.form['v']

        kv = KvData(key_id=k, value=v)
        res = kv.put()
        print '=' *10 + res.__str__()
        return 'save' + k + v
    except:
        traceback.print_exc()

if __name__ == '__main__':
    app.run()
