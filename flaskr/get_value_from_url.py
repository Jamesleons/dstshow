#!/usr/bin/env python


import urllib2
import time
import sqlite3


def get_value():


    f = urllib2.urlopen('http://mcache.oss.letv.com/queue/dump?type=0')
    value_list = f.read()[1:-1].split("}, ")
    print value_list
    for i in value_list:
        record = i[1:]
        username = record.split(",")[0].split(":")[-1]
        reply = record.split(",")[1].split(":")[-1]
        ptime = int(time.strftime("%Y%m%d%H%M"))/5*5
        sql = "insert into dstshow('ptime','username','reply') values(%s,%s,%s)"%(ptime,username,reply)
        cur.execute(sql)
        conn.commit()
    cur.execute("select * from dstshow")
    result = cur.fetchall()
    print result




def db_conn():
    conn = sqlite3.connect('dstshow.db')
    cur = conn.cursor()
    return cur


def db_close():
    pass


if __name__ == '__main__':
    conn = sqlite3.connect('dstshow.db')
    cur = conn.cursor()

    get_value()

    conn.close()



