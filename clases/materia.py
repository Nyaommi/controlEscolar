class Materia:
  def __init__(self, id, carrera, asignatura, creditos, semestres):
    self.__id = id
    self.__carrera = carrera
    self.__asignatura = asignatura
    self.__creditos =creditos
    self.__semestres = semestres
    
  def getId(self):
    return self.__id
  
  def getCarrera(self):
    return self.__carrera
  
  def getAsignatura(self):
    return self.__asignatura
  
  def getCreditos(self):
    return self.__creditos
  
  def getSemestres(self):
    return  self.__semestres