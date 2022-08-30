import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="db_roberto.mysql.dbaas.com.br",
  user="db_roberto",
  password="roberto",
  database="db_roberto"
)

cursor = connection.cursor()

sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"
data = (
  'Roberto Braga',
  'contato@absolemtech.com.br',
  datetime.datetime.today()
)

cursor.execute(sql, data)
connection.commit()

userid = cursor.lastrowid

cursor.close()
connection.close()

print("Foi cadastrado o novo usuário de ID:", userid)