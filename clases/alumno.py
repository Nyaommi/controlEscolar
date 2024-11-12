class Alumno:
  def __init__(self, id, nombre, aPaterno, aMaterno, email, estado, fechaNacimiento, carrera, materias):
    self.__id=id
    self.__nombre =nombre
    self.__aPaterno=aPaterno
    self.__aMaterno=aMaterno
    self.__email=email
    self.__estado=estado
    self.__fechaNacimiento=fechaNacimiento
    self.__carrera=carrera
    self.__materias=materias

  def getId(self):
    return self.__id
  def getNombre(self):
    return self.__nombre
  def getAPaterno(self):
    return self.__aPaterno
  def getAMaterno(self):
    return self.__aMaterno
  def getMail(self):
    return self.__email
  def getEstado(self):
    return self.__estado
  def getFechaNacimiento(self):
    return self.__fechaNacimiento
  def getCarrera(self):
    return self.__carrera
  def getMaterias(self):
    return self.__materias