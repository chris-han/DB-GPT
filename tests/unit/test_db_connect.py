import pymysql

# Connect to the MySQL server with a 10-second timeout
conn = pymysql.connect(host='0.0.0.0', 
                       port=3306, 
                       user='root', 
                       password='aa12345678', 
                       db='mysql', 
                       connect_timeout=10)
#mysql -h 172.17.0.2 -u root -p
#GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'aa12345678' WITH GRANT OPTION;