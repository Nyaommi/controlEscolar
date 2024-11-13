import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime
import database

def FrameGrupos(nb):
  frameGrupos = ttk.Frame(nb)
  frameGrupos.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
  frameGrupos.grid_columnconfigure((0,1,2,3,4), weight=1)

  carrerasI, carrerasN = database.carreraList()

  labelBusqueda = ttk.Label(frameGrupos, text='Ingrese el ID de grupo:')
  labelID = ttk.Label(frameGrupos, text='ID:')
  labelNombre = ttk.Label(frameGrupos, text='Nombre grupo:')
  labelFecha = ttk.Label(frameGrupos, text='Fecha:')
  labelCarrera = ttk.Label(frameGrupos, text='Carrera')
  labelMateria = ttk.Label(frameGrupos, text='Materia:')
  labelMaestro = ttk.Label(frameGrupos, text='Maestro:')
  labelSalon = ttk.Label(frameGrupos, text='Salon:')
  labelHorario = ttk.Label(frameGrupos, text='Horario')
  labelSemestre = ttk.Label(frameGrupos, text='Semestre:')
  labelAlumnos = ttk.Label(frameGrupos, text='Max. num. alumnos:')

  entryBusqueda = ttk.Entry(frameGrupos, width=20)
  entryID = ttk.Entry(frameGrupos, state='readonly')
  entryNombre = ttk.Entry(frameGrupos, state='readonly')
  entryFecha = DateEntry(frameGrupos, background='darkblue', foreground='white', borderwidth=2, state=DISABLED)
  entryCarrera = ttk.Combobox(frameGrupos, values=carrerasN, state=DISABLED)
  entryMateria = ttk.Combobox(frameGrupos, state=DISABLED)
  entryMaestro = ttk.Combobox(frameGrupos, state=DISABLED)
  entrySalon = ttk.Combobox(frameGrupos, state=DISABLED)
  entryHorario = ttk.Combobox(frameGrupos, state=DISABLED)
  entrySemestre = ttk.Entry(frameGrupos, state='readonly')
  entryAlumno =ttk.Entry(frameGrupos, state='readonly', show='*')

  labelID.grid(row=1, column=0)
  entryID.grid(row=1, column=1, sticky=W+E)
  labelNombre.grid(row=2, column=0)
  entryNombre.grid(row=2, column=1, sticky=W+E)
  labelFecha.grid(row=3, column=0)
  entryFecha.grid(row=3, column=1, sticky=W+E)
  labelCarrera.grid(row=4, column=0)
  entryCarrera.grid(row=4, column=1, sticky=W+E)
  labelMateria.grid(row=5, column=0)
  entryMateria.grid(row=5, column=1, sticky=W+E)

  #matertiasI, materiasN = database.materiaList()