import mysql.connector;

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost'
}

conn = mysql.connector.connect(**config);
cursor = conn.cursor();