import mysqlConnection as mydb
#Recuperer salles -> noms ,capacité
cursor = mydb.db.cursor()

cursor.execute("SELECT nom,capacite FROM salles")
print(cursor.fetchall())