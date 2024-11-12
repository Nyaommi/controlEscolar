import mysql.connector
import bcrypt
import clases.administrador as administrador
import clases.alumno as alumno
import clases.maestro as maestro
from tkinter import messagebox
import re

user = 'root'
password = 'cinna123'
database = 'controlescolar'
host = 'localhost' #it's all in localhost cause it's a shcollar proyect... but we could do it in a web server...

def passwordCheck(password):
  pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
  return bool(re.fullmatch(pattern, password))

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

def login(userType, mail, password):
  try:
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
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def carreraName(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select nombre from carreras where id = %s;'
    cursor1.execute(sql,(id,))
    carrera = cursor1.fetchone()
    conn.close()
    return carrera[0]
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def carreraList():
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select id, nombre from carreras;'
    cursor1.execute(sql)
    carreras = cursor1.fetchall()
    conn.close()
    carrerasN = [carrera[1] for carrera in carreras]
    carrerasI = [carrera[0] for carrera in carreras]
    return carrerasI, carrerasN
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

#- Admin Function -
  
def searchAdmin(id):
  try:
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
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')
  
def getCountAdmin():
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select auto_increment from information_schema.tables where table_name = \'administradores\' and table_schema = \'controlescolar\';'
    cursor1.execute(sql)
    total = cursor1.fetchone()
    conn.close()
    return total[0]
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def checkAdmin(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from administradores where id = %s;'
    cursor1.execute(sql,(id,))
    row = cursor1.fetchone()
    conn.close()
    return bool(row)
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def updateAdmin(admin):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'update administradores set usuario = %s, nombre = %s, apellidoPaterno = %s, apellidoMaterno = %s, mail = %s where id = %s;'
    cursor1.execute(sql,(admin.getUsuario(),admin.getNombre(),admin.getAPaterno(), admin.getAMaterno(), admin.getMail(), admin.getId()))
    conn.commit()
    conn.close()
    return True
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')
    return False
  
def createAdmin(admin):
  if passwordCheck(admin.getPassword()):
    try:
      conn = open()
      cursor1 = conn.cursor()
      sql = 'insert into administradores(usuario, password, nombre, apellidoPaterno, apellidoMaterno, mail) values(%s,%s,%s,%s,%s,%s);'
      cursor1.execute(sql,(admin.getUsuario(),hashPassword(admin.getPassword()),admin.getNombre(),admin.getAPaterno(), admin.getAMaterno(), admin.getMail()))
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
      return False
  else:
    messagebox.showerror('Contrasena no valida', 'Porfavor introduzca un contrasena que cumpla con:\n-Minimo 6 caracteres\n-Minimo una mayuscula\n-Minimo un numero\n-Minimo un simbolo especial')
  
def deleteAdmin(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'delete from administradores where id = %s;'
    cursor1.execute(sql,(id,))
    conn.commit()
    conn.close()
    messagebox.showinfo('Usuario eliminado', f'El usuario con el id {id} ha sido eliminado de la base de datos')
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
  
#- Student Functions -\
def searchStudent(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from alumnos where id = %s;'
    cursor1.execute(sql, (id,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      aux = alumno.Alumno(row[0],row[1],row[2],row[3],row[4],row[8],row[7],carreraName(row[6]), [])
      return aux
    else:
      return None
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def getCountStudent():
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select auto_increment from information_schema.tables where table_name = \'alumnos\' and table_schema = \'controlescolar\';'
    cursor1.execute(sql)
    total = cursor1.fetchone()
    conn.close()
    return total[0]
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def checkStudent(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from alumnos where id = %s;'
    cursor1.execute(sql,(id,))
    row = cursor1.fetchone()
    conn.close()
    return bool(row)
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def updateStudent(student, idCarrera):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'update alumnos set nombre = %s, apellidoPaterno = %s, apellidoMaterno = %s, mail = %s, idCarrera = %s, fechaNacimiento = str_to_date(%s, \'%m/'+'%'+'d/%y\'), estado = %s where id = %s;'
    cursor1.execute(sql,(student.getNombre(),student.getAPaterno(), student.getAMaterno(), student.getMail(), idCarrera, student.getFechaNacimiento(), student.getEstado(), student.getId()))
    conn.commit()
    conn.close()
    return True
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
    return False
  
def createStudent(student, password, idCarrera):
  if passwordCheck(password):
    try:
      conn = open()
      cursor1 = conn.cursor()
      sql = 'insert into alumnos(nombre, apellidoPaterno, apellidoMaterno, mail, password, idCarrera, fechaNacimiento, estado) values(%s,%s,%s,%s,%s,%s,str_to_date(%s, \'%m/'+'%'+'d/%y\'),%s);'
      cursor1.execute(sql,(student.getNombre(),student.getAPaterno(), student.getAMaterno(), student.getMail(), hashPassword(password), idCarrera, student.getFechaNacimiento(), student.getEstado()))
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
      return False
  else:
    messagebox.showerror('Contrasena no valida', 'Porfavor introduzca un contrasena que cumpla con:\n-Minimo 6 caracteres\n-Minimo una mayuscula\n-Minimo un numero\n-Minimo un simbolo especial')
  
def deleteStudent(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'delete from alumnos where id = %s;'
    cursor1.execute(sql,(id,))
    conn.commit()
    conn.close()
    messagebox.showinfo('Alumno eliminado', f'El alumno con el id {id} ha sido eliminado de la base de datos')
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

#- Teachers Functions -\
def searchTeacher(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from maestros where id = %s;'
    cursor1.execute(sql, (id,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      aux = maestro.Maestro(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],carreraName(row[8]))
      return aux
    else:
      return None
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def getCountTeacher():
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select auto_increment from information_schema.tables where table_name = \'maestros\' and table_schema = \'controlescolar\';'
    cursor1.execute(sql)
    total = cursor1.fetchone()
    conn.close()
    return total[0]
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def checkTeacher(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from maestros where id = %s;'
    cursor1.execute(sql,(id,))
    row = cursor1.fetchone()
    conn.close()
    return bool(row)
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def updateTeacher(teacher, idCarrera):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'update maestros set nombre = %s, apellidoPaterno = %s, apellidoMaterno = %s, mail = %s, idCarrera = %s, fechaNacimiento = str_to_date(%s, \'%m/'+'%'+'d/%y\'), gradoEstudios = %s where id = %s;'
    cursor1.execute(sql,(teacher.getNombre(),teacher.getAPaterno(), teacher.getAMaterno(), teacher.getMail(), idCarrera, teacher.getFecha(), teacher.getEstudios(), teacher.getId()))
    conn.commit()
    conn.close()
    return True
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
    return False
  
def createTeacher(teacher, password, idCarrera):
  if passwordCheck(password):
    try:
      conn = open()
      cursor1 = conn.cursor()
      sql = 'insert into maestros(nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, gradoEstudios, mail, password, idCarrera) values(%s,%s,%s,str_to_date(%s, \'%m/'+'%'+'d/%y\'),%s,%s,%s,%s);'
      cursor1.execute(sql,(teacher.getNombre(),teacher.getAPaterno(), teacher.getAMaterno(), teacher.getFecha(), teacher.getEstudios(), teacher.getMail(), hashPassword(password), idCarrera))
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
      return False
  else:
    messagebox.showerror('Contrasena no valida', 'Porfavor introduzca un contrasena que cumpla con:\n-Minimo 6 caracteres\n-Minimo una mayuscula\n-Minimo un numero\n-Minimo un simbolo especial')
  
def deleteTeacher(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'delete from maestros where id = %s;'
    cursor1.execute(sql,(id,))
    conn.commit()
    conn.close()
    messagebox.showinfo('Maestro eliminado', f'El maestro con el id {id} ha sido eliminado de la base de datos')
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
