class Horario:
  def __init__(self, id, turno, hora, dia):
    self.__id = id
    self.__turno = turno
    self.__hora = hora
    self.__dia = dia
    
  def getId(self):
    return self.__id
  
  def getTurno(self):
    return self.__turno
  
  def getHora(self):
    return self.__hora
  
  def getDia(self):
    return self.__dia