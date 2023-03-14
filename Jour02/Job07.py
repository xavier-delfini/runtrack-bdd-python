import basededonnéejob07 as mydb
def insert_values(sql, arrayvalues):
    for value in arrayvalues:
        cursor.execute(sql, value)
        mydb.db.commit()
cursor = mydb.db.cursor()
#CREATE DATABASE entreprise;
#cursor.execute("CREATE TABLE employes (id int NOT NULL AUTO_INCREMENT,nom varchar(255) NOT NULL,prenom varchar(255) NOT NULL,salaire decimal NOT NULL,id_service int NOT NULL,primary key (id))")
#sqlcommand=("INSERT INTO employes(nom,prenom,salaire,id_service) VALUES(%s,%s,%s,%s)")
#values=("Doe","John",3500,0),("Kojima","Hideo",5000,1),("Delfini","Xavier",2500,2),("Masahyro","Sakurai",5000,1)
#insert_values(sqlcommand,values)
cursor.execute("SELECT * FROM employes WHERE salaire>=3000")
print(cursor.fetchall())
#cursor.execute("CREATE TABLE service (id int NOT NULL AUTO_INCREMENT,nom varchar(255) NOT NULL,primary key (id))")
servicecommand="INSERT INTO service(nom) VALUES(%s)"
servicevalues=[("CEO"),("Director"),("JuniorDevelopper")]
insert_values(servicecommand,servicevalues)
cursor.execute("SELECT * FROM employes")
employes_list=cursor.fetchall()
cursor.execute("SELECT * FROM service")
service_list=cursor.fetchall()
def insert_service_name(employelist,service_list):
    new_employe_list=[]
    for employe in employelist:
        employe[4]=service_list[employe[4]]
        new_employe_list.append(employe)
    return new_employe_list
print(insert_service_name(employes_list,service_list))


#class table_employes:
    #def __init__(self,id=-1,nom="",prenom="",salaire=-1,id_service=-1):

    #def fetch_employe(self,nom,prenom):

