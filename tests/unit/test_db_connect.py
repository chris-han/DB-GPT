import pymysql

# Connect to the MySQL server with a 10-second timeout
conn = pymysql.connect(host='172.17.0.2', 
                       port=3306, 
                       user='root', 
                       password='aa12345678', 
                       db='mydb', 
                       connect_timeout=10)
