import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database
import administrador

def FrameCoordinador(nb):
  frameCoordinadores = ttk.Frame(nb)
  frameCoordinadores.grid_rowconfigure((0,1,2,3,4,5), weight=1)
  frameCoordinadores.grid_columnconfigure((0,1,2,3,4), weight=1)
  labelBusqueda1 = ttk.Label(frameCoordinadores, text='ID Coordinador:')
  labelID1 = ttk.Label(frameCoordinadores, text='ID:')
  labelNombre1 = ttk.Label(frameCoordinadores, text='Nombre:')
  labelPaterno1 = ttk.Label(frameCoordinadores, text='A. Paterno:')
  labelMaterno1 = ttk.Label(frameCoordinadores, text='A. Materno:')
  labelMail1 = ttk.Label(frameCoordinadores, text='Mail:')
  labelUsuario1 = ttk.Label(frameCoordinadores, text='Usuario:')
  labelPassword1 = ttk.Label(frameCoordinadores, text='Password:')

  entryBusqueda1 = ttk.Entry(frameCoordinadores, width=20)
  entryID1 = ttk.Entry(frameCoordinadores, state='readonly')
  entryNombre1 = ttk.Entry(frameCoordinadores, state='readonly')
  entryPaterno1 = ttk.Entry(frameCoordinadores, state='readonly')
  entryMaterno1 = ttk.Entry(frameCoordinadores, state='readonly')
  entryMail1 = ttk.Entry(frameCoordinadores, state='readonly')
  entryUsuario1 = ttk.Entry(frameCoordinadores, state='readonly')
  entryPassword1 = ttk.Entry(frameCoordinadores, show='*', state='readonly')

  buttonBuscar1 = ttk.Button(frameCoordinadores, text='Buscar', command=lambda:buscar(entryBusqueda1.get()))
  buttonNuevo1 = ttk.Button(frameCoordinadores, text='Nuevo')
  buttonGuardar1 = ttk.Button(frameCoordinadores, text='Guardar')
  buttonCancelar1 = ttk.Button(frameCoordinadores, text='Cancelar')
  buttonEditar1 = ttk.Button(frameCoordinadores, text='Editar')
  buttonBaja1 = ttk.Button(frameCoordinadores, text='Baja')

  #-Commands-
  def buscar(id):
    admin = database.searchAdmin(id)
    if admin == None:
      messagebox.showwarning('Usuario no encontrado', 'Parece que no tenemos ningun coordinador con ese ID')
    else:
      entryID1.config(state=NORMAL)
      entryID1.delete(0, tk.END)
      entryID1.insert(0, admin.getId())
      entryID1.config(state='readonly')
      entryNombre1.config(state=NORMAL)
      entryNombre1.delete(0, tk.END)
      entryNombre1.insert(0, admin.getNombre())
      entryNombre1.config(state='readonly')
      entryPaterno1.config(state=NORMAL)
      entryPaterno1.delete(0, tk.END)
      entryPaterno1.insert(0, admin.getAPaterno())
      entryPaterno1.config(state='readonly')
      entryMaterno1.config(state=NORMAL)
      entryMaterno1.delete(0, tk.END)
      entryMaterno1.insert(0, admin.getAMaterno())
      entryMaterno1.config(state='readonly')
      entryMail1.config(state=NORMAL)
      entryMail1.delete(0, tk.END)
      entryMail1.insert(0, admin.getMail())
      entryMail1.config(state='readonly')
      entryUsuario1.config(state=NORMAL)
      entryUsuario1.delete(0, tk.END)
      entryUsuario1.insert(0, admin.getUsuario())
      entryUsuario1.config(state='readonly')
      entryPassword1.config(state=NORMAL)
      entryPassword1.delete(0, tk.END)
      entryPassword1.config(state='readonly')

  labelBusqueda1.grid(row=0, column=1, sticky=E)
  entryBusqueda1.grid(row=0, column=2, sticky=W+E)
  buttonBuscar1.grid(row=0, column=3, sticky=W)

  labelID1.grid(row=1, column=0)
  entryID1.grid(row=1, column=1, sticky=W+E)
  labelNombre1.grid(row=2, column=0)
  entryNombre1.grid(row=2, column=1, sticky=W+E)
  labelPaterno1.grid(row=3, column=0)
  entryPaterno1.grid(row=3, column=1, sticky=W+E)
  labelMaterno1.grid(row=4, column=0)
  entryMaterno1.grid(row=4, column=1, sticky=W+E)

  labelMail1.grid(row=1, column=2)
  entryMail1.grid(row=1, column=3, sticky=W+E)
  labelUsuario1.grid(row=2, column=2)
  entryUsuario1.grid(row=2, column=3, sticky=W+E)
  labelPassword1.grid(row=3, column=2)
  entryPassword1.grid(row=3, column=3, sticky=W+E)

  buttonNuevo1.grid(row=5, column=0)
  buttonGuardar1.grid(row=5, column=1)
  buttonCancelar1.grid(row=5, column=2)
  buttonEditar1.grid(row=5, column=3)
  buttonBaja1.grid(row=5, column=4)

  return frameCoordinadores