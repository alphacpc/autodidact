import mysql.connector;

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'Exercice1'
}

conn = mysql.connector.connect(**config);
cursor = conn.cursor();
