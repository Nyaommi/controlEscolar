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
  frameGrupos.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)
  frameGrupos.grid_columnconfigure((0,1,2,3,4), weight=1)

  carrerasI, carrerasN = database.carreraList()
  salonI, salonN = database.salonList()

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
  labelAlumno = ttk.Label(frameGrupos, text='Max. num. alumnos:')

  entryBusqueda = ttk.Entry(frameGrupos, width=20)
  entryID = ttk.Entry(frameGrupos, state='readonly')
  entryNombre = ttk.Entry(frameGrupos, state='readonly')
  entryFecha = DateEntry(frameGrupos, background='darkblue', foreground='white', borderwidth=2, state=DISABLED)
  entryCarrera = ttk.Combobox(frameGrupos, values=carrerasN, state=DISABLED)
  entryMateria = ttk.Combobox(frameGrupos, state=DISABLED)
  entryMaestro = ttk.Combobox(frameGrupos, state=DISABLED)
  entrySalon = ttk.Combobox(frameGrupos, values=salonN, state=DISABLED)
  entryHorario = ttk.Combobox(frameGrupos, state=DISABLED)
  entrySemestre = ttk.Entry(frameGrupos, state='readonly')
  entryAlumno =ttk.Spinbox(frameGrupos, state='readonly', from_=10, to=50)

  buttonBuscar = ttk.Button(frameGrupos, text='Buscar', command=lambda:buscar(entryBusqueda.get()))
  buttonNuevo = ttk.Button(frameGrupos, text='Nuevo', command=lambda:nuevo())
  buttonGuardar = ttk.Button(frameGrupos, text='Guardar', state="disabled", command=lambda:guardar())
  buttonCancelar = ttk.Button(frameGrupos, text='Cancelar', state="disabled", command=lambda:cancelar())
  buttonEditar = ttk.Button(frameGrupos, text='Editar', state="disabled", command=lambda:editar())
  buttonBaja = ttk.Button(frameGrupos, text='Baja', state="disabled", command=lambda:baja())


  def buscar(id):
    pass
  
  def nuevo():
    entryID.config(state=NORMAL)
    entryID.delete(0, tk.END)
    entryID.insert(0, str(database.getCountGroup()))
    entryID.config(state='readonly')
    entryNombre.config(state=NORMAL)
    entryNombre.delete(0, tk.END)
    entryFecha.config(state=NORMAL)
    entryFecha.set_date(date.today())
    entryFecha.config(state='readonly')
    entryCarrera.config(state='readonly')
    entrySalon.config(state='readonly')
    #entryHorario.config(state=NORMAL)
    #entryHorario.
    entrySemestre.config(state=NORMAL)
    entrySemestre.delete(0, tk.END)
    entryAlumno.config(state=NORMAL)
  
  def guardar():
    pass
  
  def cancelar():
    pass
  
  def editar():
    pass
  
  def baja():
    pass

  labelBusqueda.grid(row=0, column=1, sticky=E)
  entryBusqueda.grid(row=0, column=2, sticky=W+E)
  buttonBuscar.grid(row=0, column=3, sticky=W)

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
  
  labelMaestro.grid(row=1, column=2)
  entryMaestro.grid(row=1, column=3, sticky=W+E)
  labelSalon.grid(row=2, column=2)
  entrySalon.grid(row=2, column=3, sticky=W+E)
  labelHorario.grid(row=3, column=2)
  entryHorario.grid(row=3, column=3, sticky=W+E)
  labelSemestre.grid(row=4, column=2)
  entrySemestre.grid(row=4, column=3, sticky=W+E)
  labelAlumno.grid(row=5, column=2)
  entryAlumno.grid(row=5, column=3, sticky=W+E)
  
  buttonNuevo.grid(row=6, column=0)
  buttonGuardar.grid(row=6, column=1)
  buttonCancelar.grid(row=6, column=2)
  buttonEditar.grid(row=6, column=3)
  buttonBaja.grid(row=6, column=4)

  return frameGrupos
  #matertiasI, materiasN = database.materiaList()