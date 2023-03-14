import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Wolololo1",
  database="zoo"
)
class cage:
    def __init__(self,cage_id,cage_superficie):
        __cage_id=cage_id
        __cage_superficie=cage_superficie

class animal:


class zoo(cage,animaux):
    def __ini__(self):
        super().__init__()


#SELECT * FROM zoo.animaux LEFT JOIN zoo.cage c on c.id = animaux.id_type_cage



