import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime
import database
import clases.grupo as grupo

def FrameGrupos(nb):
  frameGrupos = ttk.Frame(nb)
  frameGrupos.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)
  frameGrupos.grid_columnconfigure((0,1,2,3,4), weight=1)

  carrerasI, carrerasN = database.carreraList()
  salonI, salonN = database.salonList()
  materiasI, materiasN = [],[]
  maestrosI, maestrosN = [],[]
  horariosI, horariosN = [],[]

  labelBusqueda = ttk.Label(frameGrupos, text='Ingrese el ID de grupo:')
  labelID = ttk.Label(frameGrupos, text='ID:')
  labelNombre = ttk.Label(frameGrupos, text='Nombre grupo:')
  labelFechaI = ttk.Label(frameGrupos, text='Fecha inicio:')
  labelFechaF = ttk.Label(frameGrupos, text='Fecha fin:')
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
  entryFechaI = DateEntry(frameGrupos, background='darkblue', foreground='white', borderwidth=2, state=DISABLED)
  entryFechaF = DateEntry(frameGrupos, background='darkblue', foreground='white', borderwidth=2, state=DISABLED)
  entryCarrera = ttk.Combobox(frameGrupos, values=carrerasN, state=DISABLED)
  entryCarrera.bind("<<ComboboxSelected>>", lambda event:setMaterias(carrerasI[entryCarrera['values'].index(entryCarrera.get())]))
  entryMateria = ttk.Combobox(frameGrupos, state=DISABLED)
  entryMaestro = ttk.Combobox(frameGrupos, state=DISABLED)
  entrySalon = ttk.Combobox(frameGrupos, values=salonN, state=DISABLED)
  entrySalon.bind("<<ComboboxSelected>>", lambda event:setHorarios(salonI[entrySalon['values'].index(entrySalon.get())]))
  entryHorario = ttk.Combobox(frameGrupos, state=DISABLED)
  entrySemestre = ttk.Entry(frameGrupos, state='readonly')
  entryAlumno =ttk.Spinbox(frameGrupos, state='readonly', from_=10, to=50)

  buttonBuscar = ttk.Button(frameGrupos, text='Buscar', command=lambda:buscar(entryBusqueda.get()))
  buttonNuevo = ttk.Button(frameGrupos, text='Nuevo', command=lambda:nuevo())
  buttonGuardar = ttk.Button(frameGrupos, text='Guardar', state="disabled", command=lambda:guardar())
  buttonCancelar = ttk.Button(frameGrupos, text='Cancelar', state="disabled", command=lambda:cancelar())
  buttonEditar = ttk.Button(frameGrupos, text='Editar', state="disabled", command=lambda:editar())
  buttonBaja = ttk.Button(frameGrupos, text='Baja', state="disabled", command=lambda:baja())

  def setMaterias(idCarrera):
    global materiasI, materiasN
    entryMateria.configure(values=[])
    entryMateria.set('')
    entryMateria.config(state=DISABLED)
    entryMaestro.configure(values=[])
    entryMaestro.set('')
    entryMaestro.config(state=DISABLED)
    materiasI, materiasN = database.materiaList(idCarrera)
    if materiasN:
      entryMateria.configure(values=materiasN)
      entryMateria.set(materiasN[0])
      entryMateria.config(state='readonly')
      entryMateria.bind("<<ComboboxSelected>>", lambda event:setMaestros(materiasI[entryMateria['values'].index(entryMateria.get())]))

  def setMaestros(idMateria):
    global maestrosI, maestrosN
    entryMaestro.configure(values=[])
    entryMaestro.set('')
    entryMaestro.config(state=DISABLED)
    maestrosI, maestrosN = database.maestrosList(idMateria)
    if maestrosN:
      entryMaestro.configure(values=maestrosN)
      entryMaestro.set(maestrosN[0])
      entryMaestro.config(state='readonly')

  def setHorarios(idSalon):
    global horariosI, horariosN
    entryHorario.configure(values=[])
    entryHorario.set('')
    entryHorario.config(state=DISABLED)
    horariosI, horariosN = database.horariosList(idSalon)
    if horariosN:
      entryHorario.configure(values=horariosN)
      entryHorario.set(horariosN[0])
      entryHorario.config(state='readonly')

  def buscar(id):
    global maestrosI, maestrosN, materiasI, materiasN, horariosI, horariosN
    group = database.searchGroup(id)
    if group == None:
      messagebox.showwarning('Grupo no encontrado', 'Parece que no tenemos ningun grupo con ese ID')
    else:
      entryID.config(state=NORMAL)
      entryID.delete(0, tk.END)
      entryID.insert(0, str(group.getId()))
      entryID.config(state='readonly')
      entryNombre.config(state=NORMAL)
      entryNombre.delete(0, tk.END)
      entryNombre.insert(0, group.getNombre())
      entryNombre.config(state='readonly')
      entryFechaI.config(state=NORMAL)
      entryFechaI.set_date(group.getFechaInicio())
      entryFechaI.config(state=DISABLED)
      entryFechaF.config(state=NORMAL)
      entryFechaF.set_date(group.getFechaFin())
      entryFechaF.config(state=DISABLED)
      entryCarrera.config(state=NORMAL)
      entryCarrera.set(carrerasN[carrerasI.index(group.getIdCarrera())])
      entryCarrera.config(state=DISABLED)
      entrySalon.config(state=NORMAL)
      entrySalon.set(salonN[salonI.index(group.getIdSalon())])
      entrySalon.config(state=DISABLED)
      entryHorario.config(state=NORMAL)
      setHorarios(group.getIdSalon())
      entryHorario.set(database.searchHorario(group.getIdHorario()))
      horariosN = [database.searchHorario(group.getIdHorario())]
      horariosI = [group.getIdHorario()]
      entryHorario.config(state=DISABLED)
      entrySemestre.config(state=NORMAL)
      entrySemestre.delete(0, tk.END)
      entrySemestre.insert(0, group.getSemestre())
      entrySemestre.config(state='readonly')
      entryAlumno.config(state=NORMAL)
      entryAlumno.delete(0, tk.END)
      entryAlumno.insert(0, group.getMaxNumAlumnos())
      entryAlumno.config(state=DISABLED)
      setMaestros(group.getIdMateria())
      setMaterias(group.getIdCarrera())
      entryMaestro.config(state=NORMAL)
      entryMaestro.set(maestrosN[maestrosI.index(group.getIdMaestro())])
      entryMaestro.config(state=DISABLED)
      entryMateria.config(state=NORMAL)
      entryMateria.set(materiasN[materiasI.index(group.getIdMateria())])
      entryMateria.config(state=DISABLED)
    
      buttonNuevo.config(state=NORMAL)
      buttonGuardar.config(state='disabled')
      buttonCancelar.config(state=NORMAL)
      buttonEditar.config(state=NORMAL)
      buttonBaja.config(state=NORMAL)
  
  def nuevo():
    entryID.config(state=NORMAL)
    entryID.delete(0, tk.END)
    entryID.insert(0, str(database.getCountGroup()))
    entryID.config(state='readonly')
    entryNombre.config(state=NORMAL)
    entryNombre.delete(0, tk.END)
    entryFechaI.config(state=NORMAL)
    entryFechaI.set_date(date.today())
    entryFechaI.config(state='readonly')
    entryFechaF.config(state=NORMAL)
    entryFechaF.set_date(date.today())
    entryFechaF.config(state='readonly')
    entryCarrera.config(state='readonly')
    entrySalon.config(state='readonly')
    entryHorario.config(values=[])
    entryHorario.set('')
    entryHorario.config(state=DISABLED)
    entrySemestre.config(state=NORMAL)
    entrySemestre.delete(0, tk.END)
    entryAlumno.config(state='readonly')
    
    setMaterias(0)
    setMaestros(0)
    
    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
  
  def guardar():
    global maestrosI, maestrosN, materiasI, materiasN, horariosI, horariosN
    if database.checkGroup(entryID.get()):
      idSalon = salonI[entrySalon['values'].index(entrySalon.get())]
      idCarrera = carrerasI[entryCarrera['values'].index(entryCarrera.get())]
      entryMaestro['values'] = maestrosN
      idMaestro = maestrosI[entryMaestro['values'].index(entryMaestro.get())]
      idMateria = materiasI[entryMateria['values'].index(entryMateria.get())]
      entryHorario['values'] = horariosN
      idHorario = horariosI[entryHorario['values'].index(entryHorario.get())]
      if all (field != '' for field in (entryNombre.get(), entryFechaI.get(), entryFechaF.get(), entryCarrera.get(), entryMateria.get(), entryMaestro.get(), entrySalon.get(), entryHorario.get(), entrySemestre.get(), entryAlumno.get())):
        group = grupo.Grupo(entryID.get(), entryNombre.get(), entryFechaI.get(), entryFechaF.get(), entryAlumno.get(), entrySemestre.get(), idCarrera, idMaestro, idMateria, idHorario, idSalon)
        if database.updateGroup(group):
          messagebox.showinfo('Grupo actualizado', f'Los datos del grupo: {group.getNombre()} han sido actualizados')
          cancelar()
        else:
          print('Error')
      else:
        messagebox.showwarning('Campos incompletos', 'Por favor llene todos los campos')
    else:
      if all (field != '' for field in (entryNombre.get(), entryFechaI.get(), entryFechaF.get(), entryCarrera.get(), entryMateria.get(), entryMaestro.get(), entrySalon.get(), entryHorario.get(), entrySemestre.get(), entryAlumno.get())):
        idSalon = salonI[entrySalon['values'].index(entrySalon.get())]
        idCarrera = carrerasI[entryCarrera['values'].index(entryCarrera.get())]
        idMaestro = maestrosI[entryMaestro['values'].index(entryMaestro.get())]
        idMateria = materiasI[entryMateria['values'].index(entryMateria.get())]
        idHorario = horariosI[entryHorario['values'].index(entryHorario.get())]
        group = grupo.Grupo(entryID.get(), entryNombre.get(), entryFechaI.get(), entryFechaF.get(), entryAlumno.get(), entrySemestre.get(), idCarrera, idMaestro, idMateria, idHorario, idSalon)
        if database.createGroup(group):
          messagebox.showinfo('Grupo registrado', f'Se ha registrado el grupo {group.getNombre()} con el ID: {group.getId()}')
          cancelar()
        else:
          print('Error')
      else:
        messagebox.showwarning('Campos incompletos', 'Por favor llene todos los campos')
  def cancelar():
    entryID.config(state=NORMAL)
    entryID.delete(0, tk.END)
    entryID.config(state='readonly')
    entryNombre.config(state=NORMAL)
    entryNombre.delete(0, tk.END)
    entryNombre.config(state=DISABLED)
    entryFechaI.config(state=NORMAL)
    entryFechaI.set_date(date.today())
    entryFechaI.config(state=DISABLED)
    entryFechaF.config(state=NORMAL)
    entryFechaF.set_date(date.today())
    entryFechaF.config(state=DISABLED)
    entryCarrera.set('')
    entryCarrera.config(state=DISABLED)
    entrySalon.set('')
    entrySalon.config(state=DISABLED)
    entryHorario.config(values=[])
    entryHorario.set('')
    entryHorario.config(state=DISABLED)
    entrySemestre.config(state=NORMAL)
    entrySemestre.delete(0, tk.END)
    entrySemestre.config(state=DISABLED)
    entryAlumno.config(state=DISABLED)
    
    setMaterias(0)
    setMaestros(0)
    
    buttonNuevo.config(state=NORMAL)
    buttonGuardar.config(state='disabled')
    buttonCancelar.config(state='disabled')
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
    
  def editar():
    entryNombre.config(state=NORMAL)
    entryFechaI.config(state=NORMAL)
    entryFechaF.config(state='readonly')
    entryCarrera.config(state='readonly')
    entrySalon.config(state='readonly')
    entryHorario.config(state='readonly')
    entrySemestre.config(state=NORMAL)
    entryAlumno.config(state='readonly')
    entryMaestro.config(state='readonly')
    entryMateria.config(state='readonly')
    
    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
  
  def baja():
    option = messagebox.askyesno('Baja de grupo',f'Está a punto de de dar de baja al grupo con el ID {entryID.get()}\nDesea continuar?')
    if option:
      database.deleteGroup(entryID.get())
      cancelar()

  labelBusqueda.grid(row=0, column=1, sticky=E)
  entryBusqueda.grid(row=0, column=2, sticky=W+E)
  buttonBuscar.grid(row=0, column=3, sticky=W)

  labelID.grid(row=1, column=0)
  entryID.grid(row=1, column=1, sticky=W+E)
  labelNombre.grid(row=2, column=0)
  entryNombre.grid(row=2, column=1, sticky=W+E)
  labelFechaI.grid(row=3, column=0)
  entryFechaI.grid(row=3, column=1, sticky=W+E)
  labelFechaF.grid(row=4, column=0)
  entryFechaF.grid(row=4, column=1, sticky=W+E)
  labelCarrera.grid(row=5, column=0)
  entryCarrera.grid(row=5, column=1, sticky=W+E)
  labelMateria.grid(row=6, column=0)
  entryMateria.grid(row=6, column=1, sticky=W+E)
  
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
  
  buttonNuevo.grid(row=7, column=0)
  buttonGuardar.grid(row=7, column=1)
  buttonCancelar.grid(row=7, column=2)
  buttonEditar.grid(row=7, column=3)
  buttonBaja.grid(row=7, column=4)

  return frameGrupos
  #matertiasI, materiasN = database.materiaList()