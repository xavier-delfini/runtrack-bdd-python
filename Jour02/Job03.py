import mysqlConnection as mydb


def send_to_database(sql, arrayvalues):
    for value in arrayvalues:
        cursor.execute(sql,value )
        mydb.db.commit()


cursor = mydb.db.cursor()
etagecommand="INSERT INTO etage(nom,numero,superficie) VALUES(%s,%s,%s)"
etagevalues=[('RDC', 0, 500),('R+1', 1, 500)]
sallesvalues=[('Lounge', 1, 100),('Studio Son', 1, 5),('Broadcasting', 2, 50),('Bocal Peda', 2, 4),('Coworking', 2, 80),('Studio Video', 2, 5)]
sallecommand="INSERT INTO salles(nom,id_etage,capacite) VALUES(%s,%s,%s)"
send_to_database(etagecommand,etagevalues)
send_to_database(sallecommand,sallesvalues)