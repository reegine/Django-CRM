#install MySQL on your computer
# community version
# pip install mysql
# pip install mysql-connector  --> ini kalo butu aja
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'toor',

)

#prepare cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All done!")