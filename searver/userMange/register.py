import os
import sqlite3
from userMange.dbManage import createDB
from config.config import get_config

def register(req, user_dir, db_name):
    config = get_config()
    id = req[config.user_id_name]
    path = os.path.join(user_dir, db_name)

    if not os.path.exists(path):
        createDB()

    with sqlite3.connect(path) as conn:
        curs = conn.cursor()
        curs.execute("SELECT * FROM userManage")
        num = str(len(curs.fetchall()) + 1)
        conn.commit()
        curs.execute("insert into userManage values ('" + num + "', '" + id + "')")
        conn.commit()

    return num, id
