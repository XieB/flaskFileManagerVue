# -*- coding:utf-8 -*-
import os
import shutil
from datetime import datetime


def get_dir_list(request_path):
    file_list = {'dirs' : [],'files' : []}
    for item in os.listdir(request_path):
        full_path = os.path.join(request_path, item)
        fsize = os.path.getsize(full_path)
        # fmtime = time.strftime("%Y-%m-%d %H:%M:%S",os.path.getctime(full_path))
        fmtime = datetime.fromtimestamp(os.path.getctime(full_path)).strftime( '%Y-%m-%d %H:%M:%S')
        isWrite = os.access(full_path,os.W_OK)
        if os.path.isdir(full_path):
            file_list['dirs'].append({'name': item, 'fsize': str(fsize) + 'KB', 'fmtime': fmtime,'write':isWrite})
        else:
            file_list['files'].append({'name': item, 'fsize': fsize, 'fmtime': fmtime,'write':isWrite})
    return file_list

def unlink_f(fullName):
    if (os.path.isdir(fullName)):
        try:
            shutil.rmtree(fullName)
        except:
            shutil.rmtree(fullName)  # 调用一次只会清空目录？没有完全删除？
    else:
        os.remove(fullName)
    return not os.path.exists(fullName)