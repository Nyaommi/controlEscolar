import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
import database
import clases.alumno as alumno

def FrameAgenda(nba, mail):
  student = database.getStudentByMail(mail)
  idCarrera = database.getCarreraByMail(mail)
  frameAgenda = ttk.Frame(nba)
  frameAgenda.grid_rowconfigure((0,1,2,3,4,5), weight=1)
  frameAgenda.grid_columnconfigure((0,1,2,3,4), weight=1)
  
  gruposI = database.getMateriasAlumno(student.getId())
  if gruposI:
    materiasAlumnoN = database.getMateriasNombres(gruposI)
  
  listbox = tk.Listbox(frameAgenda, height=10, width=30, selectmode=tk.SINGLE)
  
  if materiasAlumnoN:
    for item in materiasAlumnoN:
      listbox.insert(tk.END, item[2])
  else:
    listbox.insert(tk.END, 'Parece que no tienen ninguna materia registrada')
  
  labelMaterias = ttk.Label(frameAgenda, text='Materias registradas')
  
  labelMaterias.grid(row=0, column=0)
  listbox.grid(row=1, column=0)
  
  labelMateriasDisponibles = ttk.Label(frameAgenda, text='Materias disponibles')

  listMateriasDisponibles = tk.Listbox(frameAgenda, height=10, width=30, selectmode=tk.SINGLE)
  materiasDisponibles = database.getMateriasDisponibles(idCarrera)
  
  if materiasDisponibles:
    for item in materiasDisponibles:
      listMateriasDisponibles.insert(tk.END, item[2])
  else:
    listMateriasDisponibles.insert(tk.END, 'Parece que no hay ninguna materia disponible')
  
  labelMateriasDisponibles.grid(row=0, column=1)
  listMateriasDisponibles.grid(row=1, column=1)
  
  print(f'Materias disponibles: {materiasDisponibles}')
  
  def onClick(event):
    index = listMateriasDisponibles.nearest(event.y)
    if index >= 0:
      indexMateria = materiasDisponibles[index][0]
    print(indexMateria)
    alumnosTotal, gruposList = database.getGruposDisponibles(indexMateria)
    print(alumnosTotal)
    print(gruposList)
      
    listGruposDisponibles = tk.Listbox(frameAgenda, height=10, width=30, selectmode=tk.SINGLE)
    labelGrupos = tk.Label(frameAgenda, text='Grupos disponibles')
    
    for i in gruposList:
      if i[4] > alumnosTotal[gruposList.index(i)]:
        listGruposDisponibles.insert(tk.END, f'Maestro: {database.getNombreMaestro(i[7])} | Horario: {database.getHorario(i[9])} | Inicio: {i[2]} | Fin: {i[3]} | Salon: {database.getSalon(i[10])}')
    
    def onClick2(event):
      index2 = listGruposDisponibles.nearest(event.y)
      buttonRegister = tk.Button(frameAgenda, text="Registrar materia", command=lambda:registrarMateria(student.getId(), index2))
      buttonRegister.grid(row=5,column=0)
    
    listGruposDisponibles.bind("<Button-1>", onClick2)
    
    def registrarMateria(idAlumno, idMateria):
      if database.registrarMateria(idAlumno, gruposList[idMateria][0], gruposList[idMateria][8], gruposList[idMateria][9]):
        messagebox.showinfo('La materia ha sido registrada', 'Has sido registrado en el grupo seleccionado')
        #By this point everything is soooooo fucked up xd, but this thing have to be turned in tomorrow...
    
    labelGrupos.grid(row=2, column=0)
    listGruposDisponibles.grid(row=3, column=0, sticky='we', columnspan=5)
      
  listMateriasDisponibles.bind("<Button-1>", onClick)
  
  return frameAgenda