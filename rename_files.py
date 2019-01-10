#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
if_cur_dir = input("input 1 for current dir or input the dir with like 'c:\\\\user\\\\...'")
tar_extension = input("input the target file's extension like '.txt'")
if if_cur_dir == '1':
    path = os.getcwd()
else:
    path = if_cur_dir
try:
    filenames = os.listdir(path)
except FileNotFoundError as e:
    print(e.massege)
cnt = 0
for item in filenames:
    extension = os.path.splitext(item)[1]
    if extension == tar_extension:
        cnt = cnt + 1
        new_name = '[' + str(cnt) + '] ' + item
        os.renames(path + '\\' + item, path + '\\' + new_name)
print('%d filenames modified' % cnt)


