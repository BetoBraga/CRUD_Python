import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="db_roberto.mysql.dbaas.com.br",
  user="db_roberto",
  password="roberto",
  database="db_roberto"
)

cursor = connection.cursor()

sql = "SELECT * FROM users"

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
  print(result)