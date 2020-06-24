import os
import sqlite3
from userMange.register import register
from userMange.dbManage import createDB
from config.config import get_config

def login(req, user_dir, db_name):
    config = get_config()
    id = req[config.user_id_name]
    path = os.path.join(user_dir, db_name)

    if not os.path.exists(path):
        print("[!] there is no database for raspberry pi")
        createDB(user_dir, db_name)

    with sqlite3.connect(path) as conn:
        curs = conn.cursor()
        curs.execute("SELECT * FROM userManage")
        for info in curs.fetchall():
            if info[1] == id:
                num = info[0]
                print("[*] login %s/%s raspberry pi" % (str(num), str(id)))
                return num, id
    print("[!] there is no information of raspberry pi")

    return False, False
