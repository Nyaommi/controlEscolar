class Grupo:
  def __init__(self, id, nombre, fechaInicio, fechaFin, maxNumAlumnos, semestre, idCarrera, idMaestro, idMateria, idHorario, idSalon):
    self.__id=id
    self.__nombre=nombre
    self.__fechaInicio=fechaInicio
    self.__fechaFin=fechaFin
    self.__maxNumAlumnos=maxNumAlumnos
    self.__semestre=semestre
    self.__idCarrera=idCarrera
    self.__idMaestro=idMaestro
    self.__idMateria=idMateria
    self.__idHorario=idHorario
    self.__idSalon=idSalon
    
  def getId(self):
    return self.__id
  def getNombre(self):
    return self.__nombre
  def getFechaInicio(self):
    return self.__fechaInicio
  def getFechaFin(self):
    return self.__fechaFin
  def getMaxNumAlumnos(self):
    return self.__maxNumAlumnos
  def getSemestre(self):
    return self.__semestre
  def getIdCarrera(self):
    return self.__idCarrera
  def getIdMaestro(self):
    return self.__idMaestro
  def getIdMateria(self):
    return self.__idMateria
  def getIdHorario(self):
    return self.__idHorario
  def getIdSalon(self):
    return self.__idSalon