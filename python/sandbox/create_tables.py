import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'denver',
  'password': 'Admin123',
  'host': '127.0.0.1',
  'database': 'trafficData',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)

cnx.close()


cnx = mysql.connector.connect(**conig)
cursor = cnx.cursor()

DB_NAME = 'trafficData'

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='denver')
cursor = cnx.cursor()

for name, ddl in TABLES.iteritems():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()

