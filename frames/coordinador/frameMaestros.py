import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime
import database
import clases.maestro as maestro

def FrameMaestros(nb):
  frameMaestros = ttk.Frame(nb)
  frameMaestros.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
  frameMaestros.grid_columnconfigure((0,1,2,3,4), weight=1)

  carrerasI, carrerasN = database.carreraList()

  labelBusqueda = ttk.Label(frameMaestros, text='Ingrese el ID de alumno:')
  labelID = ttk.Label(frameMaestros, text='ID:')
  labelNombre = ttk.Label(frameMaestros, text='Nombre:')
  labelPaterno = ttk.Label(frameMaestros, text='A. Paterno:')
  labelMaterno = ttk.Label(frameMaestros, text='A. Materno:')
  labelMail = ttk.Label(frameMaestros, text='Mail:')
  labelPassword = ttk.Label(frameMaestros, text='Password')
  labelFecha = ttk.Label(frameMaestros, text='Fecha Nacimiento:')
  labelEstudios = ttk.Label(frameMaestros, text='Grado de estudios:')
  labelCarrera = ttk.Label(frameMaestros, text='Carrera')

  entryBusqueda = ttk.Entry(frameMaestros, width=20)
  entryID = ttk.Entry(frameMaestros, state='readonly')
  entryNombre = ttk.Entry(frameMaestros, state='readonly')
  entryPaterno = ttk.Entry(frameMaestros, state='readonly')
  entryMaterno = ttk.Entry(frameMaestros, state='readonly')
  entryMail = ttk.Entry(frameMaestros, state='readonly')
  entryPassword =ttk.Entry(frameMaestros, state='readonly', show='*')
  entryFecha = DateEntry(frameMaestros, background='darkblue', foreground='white', borderwidth=2, state=DISABLED)
  entryEstudios = ttk.Entry(frameMaestros, state='readonly')
  entryCarrera = ttk.Combobox(frameMaestros, values=carrerasN, state=DISABLED)

  buttonBuscar = ttk.Button(frameMaestros, text='Buscar', command=lambda:buscar(entryBusqueda.get()))
  buttonNuevo = ttk.Button(frameMaestros, text='Nuevo', command=lambda:nuevo())
  buttonGuardar = ttk.Button(frameMaestros, text='Guardar', state="disabled", command=lambda:guardar())
  buttonCancelar = ttk.Button(frameMaestros, text='Cancelar', state="disabled", command=lambda:cancelar())
  buttonEditar = ttk.Button(frameMaestros, text='Editar', state="disabled", command=lambda:editar())
  buttonBaja = ttk.Button(frameMaestros, text='Baja', state="disabled", command=lambda:baja())

  def buscar(id):
    teacher = database.searchTeacher(id)
    if teacher == None:
      messagebox.showwarning('Maestro no encontrado', 'Parece que no tenemos ningun maestro con ese ID')
    else:
      entryID.config(state=NORMAL)
      entryID.delete(0, tk.END)
      entryID.insert(0, teacher.getId())
      entryID.config(state='readonly')
      entryNombre.config(state=NORMAL)
      entryNombre.delete(0, tk.END)
      entryNombre.insert(0, teacher.getNombre())
      entryNombre.config(state='readonly')
      entryPaterno.config(state=NORMAL)
      entryPaterno.delete(0, tk.END)
      entryPaterno.insert(0, teacher.getAPaterno())
      entryPaterno.config(state='readonly')
      entryMaterno.config(state=NORMAL)
      entryMaterno.delete(0, tk.END)
      entryMaterno.insert(0, teacher.getAMaterno())
      entryMaterno.config(state='readonly')
      entryMail.config(state=NORMAL)
      entryMail.delete(0, tk.END)
      entryMail.insert(0, teacher.getMail())
      entryMail.config(state='readonly')
      entryPassword.config(state=NORMAL)
      entryPassword.delete(0, tk.END)
      entryPassword.config(state='readonly')
      entryFecha.config(state=NORMAL)
      entryFecha.set_date(teacher.getFecha())
      entryFecha.config(state=DISABLED)
      entryEstudios.config(state=NORMAL)
      entryEstudios.delete(0, tk.END)
      entryEstudios.insert(0, teacher.getEstudios())
      entryEstudios.config(state=DISABLED)
      entryCarrera.config(state=NORMAL)
      entryCarrera.delete(0, tk.END)
      entryCarrera.set(teacher.getCarrera())
      entryCarrera.config(state=DISABLED)


      buttonNuevo.config(state=NORMAL)
      buttonGuardar.config(state='disabled')
      buttonCancelar.config(state=NORMAL)
      buttonEditar.config(state=NORMAL)
      buttonBaja.config(state=NORMAL)
  def nuevo():
    entryID.config(state=NORMAL)
    entryID.delete(0, tk.END)
    entryID.insert(0, str(database.getCountTeacher()))
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
    entryEstudios.config(state=NORMAL)
    entryEstudios.delete(0, tk.END)
    entryCarrera.config(state=NORMAL)
    entryCarrera.set(carrerasN[0])
    entryCarrera.config(state='readonly')

    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')

  def guardar():
    if database.checkTeacher(entryID.get()):
      if all (field != '' for field in (entryNombre.get(), entryPaterno.get(), entryMaterno.get(), entryMail.get(), entryEstudios.get(), entryFecha.get())):
        teacher = maestro.Maestro(entryID.get(), entryNombre.get(), entryPaterno.get(), entryMaterno.get(), entryFecha.get(), entryEstudios.get(), entryMail.get(), entryPassword.get(), entryCarrera.get())
        if database.updateTeacher(teacher, carrerasI[entryCarrera['values'].index(entryCarrera.get())]):
          messagebox.showinfo('Maestro actualizado', f'Los datos del Maestro con el ID: {teacher.getId()} han sido actualizados')
          cancelar()
        else:
          print('Error')
      else:
        messagebox.showwarning('Campos incompletos', 'Por favor llene todos los campos')
    else:
      if all (field != '' for field in (entryNombre.get(), entryPaterno.get(), entryMaterno.get(), entryMail.get(), entryEstudios.get(), entryFecha.get(), entryPassword.get())):
        teacher = maestro.Maestro(entryID.get(), entryNombre.get(), entryPaterno.get(), entryMaterno.get(), entryFecha.get(), entryEstudios.get(), entryMail.get(), entryPassword.get(), entryCarrera.get())
        if database.createTeacher(teacher, entryPassword.get(), carrerasI[entryCarrera['values'].index(entryCarrera.get())]):
          messagebox.showinfo('Usuario registrado', f'Se ha registrado a {teacher.getNombre()} con el ID: {teacher.getId()}')
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
    entryEstudios.config(state=NORMAL)
    entryEstudios.delete(0, tk.END)
    entryEstudios.config(state=DISABLED)
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
    entryEstudios.config(state=NORMAL)
    entryCarrera.config(state='readonly')

    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')

  def baja():
    option = messagebox.askyesno('Baja de maestro',f'Está a punto de de dar de baja al maestro con el ID {entryID.get()}\nDesea continuar?')
    if option:
      database.deleteTeacher(entryID.get())
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
  labelEstudios.grid(row=3, column=2)
  entryEstudios.grid(row=3, column=3, sticky=W+E)
  labelCarrera.grid(row=4, column=2)
  entryCarrera.grid(row=4, column=3, sticky=W+E)

  buttonNuevo.grid(row=6, column=0)
  buttonGuardar.grid(row=6, column=1)
  buttonCancelar.grid(row=6, column=2)
  buttonEditar.grid(row=6, column=3)
  buttonBaja.grid(row=6, column=4)

  return frameMaestros