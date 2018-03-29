# -*- coding:utf-8 -*-
from flask import Flask,request
from flask_cors import *
import json
import sys
app = Flask(__name__)
CORS(app)
import tools
reload(sys)
sys.setdefaultencoding('utf8')
basePath = 'D:/copy'

@app.route('/',methods=['GET', 'POST'])
def lists():
    realPath = basePath
    if (request.form['path']):
        realPath += request.form['path']
    return json.dumps(tools.get_dir_list(realPath))

@app.route('/delete',methods=['GET', 'POST'])
def delete_f():
    realPath = basePath
    res = 0
    if (request.form['path']):
        realPath += request.form['path']
    fileFullPath = realPath + '/' + request.form['file']
    # return json.dumps(fileFullPath)
    if (tools.unlink_f(fileFullPath)):
        res = 1
    return json.dumps(res)

@app.route('/edit',methods=['GET', 'POST'])
def edit():
    realPath = basePath
    if (request.form['path']):
        realPath += request.form['path']
    fileFullPath = realPath + '/' + request.form['file']
    with open(fileFullPath,'r') as f:
        return f.read()

@app.route('/save',methods=['GET', 'POST'])
def save():
    realPath = basePath
    res = 1
    if (request.form['path']):
        realPath += request.form['path']
    fileFullPath = realPath + '/' + request.form['file']
    with open(fileFullPath, 'w') as f:
        try:
            f.write(request.form['txt'])
        except Exception,e:
            print e
            res = 0
    return json.dumps(res)


if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True, threaded=True)