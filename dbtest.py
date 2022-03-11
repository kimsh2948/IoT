from typing import Any, Union

import pymysql
from seleniumtest import *
from pymysql.cursors import Cursor

conn = pymysql.connect(
    user='root',
    passwd='rlatjdgns12',
    host='localhost',
    db='seantour',
    charset='utf8'
)
cursor = conn.cursor()

sql = "INSERT INTO spot (time, name, light) VALUES (%s, %s, %s)"

if __name__ == '__main__':
    cursor.execute(sql, (time_t, hwajin.text, light_hwajin))
    cursor.execute(sql, (time_t, songcamping.text, light_songcamping))
    cursor.execute(sql, (time_t, songjiho.text, light_songiho))
    cursor.execute(sql, (time_t, sampo.text, light_sampo))
    cursor.execute(sql, (time_t, chunjin.text, light_chunjin))
    cursor.execute(sql, (time_t, deung.text, light_deung))
    cursor.execute(sql, (time_t, sokcho.text, light_sokcho))
    cursor.execute(sql, (time_t, waiong.text, light_waiong))

    # cursor.execute(sql)

    conn.commit()
    conn.close()

