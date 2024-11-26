import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime
import string
import database
import clases.salon as salon

def FrameSalon(nb):
  frameSalon = ttk.Frame(nb)
  frameSalon.grid_rowconfigure((0,1,2,3,4,5), weight=1)
  frameSalon.grid_columnconfigure((0,1,2,3,4), weight=1)
  
  edificios = list(string.ascii_uppercase)
  
  labelBusqueda = ttk.Label(frameSalon, text='Ingrese el ID de alumno:')
  labelID = ttk.Label(frameSalon, text='ID:')
  labelNombre = ttk.Label(frameSalon, text='Nombre salon:')
  labelEdificio = ttk.Label(frameSalon, text='Edificio:')
  
  entryBusqueda = ttk.Entry(frameSalon, width=20)
  entryID = ttk.Entry(frameSalon, state='readonly')
  entryNombre = ttk.Entry(frameSalon, state='readonly')
  entryEdificio = ttk.Combobox(frameSalon, values=edificios, state=DISABLED)
  
  buttonBuscar = ttk.Button(frameSalon, text='Buscar', command=lambda:buscar(entryBusqueda.get()))
  buttonNuevo = ttk.Button(frameSalon, text='Nuevo', command=lambda:nuevo())
  buttonGuardar = ttk.Button(frameSalon, text='Guardar', state="disabled", command=lambda:guardar())
  buttonCancelar = ttk.Button(frameSalon, text='Cancelar', state="disabled", command=lambda:cancelar())
  buttonEditar = ttk.Button(frameSalon, text='Editar', state="disabled", command=lambda:editar())
  buttonBaja = ttk.Button(frameSalon, text='Baja', state="disabled", command=lambda:baja())

  def buscar(id):
    classroom = database.searchClassroom(id)
    if classroom == None:
      messagebox.showwarning('Salon no encontrado', 'Parece que no tenemos ningun salon con ese ID')
    else:
      entryID.config(state=NORMAL)
      entryID.delete(0, tk.END)
      entryID.insert(0, classroom.getId())
      entryID.config(state='readonly')
      entryNombre.config(state=NORMAL)
      entryNombre.delete(0, tk.END)
      entryNombre.insert(0, classroom.getNombre())
      entryNombre.config(state='readonly')
      entryEdificio.config(state=NORMAL)
      entryEdificio.delete(0, tk.END)
      entryEdificio.insert(0, classroom.getEdificio())
      entryEdificio.config(state=DISABLED)
      
      buttonNuevo.config(state=NORMAL)
      buttonGuardar.config(state='disabled')
      buttonCancelar.config(state=NORMAL)
      buttonEditar.config(state=NORMAL)
      buttonBaja.config(state=NORMAL)
  
  def nuevo():
    entryID.config(state=NORMAL)
    entryID.delete(0, tk.END)
    entryID.insert(0, str(database.getCountClassroom()))
    entryID.config(state='readonly')
    entryNombre.config(state=NORMAL)
    entryNombre.delete(0, tk.END)
    entryEdificio.config(state=NORMAL)
    entryEdificio.set('')
    entryEdificio.config(state='readonly')
    
    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
  
  def guardar():
    if database.checkClassroom(entryID.get()):
      if all(field != '' for field in (entryNombre.get(), entryEdificio.get())):
        classroom = salon.Salon(entryID.get(), entryNombre.get(), entryEdificio.get())
        if database.updateClassroom(classroom):
          messagebox.showinfo('Salon actualizado', f'Los datos del salon con el ID: {classroom.getId()} han sido actualizados')
          cancelar()
        else:
          print('Error')
      else:
        messagebox.showwarning('Campos incompletos', 'Por favor llene todos los campos')
    else:
      if all(field != '' for field in (entryNombre.get(), entryEdificio.get())):
        classroom = salon.Salon(entryID.get(), entryNombre.get(), entryEdificio.get())
        if database.createClassroom(classroom):
          messagebox.showinfo('Salon registrado', f'Se ha registrado el salon con el ID: {classroom.getId()}')
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
    entryEdificio.config(state=NORMAL)
    entryEdificio.set('')
    entryEdificio.config(state=DISABLED)
    
    buttonNuevo.config(state=NORMAL)
    buttonGuardar.config(state='disabled')
    buttonCancelar.config(state='disabled')
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
  
  def editar():
    entryNombre.config(state=NORMAL)
    entryEdificio.config(state='readonly')
    
    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
  
  def baja():
    option = messagebox.askyesno('Baja de salon',f'Está a punto de de dar de baja el salon con el ID {entryID.get()}\nDesea continuar?')
    if option:
      database.deleteClassroom(entryID.get())
      cancelar()
  
  labelBusqueda.grid(row=0, column=1, sticky=E)
  entryBusqueda.grid(row=0, column=2, sticky=W+E)
  buttonBuscar.grid(row=0, column=3, sticky=W)
  
  labelID.grid(row=1, column=1)
  entryID.grid(row=1, column=2)
  entryNombre.grid(row=2, column=2)
  labelNombre.grid(row=2, column=1)
  entryEdificio.grid(row=3, column=2)
  labelEdificio.grid(row=3, column=1)
  
  buttonNuevo.grid(row=4, column=0)
  buttonGuardar.grid(row=4, column=1)
  buttonCancelar.grid(row=4, column=2)
  buttonEditar.grid(row=4, column=3)
  buttonBaja.grid(row=4, column=4)
  
  return frameSalon