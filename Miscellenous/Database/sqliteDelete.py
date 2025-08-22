import sqlite3
conn=sqlite3.connect('testdb.sqlite3')
cur=conn.cursor()
qry="DELETE FROM EMPLOYEE WHERE EMPID<?"

try:
   # Execute the SQL command
   cur.execute(qry, (2,))
   # Fetch all the rows in a list of lists.
   conn.commit()
   print ("Records deleted")
except Exception as e:
   print ("Error: unable to delete data")

conn.close()