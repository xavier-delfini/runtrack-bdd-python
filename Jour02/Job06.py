import mysqlConnection as mydb
cursor = mydb.db.cursor()
cursor.execute("SELECT SUM(capacite) FROM salles")
result = cursor.fetchone()[0]
print("La capacité de toutes les salles est de : "+str(result))