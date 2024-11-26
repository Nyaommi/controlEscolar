import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
import database
import clases.alumno as alumno

def FrameDatos(nba, mail):
  student = database.getStudentByMail(mail)
  frameDatos = ttk.Frame(nba)
  frameDatos.grid_rowconfigure((0,1,2), weight=1)
  frameDatos.grid_columnconfigure((0,1,2,3), weight=1)
  
  print(student.getNombre())
  print(student.getCarrera())
  
  labelDatos = ttk.Label(frameDatos, text='Tus datos')
  
  labelID = ttk.Label(frameDatos, text='ID:')
  labelNombre = ttk.Label(frameDatos, text='Nombre:')
  labelCarrera = ttk.Label(frameDatos, text='Carrera')
  labelEstado = ttk.Label(frameDatos, text='Estado')
  
  entryID = ttk.Entry(frameDatos, state=NORMAL)
  entryNombre = ttk.Entry(frameDatos, state=NORMAL)
  entryCarrera = ttk.Entry(frameDatos, state=NORMAL)
  entryEstado = ttk.Entry(frameDatos, state=NORMAL)
  
  fullName = f'{student.getAPaterno()} {student.getAMaterno()} {student.getNombre()}'
  
  entryID.insert(0, student.getId())
  entryNombre.insert(0, fullName)
  entryCarrera.insert(0, student.getCarrera())
  entryEstado.insert(0, student.getEstado())
  
  entryID.config(state='readonly')
  entryNombre.config(state='readonly')
  entryCarrera.config(state='readonly')
  entryEstado.config(state='readonly')
  
  labelDatos.grid(row=0, column=0)
  
  labelID.grid(row=1, column=0)
  labelNombre.grid(row=1, column=1)
  labelCarrera.grid(row=1, column=2)
  labelEstado.grid(row=1, column=3)
  
  entryID.grid(row=2, column=0)
  entryNombre.grid(row=2, column=1)
  entryCarrera.grid(row=2, column=2)
  entryEstado.grid(row=2, column=3)
  
  return frameDatos
