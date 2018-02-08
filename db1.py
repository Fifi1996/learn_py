import mysql.connector
conn=mysql.connector.connect(user='root',password='root',database='test')
cursor=conn.cursor
cursor.execute('create table user(id VARCHAR (20) PRIMARY KEY ,name VARCHAR (20))')
cursor.execute('insert into user (id,name) VALUE (%s.%s)',['1','fi'])
cursor.rowcount
conn.commit()
cursor.close()