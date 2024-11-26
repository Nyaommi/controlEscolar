import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
import database
import clases.carrera as carrera

def FrameCarrera(nb):
  frameCarrera = ttk.Frame(nb)
  frameCarrera.grid_rowconfigure((0,1,2,3,4,5), weight=1)
  frameCarrera.grid_columnconfigure((0,1,2,3,4), weight=1)
  
  labelBusqueda = ttk.Label(frameCarrera, text='Ingrese el ID de la carrera:')
  labelID = ttk.Label(frameCarrera, text='ID:')
  labelNombre = ttk.Label(frameCarrera, text='Nombre:')
  labelSemestres = ttk.Label(frameCarrera, text='Semestres:')
  
  entryBusqueda = ttk.Entry(frameCarrera, width=20)
  entryID = ttk.Entry(frameCarrera, state='readonly')
  entryNombre = ttk.Entry(frameCarrera, state='readonly')
  entrySemestres = ttk.Spinbox(frameCarrera, state=DISABLED, from_=6, to=8)
  
  buttonBuscar = ttk.Button(frameCarrera, text='Buscar', command=lambda:buscar(entryBusqueda.get()))
  buttonNuevo = ttk.Button(frameCarrera, text='Nuevo', command=lambda:nuevo())
  buttonGuardar = ttk.Button(frameCarrera, text='Guardar', state="disabled", command=lambda:guardar())
  buttonCancelar = ttk.Button(frameCarrera, text='Cancelar', state="disabled", command=lambda:cancelar())
  buttonEditar = ttk.Button(frameCarrera, text='Editar', state="disabled", command=lambda:editar())
  buttonBaja = ttk.Button(frameCarrera, text='Baja', state="disabled", command=lambda:baja())
  
  def buscar(id):
    carrer = database.searchCarrer(id)
    if carrer == None:
      messagebox.showwarning('Carrera no encontrada', 'Parece que no tenemos ninguna carrera con ese ID')
    else:
      entryID.config(state=NORMAL)
      entryID.delete(0, tk.END)
      entryID.insert(0, carrer.getId())
      entryID.config(state='readonly')
      entryNombre.config(state=NORMAL)
      entryNombre.delete(0, tk.END)
      entryNombre.insert(0, carrer.getNombre())
      entryNombre.config(state='readonly')
      entrySemestres.config(state=NORMAL)
      entrySemestres.delete(0, tk.END)
      entrySemestres.set(carrer.getSemestres())
      entrySemestres.config(state=DISABLED)
      
      buttonNuevo.config(state=NORMAL)
      buttonGuardar.config(state='disabled')
      buttonCancelar.config(state=NORMAL)
      buttonEditar.config(state=NORMAL)
      buttonBaja.config(state=NORMAL)
  
  def nuevo():
    entryID.config(state=NORMAL)
    entryID.delete(0, tk.END)
    entryID.insert(0, str(database.getCountCarrer()))
    entryID.config(state='readonly')
    entryNombre.config(state=NORMAL)
    entryNombre.delete(0, tk.END)
    entrySemestres.config(state=NORMAL)
    entrySemestres.set('6')
    entrySemestres.config(state='readonly')
    
    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
  
  def guardar():
    if database.checkCarrer(entryID.get()):
      if all(field != '' for field in (entryNombre.get(), entrySemestres.get())):
        carrer = carrera.Carrera(entryID.get(), entryNombre.get(), entrySemestres.get())
        if database.updateCarrer(carrer):
          messagebox.showinfo('Carrera actualizada', f'Los datos de la carrrea con el ID: {carrer.getId()} han sido actualizados')
          cancelar()
        else:
          print('Error')
      else:
        messagebox.showwarning('Campos incompletos', 'Por favor llene todos los campos')
    else:
      if all(field != '' for field in (entryNombre.get(), entrySemestres.get())):
        carrer = carrera.Carrera(entryID.get(), entryNombre.get(), entrySemestres.get())
        if database.createCarrer(carrer):
          messagebox.showinfo('Carrera registrado', f'Se ha registrado la carrera con el ID: {carrer.getId()}')
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
    entrySemestres.config(state=NORMAL)
    entrySemestres.set('')
    entrySemestres.config(state=DISABLED)
    
    buttonNuevo.config(state=NORMAL)
    buttonGuardar.config(state='disabled')
    buttonCancelar.config(state='disabled')
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
  
  def editar():
    entryNombre.config(state=NORMAL)
    entrySemestres.config(state='readonly')
    
    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
  
  def baja():
    option = messagebox.askyesno('Baja de carrera',f'Está a punto de de dar de baja la carrera con el ID {entryID.get()}\nDesea continuar?')
    if option:
      database.deleteCarrer(entryID.get())
      cancelar()
  
  labelBusqueda.grid(row=0, column=1, sticky=E)
  entryBusqueda.grid(row=0, column=2, sticky=W+E)
  buttonBuscar.grid(row=0, column=3, sticky=W)
  
  labelID.grid(row=1, column=1)
  entryID.grid(row=1, column=2)
  entryNombre.grid(row=2, column=2)
  labelNombre.grid(row=2, column=1)
  entrySemestres.grid(row=3, column=2)
  labelSemestres.grid(row=3, column=1)
  
  buttonNuevo.grid(row=4, column=0)
  buttonGuardar.grid(row=4, column=1)
  buttonCancelar.grid(row=4, column=2)
  buttonEditar.grid(row=4, column=3)
  buttonBaja.grid(row=4, column=4)
  
  return frameCarrera
