#! /usr/bin/env python
#coding=utf-8
import sys
import requests
import re
import os
import openpyxl
def check_url(url):
    try:
        request=requests.get(url)
        if(request.status_code==200):
            return True
        else:
            return False
    except :
        return False

def checkip(ip):
    try:
        status = os.system('ping -n 2 -w 1 %s' % ip)  # 每个ip ping2次，等待时间为1s
        print(status)
        if(status):
            return False
        else:
            return True
    except:
        return False

def valid_ip(ip):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip):
        return True
    else:
        return False

def read_file(file):

    workbook=openpyxl.load_workbook(file)
    booksheet=workbook.get_sheet_by_name('Sheet1')
    rows=booksheet.rows
    colums=booksheet.columns
    fi_ok = open('result_ok.txt', 'a')
    fi_error = open("result_error", "a")
    for row in rows:
        for col in row:
            str=col.value
            if valid_ip(str):
                st = checkip(str)
            else:
                st = check_url("http://"+str)
            if (st):
                print(str+" ok!")
                fi_ok.write(str)
            else:
                fi_error.write(str)
    fi_ok.close()
    fi_error.close()


if __name__ == '__main__':

    read_file("1.xlsx")

