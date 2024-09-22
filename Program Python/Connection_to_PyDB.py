 import mysql.connector
conn=mysql.connector.connect(user='root',password='babul',database='Employee',host='localhost',port=3306)
cursor=conn.cursor()
query="select * from EMPLOYEE"
cursor.execute(query)
rows=cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()
