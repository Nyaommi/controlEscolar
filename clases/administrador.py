class Administrador:
  def __init__(self, id, usuario, password, nombre, apellidoPaterno, apellidoMaterno, mail):
    self.__id = id
    self.__usuario = usuario
    self.__password = password
    self.__nombre = nombre
    self.__apellidoPaterno = apellidoPaterno
    self.__apellidoMaterno = apellidoMaterno
    self.__mail = mail
  
  def getId(self):
    return self.__id
  def getUsuario(self):
    return self.__usuario
  def getPassword(self):
    return self.__password
  def getNombre(self):
    return self.__nombre
  def getAPaterno(self):
    return self.__apellidoPaterno
  def getAMaterno(self):
    return self.__apellidoMaterno
  def getMail(self):
    return self.__mail