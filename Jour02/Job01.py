import mysqlConnection as mydb

cursor=mydb.db.cursor()
cursor.execute("SELECT * FROM etudiants")
print(cursor.fetchall())
