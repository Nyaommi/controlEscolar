class Salon:
  def __init__(self, id, nombre, edificio):
    self.__id = id
    self.__nombre = nombre
    self.__edificio = edificio
  
  def getId(self):
    return self.__id
  
  def getNombre(self):
    return self.__nombre
  
  def getEdificio(self):
    return self.__edificio