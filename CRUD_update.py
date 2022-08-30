import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="db_roberto.mysql.dbaas.com.br",
  user="db_roberto",
  password="roberto",
  database="db_roberto"
)

cursor = connection.cursor()

sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
data = (
  'Ana Paula Perez',
  'comercial@absolemtech.com.br',
  2
)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, " registros alterados")