import pymysql
from pymysql.cursors import Cursor

conn = pymysql.connect(
    user='root',
    passwd='rlatjdgns12',
    host='localhost',
    db = 'seantour',
    charset='utf8'
)
cursor = conn.cursor()

# sql = "CREATE DATABASE seantour"
sql = '''CREATE TABLE spot (
id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
time varchar(255),
name varchar(255),
light varchar(255)
)
'''

cursor.execute(sql)

conn.commit()
conn.close()