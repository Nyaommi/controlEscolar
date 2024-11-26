import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
import database
import clases.alumno as alumno

def FrameMaterias(nba, mail):
  maestro = database.getTeacherByMail(mail)
  frameMaterias = ttk.Frame(nba)
  frameMaterias.grid_rowconfigure((0,1,2,3,4,5), weight=1)
  frameMaterias.grid_columnconfigure((0,1,2,3,4), weight=1)

  materiasN = []
  
  materiasI = database.getMateriasMaestro(maestro.getId())
  if materiasI:
    materiasN = database.getMateriasNombresMaestros(materiasI)
  
  listbox = tk.Listbox(frameMaterias, height=10, width=30, selectmode=tk.SINGLE)
  
  if materiasN:
    for item in materiasN:
      listbox.insert(tk.END, item[2])
  else:
    listbox.insert(tk.END, 'Parece que no tienen ninguna materia registrada')

  labelMaterias = ttk.Label(frameMaterias, text='Materias registradas')
  
  labelMaterias.grid(row=0, column=0)
  listbox.grid(row=1, column=0)
  
  ###
  
  labelMateriasDisponibles = ttk.Label(frameMaterias, text='Materias disponibles')

  listMateriasDisponibles = tk.Listbox(frameMaterias, height=10, width=30, selectmode=tk.SINGLE)
  materiasDisponibles = database.getMateriasDisponibles(maestro.getCarrera())
  
  if materiasDisponibles:
    for item in materiasDisponibles:
      listMateriasDisponibles.insert(tk.END, item[2])
  else:
    listMateriasDisponibles.insert(tk.END, 'Parece que no hay ninguna materia disponible')
  
  labelMateriasDisponibles.grid(row=0, column=1)
  listMateriasDisponibles.grid(row=1, column=1)
  
  def onClick(event):
    index = listMateriasDisponibles.nearest(event.y)
    print(materiasDisponibles[index][2])
    def registrarMateria(maestroId, materiaId):
      if database.registrarMateriaMaestro(maestroId, materiaId):
        messagebox.showinfo('La materia ha sido registrada', 'Has sido registrado para ofertar dicha materia')
      #database.checkMateria(maestroId, materiaId)

    buttonRegister = tk.Button(frameMaterias, text="Registrar materia", command=lambda:registrarMateria(maestro.getId(), materiasDisponibles[index][0]))
    buttonRegister.grid(row=5,column=0)

  listMateriasDisponibles.bind("<Button-1>", onClick)

  return frameMaterias  