class Maestro:
  def __init__(self,id, nombre, aPaterno, aMaterno, fechaNacimiento, gradoEstudios, mail, password, carrera):
    self.__id =id
    self.__nombre =nombre
    self.__aPaterno =aPaterno
    self.__aMaterno =aMaterno
    self.__fechaNacimiento =fechaNacimiento
    self.__gradoEstudios =gradoEstudios
    self.__mail =mail
    self.__password =password
    self.__carrera =carrera

  def getId(self):
    return self.__id

  def getNombre(self):
    return self.__nombre

  def getAPaterno(self):
    return self.__aPaterno

  def getAMaterno(self):
    return self.__aMaterno

  def getFecha(self):
    return self.__fechaNacimiento

  def getEstudios(self):
    return self.__gradoEstudios

  def getMail(self):
    return self.__mail

  def getPassword(self):
    return self.__password

  def getCarrera(self):
    return self.__carrera