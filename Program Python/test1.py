import mysql.connector
# clean way for connection
config={
    'user':'root',
    'password':'babul',
    'port':3306,
    'database':'Employee',
    'host':'localhost'  
}
try:
    conn=mysql.connector.connect(**config)
    if (conn.is_connected()):# is_connected return True if connection is Established
        print('connected')
except:
    print('Connection Error')
def Show_Db():
    # Showing all Database
    sql='SHOW DATABASES'
    # Use of Cursor
    my_coursor=conn.cursor()
    my_coursor.execute(sql)
    j=1
    for i in my_coursor:
        print(f'Number{j}: {i}')
        j+=1
def Create_Db():
    Db_name=input('Enter Your Database Name To Create:')
    # Creating Database
    sql='CREATE DATABASE'+' '+Db_name
    # Use of Cursor
    my_coursor=conn.cursor()
    my_coursor.execute(sql)
def Create_Tb():
    col=int(input('Enter number of column to Input:'))
    i=1
    for ele in range(col):
        input(f'Enter {i} column name:')
        i+=1
    # Creating Database
    # sql=
    # Use of Cursor
    my_coursor=conn.cursor()
    my_coursor.execute(sql)
# Show_Db() 
# Create_Db()
# Show_Db()
Create_Tb()
# closing connection
conn.close()
