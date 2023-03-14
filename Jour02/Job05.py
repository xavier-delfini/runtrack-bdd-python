import mysqlConnection as mydb
cursor = mydb.db.cursor()
cursor.execute("SELECT SUM(superficie) FROM etage")
result = cursor.fetchone()[0]
print("La superficie de La Plateforme est de "+str(result))