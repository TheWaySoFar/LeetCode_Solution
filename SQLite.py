#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

def createDB():
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
        cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
        cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
        cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
    finally:
        cursor.close()
        conn.commit()
        conn.close()

def get_score_in(low, high):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(r'select name from user where score >=? and score <=? ORDER BY score', (low, high))
        #cursor.execute(r'select * from user')
        result = cursor.fetchall()
        #print(cursor.rowcount, 'fuck')
    finally:
        cursor.close()
        conn.commit()
        conn.close()
    names = list()
    for name in result:
        names.append(name[0])
    return names


# 测试:
if __name__ == '__main__':
    createDB()
    assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
    assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
    assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

    print('Pass')
