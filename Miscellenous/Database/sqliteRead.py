import sqlite3

conn = sqlite3.connect('testdb.sqlite3')
cur = conn.cursor()

qry = """SELECT * FROM EMPLOYEE"""
try:
    rows = cur.execute(qry)
    for row in rows:
        print(row)
except:
    conn.rollback()
print('error in read operation')
conn.close()
