import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime
import database
import clases.alumno as alumno

def FrameAlumnos(nb):
  frameAlumnos = ttk.Frame(nb)
  frameAlumnos.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
  frameAlumnos.grid_columnconfigure((0,1,2,3,4), weight=1)
  carrerasI, carrerasN = database.carreraList()
  estados = ['Regular', 'Irregular', 'Baja temporal']

  labelBusqueda = ttk.Label(frameAlumnos, text='Ingrese el ID de alumno:')
  labelID = ttk.Label(frameAlumnos, text='ID:')
  labelNombre = ttk.Label(frameAlumnos, text='Nombre:')
  labelPaterno = ttk.Label(frameAlumnos, text='A. Paterno:')
  labelMaterno = ttk.Label(frameAlumnos, text='A. Materno:')
  labelMail = ttk.Label(frameAlumnos, text='Mail:')
  labelPassword = ttk.Label(frameAlumnos, text='Password')
  labelFecha = ttk.Label(frameAlumnos, text='Fecha Nacimiento:')
  labelEstado = ttk.Label(frameAlumnos, text='Estado:')
  labelCarrera = ttk.Label(frameAlumnos, text='Carrera')
  
  entryBusqueda = ttk.Entry(frameAlumnos, width=20)
  entryID = ttk.Entry(frameAlumnos, state='readonly')
  entryNombre = ttk.Entry(frameAlumnos, state='readonly')
  entryPaterno = ttk.Entry(frameAlumnos, state='readonly')
  entryMaterno = ttk.Entry(frameAlumnos, state='readonly')
  entryMail = ttk.Entry(frameAlumnos, state='readonly')
  entryPassword =ttk.Entry(frameAlumnos, state='readonly', show='*')
  entryFecha = DateEntry(frameAlumnos, background='darkblue', foreground='white', borderwidth=2, state=DISABLED)
  entryEstado = ttk.Combobox(frameAlumnos, values=estados, state=DISABLED)
  entryCarrera = ttk.Combobox(frameAlumnos, values=carrerasN, state=DISABLED)

  buttonBuscar = ttk.Button(frameAlumnos, text='Buscar', command=lambda:buscar(entryBusqueda.get()))
  buttonNuevo = ttk.Button(frameAlumnos, text='Nuevo', command=lambda:nuevo())
  buttonGuardar = ttk.Button(frameAlumnos, text='Guardar', state="disabled", command=lambda:guardar())
  buttonCancelar = ttk.Button(frameAlumnos, text='Cancelar', state="disabled", command=lambda:cancelar())
  buttonEditar = ttk.Button(frameAlumnos, text='Editar', state="disabled", command=lambda:editar())
  buttonBaja = ttk.Button(frameAlumnos, text='Baja', state="disabled", command=lambda:baja())

  #-Commands-
  def buscar(id):
    student = database.searchStudent(id)
    if student == None:
      messagebox.showwarning('Alumno no encontrado', 'Parece que no tenemos ningun alumno con ese ID')
    else:
      entryID.config(state=NORMAL)
      entryID.delete(0, tk.END)
      entryID.insert(0, student.getId())
      entryID.config(state='readonly')
      entryNombre.config(state=NORMAL)
      entryNombre.delete(0, tk.END)
      entryNombre.insert(0, student.getNombre())
      entryNombre.config(state='readonly')
      entryPaterno.config(state=NORMAL)
      entryPaterno.delete(0, tk.END)
      entryPaterno.insert(0, student.getAPaterno())
      entryPaterno.config(state='readonly')
      entryMaterno.config(state=NORMAL)
      entryMaterno.delete(0, tk.END)
      entryMaterno.insert(0, student.getAMaterno())
      entryMaterno.config(state='readonly')
      entryMail.config(state=NORMAL)
      entryMail.delete(0, tk.END)
      entryMail.insert(0, student.getMail())
      entryMail.config(state='readonly')
      entryPassword.config(state=NORMAL)
      entryPassword.delete(0, tk.END)
      entryPassword.config(state='readonly')
      entryFecha.config(state=NORMAL)
      entryFecha.set_date(student.getFechaNacimiento())
      entryFecha.config(state=DISABLED)
      entryEstado.config(state=NORMAL)
      entryEstado.delete(0, tk.END)
      entryEstado.set(student.getEstado())
      entryEstado.config(state=DISABLED)
      entryCarrera.config(state=NORMAL)
      entryCarrera.delete(0, tk.END)
      entryCarrera.set(student.getCarrera())
      entryCarrera.config(state=DISABLED)


      buttonNuevo.config(state=NORMAL)
      buttonGuardar.config(state='disabled')
      buttonCancelar.config(state=NORMAL)
      buttonEditar.config(state=NORMAL)
      buttonBaja.config(state=NORMAL)

  def nuevo():
    entryID.config(state=NORMAL)
    entryID.delete(0, tk.END)
    entryID.insert(0, str(database.getCountStudent()))
    entryID.config(state='readonly')
    entryNombre.config(state=NORMAL)
    entryNombre.delete(0, tk.END)
    entryPaterno.config(state=NORMAL)
    entryPaterno.delete(0, tk.END)
    entryMaterno.config(state=NORMAL)
    entryMaterno.delete(0, tk.END)
    entryMail.config(state=NORMAL)
    entryMail.delete(0, tk.END)
    entryPassword.config(state=NORMAL)
    entryPassword.delete(0, tk.END)
    entryFecha.config(state=NORMAL)
    entryFecha.set_date(datetime(2000, 1, 1))
    entryFecha.config(state='readonly')
    entryEstado.config(state=NORMAL)
    entryEstado.set(estados[0])
    entryEstado.config(state='readonly')
    entryCarrera.config(state=NORMAL)
    entryCarrera.set(carrerasN[0])
    entryCarrera.config(state='readonly')

    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')

  def guardar():
    if database.checkStudent(entryID.get()):
      if all (field != '' for field in (entryNombre.get(), entryPaterno.get(), entryMaterno.get(), entryMail.get(), entryEstado.get(), entryFecha.get())):
        student = alumno.Alumno(entryID.get(), entryNombre.get(), entryPaterno.get(), entryMaterno.get(), entryMail.get(), entryEstado.get(), entryFecha.get(), entryCarrera.get(), [])
        if database.updateStudent(student, carrerasI[entryCarrera['values'].index(entryCarrera.get())]):
          messagebox.showinfo('Alumno actualizado', f'Los datos del alumno con el ID: {student.getId()} han sido actualizados')
          cancelar()
        else:
          print('Error')
      else:
        messagebox.showwarning('Campos incompletos', 'Por favor llene todos los campos')
    else:
      if all (field != '' for field in (entryNombre.get(), entryPaterno.get(), entryMaterno.get(), entryMail.get(), entryEstado.get(), entryFecha.get(), entryPassword.get())):
        student = alumno.Alumno(entryID.get(), entryNombre.get(), entryPaterno.get(), entryMaterno.get(), entryMail.get(), entryEstado.get(), entryFecha.get(), entryCarrera.get(), [])
        if database.createStudent(student, entryPassword.get(), carrerasI[entryCarrera['values'].index(entryCarrera.get())]):
          messagebox.showinfo('Usuario registrado', f'Se ha registrado a {student.getNombre()} con el ID: {student.getId()}')
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
    entryNombre.config(state='readonly')
    entryPaterno.config(state=NORMAL)
    entryPaterno.delete(0, tk.END)
    entryPaterno.config(state='readonly')
    entryMaterno.config(state=NORMAL)
    entryMaterno.delete(0, tk.END)
    entryMaterno.config(state='readonly')
    entryMail.config(state=NORMAL)
    entryMail.delete(0, tk.END)
    entryMail.config(state='readonly')
    entryPassword.config(state=NORMAL)
    entryPassword.delete(0, tk.END)
    entryPassword.config(state='readonly')
    entryFecha.config(state=NORMAL)
    entryFecha.set_date(datetime(2000, 1, 1))
    entryFecha.config(state=DISABLED)
    entryEstado.config(state=NORMAL)
    entryEstado.set(estados[0])
    entryEstado.config(state=DISABLED)
    entryCarrera.config(state=NORMAL)
    entryCarrera.set(carrerasN[0])
    entryCarrera.config(state=DISABLED)

    buttonNuevo.config(state=NORMAL)
    buttonGuardar.config(state='disabled')
    buttonCancelar.config(state='disabled')
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')

  def editar():
    entryNombre.config(state=NORMAL)
    entryPaterno.config(state=NORMAL)
    entryMaterno.config(state=NORMAL)
    entryMail.config(state=NORMAL)
    labelPassword.config(state=DISABLED)
    entryFecha.config(state='readonly')
    entryEstado.config(state='readonly')
    entryCarrera.config(state='readonly')

    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')

  def baja():
    option = messagebox.askyesno('Baja de alumno',f'Está a punto de de dar de baja al alumno con el ID {entryID.get()}\nDesea continuar?')
    if option:
      database.deleteStudent(entryID.get())
      cancelar()
      
  labelBusqueda.grid(row=0, column=1, sticky=E)
  entryBusqueda.grid(row=0, column=2, sticky=W+E)
  buttonBuscar.grid(row=0, column=3, sticky=W)

  labelID.grid(row=1, column=0)
  entryID.grid(row=1, column=1, sticky=W+E)
  labelNombre.grid(row=2, column=0)
  entryNombre.grid(row=2, column=1, sticky=W+E)
  labelPaterno.grid(row=3, column=0)
  entryPaterno.grid(row=3, column=1, sticky=W+E)
  labelMaterno.grid(row=4, column=0)
  entryMaterno.grid(row=4, column=1, sticky=W+E)
  labelMail.grid(row=5, column=0)
  entryMail.grid(row=5, column=1, sticky=W+E)

  labelPassword.grid(row=1, column=2)
  entryPassword.grid(row=1, column=3, sticky=W+E)
  labelFecha.grid(row=2, column=2)
  entryFecha.grid(row=2, column=3, sticky=W+E)
  labelEstado.grid(row=3, column=2)
  entryEstado.grid(row=3, column=3, sticky=W+E)
  labelCarrera.grid(row=4, column=2)
  entryCarrera.grid(row=4, column=3, sticky=W+E)

  buttonNuevo.grid(row=6, column=0)
  buttonGuardar.grid(row=6, column=1)
  buttonCancelar.grid(row=6, column=2)
  buttonEditar.grid(row=6, column=3)
  buttonBaja.grid(row=6, column=4)

  return frameAlumnos