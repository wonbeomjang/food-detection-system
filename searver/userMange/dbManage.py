import os
import sqlite3


def createDB(user_dir, db_name):
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    if not os.path.exists(os.path.join(user_dir, db_name)):
        with sqlite3.connect(os.path.join(user_dir, 'userInfo.db')) as conn:
            curs = conn.cursor()
            curs.execute('create table userManage (num , user_id)')
            conn.commit()
            print("[*] create database for raspberry pi")
