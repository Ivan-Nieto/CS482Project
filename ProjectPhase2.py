import pymysql
import time

file1 = input("\nenter the file to read from: ")
filename = "/Users/acruz_42/Documents/NMSU 2.0/CS 482/NFL Project/" + file1
temp = file1.split(".")
table = temp[0]

def LoadDataInsert():
   #empty()
   try:
      connection = pymysql.connect(
         host = '127.0.0.1',
         user = 'root',
         password = 'passwd17',
         port = 3306,
         db = 'NFL',
         charset = 'utf8mb4',
         cursorclass = pymysql.cursors.DictCursor,
         local_infile=1
      )
      cursor = connection.cursor()
      starttime = time.time()
      sql = "LOAD DATA local INFILE '" + filename + "' INTO TABLE NFL." + table + " fields terminated BY ',' lines terminated BY '\n';"
      cursor.execute(sql)
      cursor.close()
      connection.commit()
      endtime = time.time()
      print(f"Load data insertion runtime: {endtime-starttime}")
   finally:
      connection.close()

def MultiRowInsert():
   try:
      connection = pymysql.connect(
         host = '127.0.0.1',
         user = 'root',
         password = 'passwd17',
         port = 3306,
         db = 'NFL',
         charset = 'utf8mb4',
         cursorclass = pymysql.cursors.DictCursor,
         local_infile=1
      )
      cursor = connection.cursor()
      f = open(filename,"r")
      starttime = time.time()
      sql = "INSERT INTO " + table + " VALUES "
      for line in f:
         line = line.strip("\n")
         data = line.split(",")
         for i in range(len(data)):
            if i == 0:
               sql = sql + "('" + data[i] + "'"
            elif i == len(data) - 1:
               sql = sql + ",'" + data[i] + "'),"
            else:
               sql = sql + ",'" + data[i] + "'"
      sql = sql[:-1]
      sql = sql + ";"
      cursor.execute(sql)
      f.close()
      cursor.close()
      connection.commit()
      endtime = time.time()
      print(f"Multi-row insertion runtime: {endtime-starttime}")
   finally:
      connection.close()

def SingleInsert():
   #empty()
   try:
      connection = pymysql.connect(
         host = '127.0.0.1',
         user = 'root',
         password = 'passwd17',
         port = 3306,
         db = 'NFL',
         charset = 'utf8mb4',
         cursorclass = pymysql.cursors.DictCursor,
         local_infile=1
      )
      cursor = connection.cursor()
      f = open(filename,"r")
      starttime = time.time()
      for line in f:
         line = line.strip("\n")
         data = line.split(",")
         sql = "INSERT INTO " + table + " VALUES ("
         for i in range(len(data)):
            if i == 0:
               sql = sql + "'" + data[i] + "'"
            else:
               sql = sql + ",'" + data[i] + "'"
         sql = sql + ");"
         cursor.execute(sql)
      f.close()
      cursor.close()
      connection.commit()
      endtime = time.time()
      print(f"Single insertion runtime: {endtime-starttime}")
   finally:
      connection.close()

def empty():
   try:
      connection = pymysql.connect(
         host = '127.0.0.1',
         user = 'root',
         password = 'passwd17',
         port = 3306,
         db = 'NFL',
         charset = 'utf8mb4',
         cursorclass = pymysql.cursors.DictCursor,
         local_infile=1
      )
      cursor = connection.cursor()
      cursor.execute("DELETE FROM players;")
      cursor.close()
      connection.commit()
   finally:
      connection.close()

def delete(tableName):
   try:
      connection = pymysql.connect(
         host = '127.0.0.1',
         user = 'root',
         password = 'passwd17',
         port = 3306,
         db = 'NFL',
         charset = 'utf8mb4',
         cursorclass = pymysql.cursors.DictCursor,
         local_infile=1
      )
      cursor = connection.cursor()
      cursor.execute("DELETE FROM " + tableName + ";")
      cursor.close()
      connection.commit()
   finally:
      connection.close()

def retrieve(tableName):
   try:
      connection = pymysql.connect(
         host = '127.0.0.1',
         user = 'root',
         password = 'passwd17',
         port = 3306,
         db = 'NFL',
         charset = 'utf8mb4',
         cursorclass = pymysql.cursors.DictCursor,
         local_infile=1
      )
      cursor = connection.cursor()
      cursor.execute("SELECT * FROM " + tableName + ";")
      string = cursor.fetchall()
      cursor.close()
      connection.commit()
   finally:
      connection.close()
   return str(string)

def average(tableName,columnName):
   try:
      connection = pymysql.connect(
         host = '127.0.0.1',
         user = 'root',
         password = 'passwd17',
         port = 3306,
         db = 'NFL',
         charset = 'utf8mb4',
         cursorclass = pymysql.cursors.DictCursor,
         local_infile=1
      )
      cursor = connection.cursor()
      cursor.execute("SELECT AVG(" + columnName + ") FROM " + tableName + ";")
      value = cursor.fetchall()
      cursor.close()
      connection.commit()
   finally:
      connection.close()
   return value

choice = int(input("Enter 1 for Load Data\nEnter 2 for Single Insertion\n3 for multi-row insert\nchoice = "))

if choice == 1:
   LoadDataInsert()
elif choice == 2:
   SingleInsert()
elif choice == 3:
   MultiRowInsert()
else:
   print("Not an option...\n")

print("\nEnd of Python Script\n")