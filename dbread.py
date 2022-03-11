import pymysql
from pymysql.cursors import Cursor

conn = pymysql.connect(
    user='root',
    passwd='rlatjdgns12',
    host='localhost',
    db='seantour',
    charset='utf8'
)
cursor = conn.cursor()

sql = "SELECT * FROM spot where light = %s"

cursor.execute(sql, ("green"))
res = cursor.fetchall()

for data in res:
        print(data)

conn.commit()
conn.close()