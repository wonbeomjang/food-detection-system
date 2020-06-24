import os
import sqlite3
from config.config import get_config
from userMange.login import login

def switch(req, detection_dir='detection', switch_dir='user_data', db_name='switch.db'):
    config = get_config()
    id = req[config.user_id_name]
    dir_path = os.path.join(detection_dir, switch_dir)
    path = os.path.join(dir_path, db_name)

    num, id = login(req, config.user_info_dir, config.user_info_db)
    if num == False:
        return False

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if not os.path.exists(path):
        with sqlite3.connect(path) as conn:
            curs = conn.cursor()
            curs.execute('create table switch (id)')
            conn.commit()
            print("[*] create database for switch")

    with sqlite3.connect(path) as conn:
        curs = conn.cursor()
        curs.execute("SELECT * FROM switch")
        conn.commit()
        curs.execute("insert into switch values ('" + id + "')")
        conn.commit()
    return True
