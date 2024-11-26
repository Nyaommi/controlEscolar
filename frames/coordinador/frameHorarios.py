import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime
import database
import clases.horario as horario

def FrameHorarios(nb):
  frameHorarios = ttk.Frame(nb)
  frameHorarios.grid_rowconfigure((0,1,2,3,4,5), weight=1)
  frameHorarios.grid_columnconfigure((0,1,2,3,4), weight=1)
  turnos = ['Matutino', 'Vespertino']
  dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']  
  horas = [
        "7:00 - 8:50", "9:00 - 10:50", "11:00 - 12:50",
        "13:00 - 14:50", "15:00 - 16:50", "17:00 - 18:50", "19:00 - 20:50"
    ]
  labelBusqueda = ttk.Label(frameHorarios, text='Ingrese el ID de alumno:')
  labelID = ttk.Label(frameHorarios, text='ID:')
  labelDia = ttk.Label(frameHorarios, text='Hora:')
  labelTurno = ttk.Label(frameHorarios, text='Turno:')
  labelHora = ttk.Label(frameHorarios, text='Hora:')
  
  entryBusqueda = ttk.Entry(frameHorarios, width=20)
  entryID = ttk.Entry(frameHorarios, state='readonly')
  entryDia = ttk.Combobox(frameHorarios, values=dias, state=DISABLED)
  entryTurno = ttk.Combobox(frameHorarios, values=turnos, state=DISABLED)
  entryHora = ttk.Combobox(frameHorarios, values=horas, state=DISABLED)
  
  buttonBuscar = ttk.Button(frameHorarios, text='Buscar', command=lambda:buscar(entryBusqueda.get()))
  buttonNuevo = ttk.Button(frameHorarios, text='Nuevo', command=lambda:nuevo())
  buttonGuardar = ttk.Button(frameHorarios, text='Guardar', state="disabled", command=lambda:guardar())
  buttonCancelar = ttk.Button(frameHorarios, text='Cancelar', state="disabled", command=lambda:cancelar())
  buttonEditar = ttk.Button(frameHorarios, text='Editar', state="disabled", command=lambda:editar())
  buttonBaja = ttk.Button(frameHorarios, text='Baja', state="disabled", command=lambda:baja())

  #-Commands-
  def buscar(id):
    schedule = database.searchSchedule(id)
    if schedule == None:
      messagebox.showwarning('Alumno no encontrado', 'Parece que no tenemos ningun alumno con ese ID')
    else:
      entryID.config(state=NORMAL)
      entryID.delete(0, tk.END)
      entryID.insert(0, schedule.getId())
      entryID.config(state='readonly')
      entryDia.config(state=NORMAL)
      entryDia.set(schedule.getDia())
      entryDia.config(state=DISABLED)
      entryTurno.config(state=NORMAL)
      entryTurno.set(schedule.getTurno())
      entryTurno.config(state=DISABLED)
      entryHora.config(state=NORMAL)
      entryHora.set(schedule.getHora())
      entryHora.config(state=DISABLED)
      
      buttonNuevo.config(state=NORMAL)
      buttonGuardar.config(state='disabled')
      buttonCancelar.config(state=NORMAL)
      buttonEditar.config(state=NORMAL)
      buttonBaja.config(state=NORMAL)
  
  def nuevo():
    entryID.config(state=NORMAL)
    entryID.delete(0, tk.END)
    entryID.insert(0, str(database.getCountSchedule()))
    entryID.config(state='readonly')
    entryDia.config(state='readonly')
    entryDia.set('')
    entryTurno.config(state='readonly')
    entryTurno.set('')
    entryHora.config(state='readonly')
    entryHora.set('')
    
    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
  
  def guardar():
    if database.checkSchedule(entryID.get()):
      if all(field != '' for field in (entryDia.get(), entryTurno.get(), entryHora.get())):
        schedule = horario.Horario(entryID.get(),entryTurno.get(), entryHora.get(), entryDia.get())
        if database.updateSchedule(schedule):
          messagebox.showinfo('Horario actualizado', f'Los datos del horario con el ID: {schedule.getId()} han sido actualizados')
          cancelar()
        else:
          print('Error')
      else:
        messagebox.showwarning('Campos incompletos', 'Por favor llene todos los campos')
    else:
      if all(field != '' for field in (entryDia.get(), entryTurno.get(), entryHora.get())):
        schedule = horario.Horario(entryID.get(),entryTurno.get(), entryHora.get(), entryDia.get())
        if database.createSchedule(schedule):
          messagebox.showinfo('Horario registrado', f'Se ha registrado el horario con el ID: {schedule.getId()}')
          cancelar()
        else:
          print('Error')    
      else:
        messagebox.showwarning('Campos incompletos', 'Por favor llene todos los campos')
  
  def cancelar():
    entryID.config(state=NORMAL)
    entryID.delete(0, tk.END)
    entryID.config(state='readonly')
    entryDia.set('')
    entryDia.config(state=DISABLED)
    entryTurno.set('')
    entryTurno.config(state=DISABLED)
    entryHora.set('')
    entryHora.config(state=DISABLED)
    
    buttonNuevo.config(state=NORMAL)
    buttonGuardar.config(state='disabled')
    buttonCancelar.config(state='disabled')
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
  
  def editar():
    entryDia.config(state='readonly')
    entryTurno.config(state='readonly')
    entryHora.config(state='readonly')
    
    buttonNuevo.config(state='disabled')
    buttonGuardar.config(state=NORMAL)
    buttonCancelar.config(state=NORMAL)
    buttonEditar.config(state='disabled')
    buttonBaja.config(state='disabled')
  
  def baja():
    option = messagebox.askyesno('Baja de horario',f'Está a punto de de dar de baja el horario con el ID {entryID.get()}\nDesea continuar?')
    if option:
      database.deleteSchedule(entryID.get())
      cancelar()
  
  labelBusqueda.grid(row=0, column=1, sticky=E)
  entryBusqueda.grid(row=0, column=2, sticky=W+E)
  buttonBuscar.grid(row=0, column=3, sticky=W)
  
  labelID.grid(row=1, column=1)
  entryID.grid(row=1, column=2)
  entryDia.grid(row=2, column=2)
  labelDia.grid(row=2, column=1)
  entryTurno.grid(row=3, column=2)
  labelTurno.grid(row=3, column=1)
  labelHora.grid(row=4, column=1)
  entryHora.grid(row=4, column=2)
  
  buttonNuevo.grid(row=5, column=0)
  buttonGuardar.grid(row=5, column=1)
  buttonCancelar.grid(row=5, column=2)
  buttonEditar.grid(row=5, column=3)
  buttonBaja.grid(row=5, column=4)
  
  return frameHorarios