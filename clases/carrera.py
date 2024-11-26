class Carrera:
  def __init__(self, id, nombre, semestres):
    self.__id = id
    self.__nombre = nombre
    self.__semestres = semestres
    
  def getId(self):
    return self.__id
  
  def getNombre(self):
    return self.__nombre
  
  def getSemestres(self):
    return self.__semestres