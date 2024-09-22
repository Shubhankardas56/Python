import mysql.connector
try:
    conn=mysql.connector.connect(user='root',password='babul',host='localhost',port=3306)
    print("Connection Established")
    
except:
    print("Connection Error")