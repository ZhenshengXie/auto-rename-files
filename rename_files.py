#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os


mode_dict = {"replace": "1",
             "add_order": "2",
             "add_prefix": "3",
             "add_postfix": "4",
             "insert_str_before": "5",
             "insert_str_after": "6",
             "replace_ext": "7"}


def ui():
    if_cur_dir = input("input 1 for current dir or input the dir with like 'c:\\user\\...'\n")
    tar_extension = input("input the target file's extension like '.txt'\n")
    mode = input("please choose the mode of rename:\n"
                 "1. replace certain str into other.\n"
                 "2. add order number before filename.\n"
                 "3. add prefix to filename\n"
                 "4. add postfix filename\n"
                 "5. insert str before certain str\n"
                 "6. insert str after certain str\n"
                 "7. change the file's extension\n"
                 "mode = ")
    if mode not in mode_dict.values():
        print("mode chosen not match!\n")
        exit(-1)
    ui_data = [if_cur_dir, tar_extension, mode]
    return ui_data


def get_path(ui_data):
    if ui_data[0] == '1':
        path = os.getcwd()
    else:
        path = ui_data[0]
    return path


def get_tar_extension(ui_data):
    tar_extension = ui_data[1]
    return tar_extension


def get_mode(ui_data):
    mode = ui_data[2]
    return mode


def get_filenames(ui_data):
    path = get_path(ui_data)
    tar_ext = get_tar_extension(ui_data)
    try:
        dir_list = os.listdir(path)
    except FileNotFoundError:
        print("dir not found, check and try again.\n")
        exit(code=-1)
    filenames = []
    for item in dir_list:
        ext = os.path.splitext(item)[1]
        if ext == tar_ext:
            filenames.append(item)
    return filenames


def replace_handle(filenames, ui_data):
    path = get_path(ui_data)
    print("the tar path is: %s\n" % path)
    str_before = input("enter the str you want to replace from:")
    str_after = input("enter the str you want to replace to:")
    cnt = 0
    for old_name in filenames:
        if old_name.find(str_before) >= 0:
            new_name = old_name.replace(str_before, str_after)
            os.renames(path + "\\" + old_name, path + "\\" + new_name)
            cnt = cnt + 1
    print("%d files modified\n" % cnt)
    return cnt


def add_order_handle(filenames, ui_data):
    path = get_path(ui_data)
    print("the tar path is: %s\n" % path)
    order = 0
    for old_name in filenames:
        order = order + 1
        new_name = '[' + order.__str__() + '] ' + old_name
        os.renames(path + "\\" + old_name, path + "\\" + new_name)
    print("%d files modified\n" % order)
    return order


def add_prefix_handle(filenames, ui_data):
    path = get_path(ui_data)
    print("the tar path is: %s\n" % path)
    prefix = input("enter the prefix:")
    cnt = 0
    for old_name in filenames:
        new_name = prefix + old_name
        os.renames(path + "\\" + old_name, path + "\\" + new_name)
        cnt = cnt + 1
    print("%d files modified\n" % cnt)
    return cnt


def add_postfix_handle(filenames, ui_data):
    path = get_path(ui_data)
    print("the tar path is: %s\n" % path)
    postfix = input("enter the postfix:")
    cnt = 0
    for old_name in filenames:
        name = os.path.splitext(old_name)[0]
        ext = os.path.splitext(old_name)[1]
        new_name = name + postfix + ext
        os.renames(path + "\\" + old_name, path + "\\" + new_name)
        cnt = cnt + 1
    print("%d files modified\n" % cnt)
    return cnt


def insert_before_handle(filenames, ui_data):
    path = get_path(ui_data)
    print("the tar path is: %s\n" % path)
    flag_str = input("enter the flag str you want to insert str before(insert to the first str matched):")
    str = input("enter the str you want to insert:")
    cnt = 0
    for old_name in filenames:
        pos = old_name.find(flag_str)
        if pos >= 0:
            new_name = old_name[0:pos] + str + old_name[pos:]
            os.renames(path + "\\" + old_name, path + "\\" + new_name)
            cnt = cnt + 1
    if cnt == 0:
        print("no filename matched\n")
    print("%d files modified\n" % cnt)
    return cnt


def insert_after_handle(filenames, ui_data):
    path = get_path(ui_data)
    print("the tar path is: %s\n" % path)
    flag_str = input("enter the flag str you want to insert str before(insert to the first str matched):")
    str = input("enter the str you want to insert:")
    length = flag_str.__len__()
    cnt = 0
    for old_name in filenames:
        pos = old_name.find(flag_str)
        if pos >= 0:
            new_name = old_name[0:pos + length] + str + old_name[pos + length:]
            os.renames(path + "\\" + old_name, path + "\\" + new_name)
            cnt = cnt + 1
    if cnt == 0:
        print("no filename matched\n")
    print("%d files modified\n" % cnt)
    return cnt


def replace_ext_handle(filenames, ui_data):
    path = get_path(ui_data)
    print("the tar path is: %s\n" % path)
    new_ext = input("enter the new ext:")
    cnt = 0
    for old_name in filenames:
        name = os.path.splitext(old_name)[0]
        new_name = name + new_ext
        os.renames(path + "\\" + old_name, path + "\\" + new_name)
        cnt = cnt + 1
    print("%d files modified\n" % cnt)
    return cnt


if __name__ == "__main__":
    ui_data = ui()
    filenames = get_filenames(ui_data)
    mode = get_mode(ui_data)
    if mode == mode_dict["replace"]:
        replace_handle(filenames, ui_data)
    elif mode == mode_dict["add_order"]:
        add_order_handle(filenames, ui_data)
    elif mode == mode_dict["add_prefix"]:
        add_prefix_handle(filenames, ui_data)
    elif mode == mode_dict["add_postfix"]:
        add_postfix_handle(filenames, ui_data)
    elif mode == mode_dict["insert_str_before"]:
        insert_before_handle(filenames, ui_data)
    elif mode == mode_dict["insert_str_after"]:
        insert_after_handle(filenames, ui_data)
    elif mode == mode_dict["replace_ext"]:
        replace_ext_handle(filenames, ui_data)
    os.system("pause")

