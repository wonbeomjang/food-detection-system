from config.config import get_config
import os
import sqlite3


def delete_user_command(req):
    config = get_config()
    del_id = req[config.user_id_name]
    dir_path = os.path.join('detection', 'user_data')
    path = os.path.join(dir_path, 'switch.db')

    if not os.path.exists(os.path.join('detection', 'user_data')):
        return 'False'

    with sqlite3.connect(path) as conn:
        curs = conn.cursor()
        curs.execute("SELECT * FROM switch")
        for info in curs.fetchall():
            if info[0] == del_id:
                num = info[0]
                curs.execute("DELETE FROM switch WHERE id = '%s'" % (del_id))
                print("[*] delete command of %s raspberry pi" % (str(del_id)))
                return del_id

    return False