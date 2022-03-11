import mysql.connector;

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'Schoolsa'
}

conn = mysql.connector.connect(**config);
cursor = conn.cursor();