import mysql.connector;

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'Lemgui'
}

conn = mysql.connector.connect(**config)

if conn.is_connected():
    db_Info = conn.get_server_info()

    print("Connexion à MySQL Server version ", db_Info)

    cursor = conn.cursor()

else:
    print("Impossible de se connecter sur la base de données")

