import mysql.connector
import json
import requests
import pysftp
import time
from pterodactyl import api_mysql
from secretinfo import api_key, ser_url,ssh_hos

#Warning!!! This script assumes that you have one mysql database on the desired server, if there is more than one database the request will fail.

input1 = input("Enter read or join: ")

server = api_mysql(api_key, ser_url)

database = server[0]
host = server[1]
port = server[2]
username = server[3]
password = server[4]

mydb = mysql.connector.connect(
  host=ssh_hos,
  user=username,
  password=password,
  database=database
)
if input1 =="read":
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM users1")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
  mycursor.execute("SELECT * FROM products")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

if input1 =="join":
  input2 = input("enter inner or outer: ")
  if input1 =="inner":
    mycursor = mydb.cursor()
    sql = "SELECT \
      users1.name AS user, \
      products.name AS favorite \
      FROM users \
      INNER JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  if input1 =="outer":
    mycursor = mydb.cursor()
    sql = "SELECT \
      users1.name AS user, \
      products.name AS favorite \
      FROM users \
      LEFT JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)