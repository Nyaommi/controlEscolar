import mysql.connector
import bcrypt
import clases.administrador as administrador
import clases.alumno as alumno
import clases.maestro as maestro
import clases.materia as materia
import clases.grupo as grupo
import clases.horario as horario
import clases.salon as salon
import clases.carrera as carrera
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
  conn = mysql.connector.connect(host = host, user = user, passwd = password, database = database, charset='utf8mb4', collation='utf8mb4_unicode_ci')
  return conn

def close():
  conn = open()
  conn.close()

def login(mail, password):
  users = ['administradores', 'alumnos', 'maestros']
  userType = ''
  row = None
  try:
    conn = open()
    cursor1 = conn.cursor()
    for user in users:
      userType = user
      sql = 'select password from '+user+' where mail = %s;'
      cursor1.execute(sql, (mail,))
      row = cursor1.fetchone()
      if row:
        if verifyPassword(password, row[0]):
          return True, userType
          conn.close()
        else:
          return False, None
          conn.close()
    conn.close()
    return 'noUser', None
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')
    return None, None
  
def mailCheck(mail):
  users = ['administradores', 'alumnos', 'maestros']
  try:
    for user in users:
      conn = open()
      cursor1 = conn.cursor()
      sql = 'select mail from '+user+' where mail = %s;'
      cursor1.execute(sql, (mail,))
      row = cursor1.fetchone()
      conn.close()
      if row:
        return True
    return False
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def classCheck(asignatura):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from materias where asignatura = %s;'
    cursor1.execute(sql, (asignatura,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      return True
    return False
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def groupCheck(name):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from grupos where nombre = %s;'
    cursor1.execute(sql, (name,))
    row = cursor1.fetchone()
    conn.close()
    return bool(row)
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')


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
  except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def materiaList(idCarrera):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select id, asignatura from materias where idCarrera = %s;'
    cursor1.execute(sql, (idCarrera,))
    materias = cursor1.fetchall()
    conn.close()
    materiasN = [materia[1] for materia in materias]
    materiasI = [materia[0] for materia in materias]
    return materiasI, materiasN
  except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def salonList():
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select id, nombre from salones;'
    cursor1.execute(sql)
    salones = cursor1.fetchall()
    conn.close()
    salonN = [salon[1] for salon in salones]
    salonI = [salon[0] for salon in salones]
    return salonI, salonN
  except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def maestrosList(idMateria):
  maestrosI = []
  maestrosN = []
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select idMaestro from maestrosmaterias where idMateria = %s;'
    cursor1.execute(sql,(idMateria,))
    aux = cursor1.fetchall()
    maestrosI = [id[0] for id in aux]
    for id in maestrosI:
      sql = 'SELECT nombre, apellidoPaterno FROM maestros WHERE id = %s;'
      cursor1.execute(sql,(id,))
      aux = cursor1.fetchall()
      if aux:
        nc = f'{aux[0][0]} {aux[0][1]}'
        maestrosN.append(nc)
    conn.close()
    return maestrosI, maestrosN
  except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def horariosList(idSalon):
  horariosI = []
  horariosN = []
  horariosId = []
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select distinct idHorario from grupos where idSalon = %s;'
    cursor1.execute(sql,(idSalon,))
    aux = cursor1.fetchall()
    if not(aux):
      horariosId.append(0)
    else:
      horariosId = [id[0] for id in aux]
    placeholders = ', '.join(['%s'] * len(horariosId))    
    sql = f'SELECT * FROM horarios WHERE id not in ({placeholders});'
    cursor1.execute(sql,horariosId)
    aux = cursor1.fetchall()
    if aux:
      for row in aux:
        nc = f'{row[3]} {row[2]}'
        horariosI.append(row[0])
        horariosN.append(nc)
    conn.close()
    return horariosI, horariosN
  except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def searchHorario(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select dia, hora from horarios where id = %s;'
    cursor1.execute(sql,(id,))
    aux = cursor1.fetchall()
    conn.close()
    if aux:
      nc = f'{aux[0][0]} {aux[0][1]}'
      return nc
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
    return ''


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
  if not mailCheck(admin.getMail()):
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
  else:
    messagebox.showerror('Usuario ya existente', 'El mail ya esta registrado en nuestra base de datos')

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
def getStudentByMail(mail):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from alumnos where mail = %s;'
    cursor1.execute(sql, (mail,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      aux = alumno.Alumno(row[0],row[1],row[2],row[3],row[4],row[8],row[7],carreraName(row[6]), [])
      return aux
    else:
      return None
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def getCarreraByMail(mail):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from alumnos where mail = %s;'
    cursor1.execute(sql, (mail,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      return row[6]
    else:
      return None
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def getMateriasDisponibles(idCarrera):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from materias where idCarrera = %s;'
    cursor1.execute(sql, (idCarrera,))
    row = cursor1.fetchall()
    conn.close()
    if row:
      print(row)
      materias = [materia for materia in row]
      return materias
    else:
      return None
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')
  
def getMateriasAlumno(idA):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select idGrupo from alumnosgrupos where idAlumno = %s;'
    cursor1.execute(sql, (idA,))
    grupos = cursor1.fetchall()
    conn.close()
    if grupos:
      gruposI = [grupo[0] for grupo in grupos]
      return gruposI
    else:
      return []
  except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def getMateriasMaestro(idA):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select idMateria from maestrosmaterias where idMaestro = %s;'
    cursor1.execute(sql, (idA,))
    grupos = cursor1.fetchall()
    conn.close()
    if grupos:
      gruposI = [grupo[0] for grupo in grupos]
      return gruposI
    else:
      return []
  except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def registrarMateriaMaestro(maestroId, materiaId):
    if checkMateria(maestroId, materiaId):
      messagebox.showerror('Materia ya registrada', 'Parece que ya estas registrado a esta materia')
    else:
      try:
        conn = open()
        cursor1 = conn.cursor()
        sql = 'insert into maestrosmaterias(idMaestro, idMateria) values(%s, %s);'
        cursor1.execute(sql, (maestroId, materiaId))
        conn.commit()
        conn.close()
        return True
      except Exception as e:
        messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
        print(e)
        return False

def checkMateria(maestroId, materiaId):
  try:
    flag = False
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select idMateria from maestrosmaterias where idMaestro = %s;'
    cursor1.execute(sql, (maestroId,))
    aux = cursor1.fetchall()
    conn.close()
    for i in aux:
      if materiaId == i[0]:
        flag = True
    return flag
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')


def getMateriasNombresMaestros(materiasI):
  try:
    conn = open()
    cursor1 = conn.cursor()
    placeholders = ', '.join(['%s'] * len(materiasI))
    sql = f'select * from materias WHERE id IN ({placeholders});'
    cursor1.execute(sql, tuple(materiasI))
    materias = cursor1.fetchall()
    conn.close()
    if materias:
      materiasN = [materia for materia in materias]
      return materiasN
    else:
      return []
  except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')


def getMateriasNombres(ids):
  try:
    materiasI = []
    conn = open()
    cursor1 = conn.cursor()
    placeholders = ', '.join(['%s'] * len(ids))
    sql = f'select * from grupos WHERE id IN ({placeholders});'
    cursor1.execute(sql, tuple(ids))
    grupos = cursor1.fetchall()
    if grupos:
      materiasI = [grupo[8] for grupo in grupos]
    conn.close()
    conn = open()
    cursor1 = conn.cursor()
    placeholders = ', '.join(['%s'] * len(materiasI))
    sql = f'select * from materias WHERE id IN ({placeholders});'
    cursor1.execute(sql, tuple(materiasI))
    materias = cursor1.fetchall()
    conn.close()
    if materias:
      materiasN = [materia for materia in materias]
      return materiasN
    else:
      return []
  except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def getGruposDisponibles(idMateria):
  try:
    grupos = []
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from grupos WHERE idMateria = %s;'
    cursor1.execute(sql, (idMateria,))
    grupos = cursor1.fetchall()
    if grupos:
      gruposList = [grupo for grupo in grupos]
      print(f'Grupos list: {gruposList}')
      gruposId = [grupo[0] for grupo in grupos]
    conn.close()
    conn = open()
    cursor1 = conn.cursor()
    alumnosTotal = []
    for i in gruposId:
      sql = 'select count(*) as alumnos from alumnosgrupos WHERE idGrupo = %s;'
      cursor1.execute(sql, (i,))
      alumnos = cursor1.fetchall()
      alumnosTotal.append(alumnos[0][0])
    conn.close()
    if alumnos:
      print(f'Total alumnos:{alumnosTotal}')
      return alumnosTotal, gruposList
    else:
      return []
  except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

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
  if not mailCheck(student.getMail()):
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
  else:
    messagebox.showerror('Usuario ya existente', 'El mail ya esta registrado en nuestra base de datos')

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

#- Teachers Functions -
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
  if not mailCheck(teacher.getMail()):
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
  else:
    messagebox.showerror('Usuario ya existente', 'El mail ya esta registrado en nuestra base de datos')

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

#- Clases Functions -
def searchClass(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from materias where id = %s;'
    cursor1.execute(sql, (id,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      aux = materia.Materia(row[0],carreraName(row[1]),row[2],row[3],row[4])
      return aux
    else:
      return None
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def getCountMaterias():
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select auto_increment from information_schema.tables where table_name = \'materias\' and table_schema = \'controlescolar\';'
    cursor1.execute(sql)
    total = cursor1.fetchone()
    conn.close()
    return total[0]
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def checkClass(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from materias where id = %s;'
    cursor1.execute(sql,(id,))
    row = cursor1.fetchone()
    conn.close()
    return bool(row)
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def updateClass(clas, idCarrera):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'update materias set idCarrera = %s, asignatura = %s, creditos = %s, semestre = %s where id = %s;'
    cursor1.execute(sql,(idCarrera, clas.getAsignatura(), clas.getCreditos(), clas.getSemestres(), clas.getId()))
    conn.commit()
    conn.close()
    return True
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
    return False
  
def createClass(clas, idCarrera):
  if not classCheck(clas.getAsignatura()):
    try:
      conn = open()
      cursor1 = conn.cursor()
      sql = 'insert into materias(idCarrera, asignatura, creditos, semestre) values(%s,%s,%s,%s);'
      cursor1.execute(sql,(idCarrera, clas.getAsignatura(), clas.getCreditos(), clas.getSemestres()))
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
      return False
  else:
    messagebox.showerror('La materia ya existe', 'La materia ya esta en nuestra base de datos')

#- Groups Functions -
def searchGroup(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from grupos where id = %s;'
    cursor1.execute(sql, (id,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      aux = grupo.Grupo(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8], row[9], row[10])
      return aux
    else:
      return None
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def getCountGroup():
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select auto_increment from information_schema.tables where table_name = \'grupos\' and table_schema = \'controlescolar\';'
    cursor1.execute(sql)
    total = cursor1.fetchone()
    conn.close()
    return total[0]
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def checkGroup(groupName):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from grupos where id = %s;'
    cursor1.execute(sql,(groupName,))
    row = cursor1.fetchone()
    conn.close()
    return bool(row)
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')
    
def updateGroup(group):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'update grupos set nombre = %s, fechaInicio = str_to_date(%s, \'%m/'+'%'+'d/%y\'), fechaFin = str_to_date(%s, \'%m/'+'%'+'d/%y\'), maxNumeroAlumnos = %s, semestre = %s, idCarrera = %s, idMaestro = %s, idHorario = %s, idSalon = %s where id = %s;'
    cursor1.execute(sql,(group.getNombre(), group.getFechaInicio(), group.getFechaFin(), group.getMaxNumAlumnos(), group.getSemestre(), group.getIdCarrera(), group.getIdMaestro(), group.getIdHorario(), group.getIdSalon(), group.getId()))
    conn.commit()
    conn.close()
    return True
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
    return False

def createGroup(group):
  if not groupCheck(group.getNombre()):
    try:
      conn = open()
      cursor1 = conn.cursor()
      sql = 'insert into grupos(nombre, fechaInicio, fechaFin, maxNumeroAlumnos, semestre, idCarrera, idMaestro, idMateria, idHorario, idSalon) values(%s,str_to_date(%s, \'%m/'+'%'+'d/%y\'),str_to_date(%s, \'%m/'+'%'+'d/%y\'),%s,%s,%s,%s,%s,%s,%s);'
      cursor1.execute(sql,(group.getNombre(), group.getFechaInicio(), group.getFechaFin(), group.getMaxNumAlumnos(), group.getSemestre(), group.getIdCarrera(), group.getIdMaestro(), group.getIdMateria(), group.getIdHorario(), group.getIdSalon()))
      print(sql)
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
      return False
  else:
    messagebox.showerror('Grupo ya existente', 'El nombre del grupo ya esta registrado en nuestra base de datos')
    
def deleteGroup(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'delete from grupos where id = %s;'
    cursor1.execute(sql,(id,))
    conn.commit()
    conn.close()
    messagebox.showinfo('Grupo eliminado', f'El grupo con el id {id} ha sido eliminado de la base de datos')
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

#- Schedule Functions -
def searchSchedule(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from horarios where id = %s;'
    cursor1.execute(sql, (id,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      aux = horario.Horario(row[0],row[1],row[2],row[3])
      return aux
    else:
      return None
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def getCountSchedule():
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select auto_increment from information_schema.tables where table_name = \'horarios\' and table_schema = \'controlescolar\';'
    cursor1.execute(sql)
    total = cursor1.fetchone()
    conn.close()
    return total[0]
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def updateSchedule(schedule):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'update horarios set turno = %s, hora = %s, dia = %s where id = %s;'
    cursor1.execute(sql,(schedule.getTurno(), schedule.getHora(), schedule.getDia(), schedule.getId()))
    conn.commit()
    conn.close()
    return True
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
    return False
  

def scheduleCheck(turno, hora, dia):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from horarios where turno = %s and hora = %s and dia = %s;'
    cursor1.execute(sql, (turno, hora, dia))
    row = cursor1.fetchone()
    conn.close()
    if row:
      return True
    return False
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def checkSchedule(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from horarios where id = %s;'
    cursor1.execute(sql,(id,))
    row = cursor1.fetchone()
    conn.close()
    return bool(row)
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')


def createSchedule(schedule):
  if not scheduleCheck(schedule.getTurno(), schedule.getHora(), schedule.getDia()):
    try:
      conn = open()
      cursor1 = conn.cursor()
      sql = 'insert into horarios(turno, hora, dia) values(%s,%s,%s);'
      cursor1.execute(sql,(schedule.getTurno(), schedule.getHora(), schedule.getDia()))
      print(sql)
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
      return False
  else:
    messagebox.showerror('Horario ya existente', 'El horario ya esta registrado en nuestra base de datos')

def deleteSchedule(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'delete from horarios where id = %s;'
    cursor1.execute(sql,(id,))
    conn.commit()
    conn.close()
    messagebox.showinfo('Horario eliminado', f'El horario con el id {id} ha sido eliminado de la base de datos')
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

#- Classroom functions -
def getCountClassroom():
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select auto_increment from information_schema.tables where table_name = \'salones\' and table_schema = \'controlescolar\';'
    cursor1.execute(sql)
    total = cursor1.fetchone()
    conn.close()
    return total[0]
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def checkClassroom(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from salones where id = %s;'
    cursor1.execute(sql,(id,))
    row = cursor1.fetchone()
    conn.close()
    return bool(row)
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def searchClassroom(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from salones where id = %s;'
    cursor1.execute(sql, (id,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      aux = salon.Salon(row[0],row[1],row[2])
      return aux
    else:
      return None
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def updateClassroom(classroom):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'update salones set nombre = %s, edificio = %s where id = %s;'
    cursor1.execute(sql,(classroom.getNombre(), classroom.getEdificio(), classroom.getId()))
    conn.commit()
    conn.close()
    return True
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
    return False
  
def createClassroom(classroom):
  if not classroomCheck(classroom.getNombre(), classroom.getEdificio()):
    try:
      conn = open()
      cursor1 = conn.cursor()
      sql = 'insert into salones(nombre, edificio) values(%s,%s);'
      cursor1.execute(sql,(classroom.getNombre(), classroom.getEdificio()))
      print(sql)
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
      return False
  else:
    messagebox.showerror('Salon ya existente', 'El salon ya esta registrado en nuestra base de datos')

def classroomCheck(nombre, edificio):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from salones where nombre = %s and edificio = %s;'
    cursor1.execute(sql, (nombre, edificio))
    row = cursor1.fetchone()
    conn.close()
    if row:
      return True
    return False
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def deleteClassroom(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'delete from salones where id = %s;'
    cursor1.execute(sql,(id,))
    conn.commit()
    conn.close()
    messagebox.showinfo('Salon eliminado', f'El salon con el id {id} ha sido eliminado de la base de datos')
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

#- Carrers functions -
def getCountCarrer():
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select auto_increment from information_schema.tables where table_name = \'carreras\' and table_schema = \'controlescolar\';'
    cursor1.execute(sql)
    total = cursor1.fetchone()
    conn.close()
    return total[0]
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def checkCarrer(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from carreras where id = %s;'
    cursor1.execute(sql,(id,))
    row = cursor1.fetchone()
    conn.close()
    return bool(row)
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def searchCarrer(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from carreras where id = %s;'
    cursor1.execute(sql, (id,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      aux = carrera.Carrera(row[0],row[1],row[2])
      return aux
    else:
      return None
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def updateCarrer(carrer):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'update carreras set nombre = %s, semestres = %s where id = %s;'
    cursor1.execute(sql,(carrer.getNombre(), carrer.getSemestres(), carrer.getId()))
    conn.commit()
    conn.close()
    return True
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
    return False
  
def createCarrer(carrer):
  if not carrerCheck(carrer.getNombre()):
    try:
      conn = open()
      cursor1 = conn.cursor()
      sql = 'insert into carreras(nombre, semestres) values(%s,%s);'
      cursor1.execute(sql,(carrer.getNombre(), carrer.getSemestres()))
      print(sql)
      conn.commit()
      conn.close()
      return True
    except Exception as e:
      messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
      return False
  else:
    messagebox.showerror('Carrera ya existente', 'La carrera ya esta registrado en nuestra base de datos')

def carrerCheck(nombre):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from carreras where nombre = %s;'
    cursor1.execute(sql, (nombre))
    row = cursor1.fetchone()
    conn.close()
    if row:
      return True
    return False
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def deleteCarrer(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'delete from carreras where id = %s;'
    cursor1.execute(sql,(id,))
    conn.commit()
    conn.close()
    messagebox.showinfo('Carrera eliminada', f'La carrera con el id {id} ha sido eliminada de la base de datos')
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def getNombreMaestro(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'SELECT CONCAT(apellidoPaterno, " ", apellidoMaterno, " ", nombre) AS nombreCompleto from maestros where id = %s;'
    cursor1.execute(sql, (id,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      return row[0]
    else:
      return None
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def getNombreMaestro(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'SELECT CONCAT(apellidoPaterno, " ", apellidoMaterno, " ", nombre) AS nombreCompleto from maestros where id = %s;'
    cursor1.execute(sql, (id,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      return row[0]
    else:
      return None
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def getHorario(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'SELECT CONCAT(dia, " ", hora) AS hora from horarios where id = %s;'
    cursor1.execute(sql, (id,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      return row[0]
    else:
      return None
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def getSalon(id):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'SELECT nombre from salones where id = %s;'
    cursor1.execute(sql, (id,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      return row[0]
    else:
      return None
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def registrarMateria(idAlumno, idGrupo, idMateria, idHorario):
  if checkGrupo(idAlumno, idMateria):
    messagebox.showerror('Materia ya registrada', 'Parece que ya estas registrado a esta materia')
  else:
    if checkCruce(idAlumno, idHorario):
      messagebox.showerror('Cruce de horarios', 'Parece que ya tienes otra clase registrada en ese horario')
    else:
      try:
        conn = open()
        cursor1 = conn.cursor()
        sql = 'insert into alumnosgrupos(idAlumno, idGrupo) values(%s, %s);'
        cursor1.execute(sql, (idAlumno, idGrupo))
        conn.commit()
        conn.close()
        return True
      except Exception as e:
        messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
        print(e)
        return False

def checkGrupo(idAlumno, idMateria):
  try:
    flag = False
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select idGrupo from alumnosgrupos where idAlumno = %s;'
    cursor1.execute(sql, (idAlumno,))
    row = cursor1.fetchall()
    conn.close()
    if row:
      for i in row:
        conn = open()
        cursor1 = conn.cursor()
        sql = 'select idMateria from grupos where id = %s;'
        cursor1.execute(sql, (i[0],))
        aux = cursor1.fetchone()
        conn.close()
        if idMateria == aux[0]:
          flag = True
      return flag
    else:
      return None
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def checkCruce(idAlumno, idHorario):
  try:
    flag = False
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select idGrupo from alumnosgrupos where idAlumno = %s;'
    cursor1.execute(sql, (idAlumno,))
    row = cursor1.fetchall()
    conn.close()
    if row:
      for i in row:
        conn = open()
        cursor1 = conn.cursor()
        sql = 'select idHorario from grupos where id = %s;'
        cursor1.execute(sql, (i[0],))
        aux = cursor1.fetchone()
        conn.close()
        if idHorario == aux[0]:
          flag = True
      return flag
    else:
      return None
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def getHorarioAlumno(idAlumno):
  try:
    horario = []
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select idGrupo from alumnosgrupos where idAlumno = %s;'
    cursor1.execute(sql, (idAlumno,))
    row = cursor1.fetchall()
    conn.close()
    if row:
      for i in row:
        horarioRow = []
        conn = open()
        cursor1 = conn.cursor()
        sql = 'select idMaestro, idMateria, idHorario, idSalon from grupos where id = %s;'
        cursor1.execute(sql, (i[0],))
        auxMaster = cursor1.fetchone()
        conn.close()
        
        conn = open()
        cursor1 = conn.cursor()
        sql = 'select hora, dia from horarios where id = %s;'
        cursor1.execute(sql, (auxMaster[2],))
        aux = cursor1.fetchone()
        conn.close()
        
        horarioRow.extend(aux)
        
        conn = open()
        cursor1 = conn.cursor()
        sql = 'select (select asignatura from materias where id = %s) as a, (select concat(nombre, " ", apellidoPaterno) as nc from maestros where id = %s)as m, (select nombre from salones where id = %s) as s;'
        cursor1.execute(sql, (auxMaster[1], auxMaster[0], auxMaster[3]))
        aux = cursor1.fetchone()
        conn.close()
        
        horarioRow.append(f'{aux[0]}\n{aux[1]}\n{aux[2]}')
        
        horario.append(horarioRow)
    return horario
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def getHorarioMaestro(idMaestro):
  try:
    horario = []
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from grupos where idMaestro = %s;'
    cursor1.execute(sql, (idMaestro,))
    row = cursor1.fetchall()
    conn.close()
    if row:
      for i in row:
        horarioRow = []
        conn = open()
        cursor1 = conn.cursor()
        sql = 'select idMaestro, idMateria, idHorario, idSalon from grupos where id = %s;'
        cursor1.execute(sql, (i[0],))
        auxMaster = cursor1.fetchone()
        conn.close()
        
        conn = open()
        cursor1 = conn.cursor()
        sql = 'select hora, dia from horarios where id = %s;'
        cursor1.execute(sql, (auxMaster[2],))
        aux = cursor1.fetchone()
        conn.close()
        
        horarioRow.extend(aux)
        
        conn = open()
        cursor1 = conn.cursor()
        sql = 'select (select asignatura from materias where id = %s) as a, (select concat(nombre, " ", apellidoPaterno) as nc from maestros where id = %s)as m, (select nombre from salones where id = %s) as s;'
        cursor1.execute(sql, (auxMaster[1], auxMaster[0], auxMaster[3]))
        aux = cursor1.fetchone()
        conn.close()
        
        horarioRow.append(f'{aux[0]}\n{aux[1]}\n{aux[2]}')
        
        horario.append(horarioRow)
    return horario
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')

def getTeacherByMail(mail):
  try:
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from maestros where mail = %s;'
    cursor1.execute(sql, (mail,))
    row = cursor1.fetchone()
    conn.close()
    if row:
      aux = maestro.Maestro(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
      return aux
    else:
      return None
  except:
    messagebox.showerror('Error con la base de datos', 'Parece que tenemos problemas para comunicarnos con la base de datos')

def getPlaneacion():
  try:
    planeacion = []
    conn = open()
    cursor1 = conn.cursor()
    sql = 'select * from grupos;'
    cursor1.execute(sql)
    row = cursor1.fetchall()
    conn.close()
    if row:
      for i in row:
        auxrow = f'Grupo: {i[1]}'
        conn = open()
        cursor1 = conn.cursor()
        sql = 'select nombre from salones where id = %s;'
        cursor1.execute(sql, (i[10],))
        aux = cursor1.fetchone()
        conn.close()
        
        auxrow += f'\nSalon: {aux[0]}'
        
        conn = open()
        cursor1 = conn.cursor()
        sql = 'select asignatura from materias where id = %s;'
        cursor1.execute(sql, (i[8],))
        aux = cursor1.fetchone()
        conn.close()
        
        auxrow += f'\nMateria: {aux[0]}'
        
        conn = open()
        cursor1 = conn.cursor()
        sql = 'select dia, hora from horarios where id = %s;'
        cursor1.execute(sql, (i[9],))
        aux = cursor1.fetchone()
        conn.close()
        
        auxrow += f'\nHorario: {aux[0]}\n{aux[1]}'
        
        planeacion.append(auxrow)
        print(f'Planeacion: {planeacion}')
    return planeacion
  except Exception as e:
    messagebox.showerror('Error con la base de datos', f'Parece que tenemos problemas para comunicarnos con la base de datos: {e}')
    print(e)