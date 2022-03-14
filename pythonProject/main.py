
from mysql.connector import connect
mydb= connect(
    host="localhost",
    user="root",
    password="",
    database="pythondatabase"
)
mycursor=mydb.cursor()
sql="drop database pythondatabase"
mycursor.execute(sql)




