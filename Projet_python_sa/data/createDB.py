from connectDB import conn, cursor;


cursor.execute("CREATE DATABASE IF NOT EXISTS Schoolsa ");

conn.commit();