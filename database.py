import mysql.connector
import bcrypt
import administrador

user = 'root'
password = 'cinna123'
database = 'controlescolar'
host = 'localhost' #it's all in localhost cause it's a shcollar proyect... but we could do it in a web server.

def hashPassword(password):
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(password.encode(), salt)
  return hashed_password

def verifyPassword(password, hashedPassword):
  if isinstance(password, str):
      password = password.encode() 
  if isinstance(hashedPassword, str):
      hashedPassword = hashedPassword.encode()
  return bcrypt.checkpw(password, hashedPassword)

def open():
  conn = mysql.connector.connect(host = host, user = user, passwd = password, database = database)
  return conn

def close():
  conn = open()
  conn.close()

def update():
  hp = hashPassword('Cinna123')
  conn = open()
  cursor1 = conn.cursor()
  sql = 'update administradores set password = %s where id = 1'
  cursor1.execute(sql, (hp,))
  conn.commit()
  conn.close()

def login(userType, mail, password):
  conn = open()
  cursor1 = conn.cursor()
  sql = 'select * from '+userType+' where mail = %s;'
  cursor1.execute(sql, (mail,))
  row = cursor1.fetchone()
  conn.close()
  if row:
    if verifyPassword(password, row[2]):
      return True
    else:
      return False
  else:
    return('noUser')
  
def searchAdmin(id):
  conn = open()
  cursor1 = conn.cursor()
  sql = 'select * from administradores where id = %s;'
  cursor1.execute(sql, (id,))
  row = cursor1.fetchone()
  conn.close()
  if row:
    aux = administrador.Administrador(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    return aux
  else:
    return None