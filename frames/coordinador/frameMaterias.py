import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database
import clases.materia as materia

def FrameMaterias(nb):
  frameMaterias = ttk.Frame(nb)
  frameMaterias.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
  frameMaterias.grid_columnconfigure((0,1,2,3,4), weight=1)

  carrerasI, carrerasN = database.carreraList()

  labelBusqueda = ttk.Label(frameMaterias, text='Ingrese el ID de materia:')
  labelID = ttk.Label(frameMaterias, text='ID:')
  labelAsignatura = ttk.Label(frameMaterias, text='Asignatura:')
  labelCreditos = ttk.Label(frameMaterias, text='Creditos:')
  labelSemestre = ttk.Label(frameMaterias, text='Semestre:')
  labelCarrera = ttk.Label(frameMaterias, text='Carrera:')
  
  entryBusqueda = ttk.Entry(frameMaterias, width=20)
  entryID = ttk.Entry(frameMaterias, state='readonly')
  entryAsignatura = ttk.Entry(frameMaterias, state='readonly')
  entryCreditos = ttk.Entry(frameMaterias, state='readonly')
  entrySemestre = ttk.Entry(frameMaterias, state='readonly')
  entryCarrera = ttk.Combobox(frameMaterias, values=carrerasN, state=DISABLED)

  buttonBuscar = ttk.Button(frameMaterias, text='Buscar', command=lambda:buscar(entryBusqueda.get()))
  buttonNuevo = ttk.Button(frameMaterias, text='Nuevo', command=lambda:nuevo())
  buttonGuardar = ttk.Button(frameMaterias, text='Guardar', state="disabled", command=lambda:guardar())
  buttonCancelar = ttk.Button(frameMaterias, text='Cancelar', state="disabled", command=lambda:cancelar())
  buttonEditar = ttk.Button(frameMaterias, text='Editar', state="disabled", command=lambda:editar())
  
  def buscar(id):
    clas = database.searchClass(id)
    if clas == None:
      messagebox.showwarning('Materia no encontrado', 'Parece que no tenemos ninguna materia con ese ID')
    else:
      entryID.config(state=NORMAL)
      entryID.delete(0, tk.END)
      entryID.insert(0, clas.getId())
      entryID.config(state='readonly')
      entryAsignatura.config(state=NORMAL)
      entryAsignatura.delete(0, tk.END)
      entryAsignatura.insert(0, clas.getAsignatura())
      entryAsignatura.config(state='readonly')
      entryCreditos.config(state=NORMAL)
      entryCreditos.delete(0, tk.END)
      entryCreditos.insert(0, clas.getCreditos())
      entryCreditos.config(state='readonly')
      entrySemestre.config(state=NORMAL)
      entrySemestre.delete(0, tk.END)
      entrySemestre.insert(0, clas.getSemestres())
      entrySemestre.config(state='readonly')
      entryCarrera.config(state=NORMAL)
      entryCarrera.delete(0, tk.END)
      entryCarrera.set(clas.getCarrera())
      entryCarrera.config(state=DISABLED)
      
      buttonNuevo.config(state=NORMAL)
      buttonGuardar.config(state='disabled')
      buttonCancelar.config(state=NORMAL)
      buttonEditar.config(state=NORMAL)

  def nuevo():
    entryID.config(state=NORMAL)
    entryID.delete(0, tk.END)
    entryID.insert(0, str(database.getCountMaterias()))
    entryID.config(state='readonly')
    entryAsignatura.config(state=NORMAL)
    entryAsignatura.delete(0, tk.END)
    entryCreditos.config(state=NORMAL)
    entryCreditos.delete(0, tk.END)
    entrySemestre.config(state=NORMAL)
    entrySemestre.delete(0, tk.END)
    entryCarrera.config(state=NORMAL)
    entryCarrera.set(carrerasN[0])
    entryCarrera.config(state='readonly')

    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
  
  def guardar():
    if database.checkClass(entryID.get()):
      if all (field != '' for field in (entryAsignatura.get(), entryCreditos.get(), entrySemestre.get(), entryCarrera.get())):
        clas = materia.materia(entryID.get(), entryCarrera.get(), entryAsignatura.get(), entryCreditos.get(), entrySemestre.get())
        if database.updateClass(clas, carrerasI[entryCarrera['values'].index(entryCarrera.get())]):
          messagebox.showinfo('Materia actualizada', f'Los datos de la materia con el ID: {clas.getId()} han sido actualizados')
          cancelar()
        else:
          print('Error')
      else:
        messagebox.showwarning('Campos incompletos', 'Por favor llene todos los campos')
    else:
      if all (field != '' for field in (entryAsignatura.get(), entryCreditos.get(), entrySemestre.get(), entryCarrera.get())):
        clas = materia.Materia(entryID.get(), entryCarrera.get(), entryAsignatura.get(), entryCreditos.get(), entrySemestre.get())
        if database.createClass(clas, carrerasI[entryCarrera['values'].index(entryCarrera.get())]):
          messagebox.showinfo('Materia registrada', f'Se ha registrado {clas.getAsignatura()} con el ID: {clas.getId()}')
          cancelar()
        else:
          print('Error')
      else:
        messagebox.showwarning('Campos incompletos', 'Por favor llene todos los campos')

  
  def cancelar():
    entryID.config(state=NORMAL)
    entryID.delete(0, tk.END)
    entryID.config(state='readonly')
    entryAsignatura.config(state=NORMAL)
    entryAsignatura.delete(0, tk.END)
    entryAsignatura.config(state='readonly')
    entryCreditos.config(state=NORMAL)
    entryCreditos.delete(0, tk.END)
    entryCreditos.config(state='readonly')
    entrySemestre.config(state=NORMAL)
    entrySemestre.delete(0, tk.END)
    entrySemestre.config(state='readonly')
    entryCarrera.config(state=NORMAL)
    entryCarrera.set(carrerasN[0])
    entryCarrera.config(state=DISABLED)

    buttonNuevo.config(state=NORMAL)
    buttonGuardar.config(state='disabled')
    buttonCancelar.config(state='disabled')
    buttonEditar.config(state='disabled')
  
  labelBusqueda.grid(row=0, column=1, sticky=E)
  entryBusqueda.grid(row=0, column=2, sticky=W+E)
  buttonBuscar.grid(row=0, column=3, sticky=W)

  labelID.grid(row=1, column=0)
  entryID.grid(row=1, column=1, sticky=W+E)
  labelAsignatura.grid(row=2, column=0)
  entryAsignatura.grid(row=2, column=1, sticky=W+E)
  labelCreditos.grid(row=3, column=0)
  entryCreditos.grid(row=3, column=1, sticky=W+E)
  labelSemestre.grid(row=4, column=0)
  entrySemestre.grid(row=4, column=1, sticky=W+E)

  labelCarrera.grid(row=3, column=2)
  entryCarrera.grid(row=3, column=3, sticky=W+E)

  buttonNuevo.grid(row=6, column=0)
  buttonGuardar.grid(row=6, column=1)
  buttonCancelar.grid(row=6, column=2)
  buttonEditar.grid(row=6, column=3)
  
  return frameMaterias