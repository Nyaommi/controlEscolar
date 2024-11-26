import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import database
import clases.administrador as administrador
import frames.coordinador.frameCoordinadores as FCC
import frames.coordinador.frameAlumnos as FCA
import frames.coordinador.frameMaestros as FCM
import frames.coordinador.frameMaterias as FCMa
import frames.coordinador.frameGrupos as FCG
import frames.coordinador.frameHorarios as FCH
import frames.coordinador.frameSalon as FCS
import frames.coordinador.frameCarrera as FCCa
import frames.coordinador.framePlaneacion as FCP

import frames.alumnos.frameDatos as FAD
import frames.alumnos.frameAgenda as FAA
import frames.alumnos.frameHorario as FAH

import frames.maestros.frameDatos as FMD
import frames.maestros.frameMaterias as FMM
import frames.maestros.frameHorario as FMH

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Login')
    self.geometry('500x350')
    self.currentUser = None
    #self.menuMaestro('joseC@udeg.com')
    self.menuAdmin()

  def menuLogin(self):
    for widget in self.winfo_children():
      widget.destroy()
    lbTittle = ttk.Label(self, text='Control Escolar')

    self.grid_rowconfigure((0,1,2,3, 4), weight=1)
    self.grid_columnconfigure((0,1,2), weight=1)

    lbUser = ttk.Label(self, text='Email:')
    lbPassword = ttk.Label(self, text='Password:')

    entryUser = ttk.Entry(self)
    entryPassword = ttk.Entry(self, show='*')

    lbTittle.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    lbUser.grid(row=1, column=1, sticky=W)
    lbPassword.grid(row=2, column=1, sticky=W)

    entryUser.grid(row=1, column=1, padx=(60, 0), sticky=W+E)
    entryPassword.grid(row=2, column=1, padx=(60,0), sticky=W+E)

    buttonLogin = ttk.Button(self, text='Login', command=lambda: self.login(entryUser.get(), entryPassword.get()))
    buttonLogin.grid(row=4, column=1, padx=5, pady=5)

  def login(self, mail, password):
    response, userType = database.login(mail, password)
    if response == 'noUser':
      messagebox.showerror('Usuario inexistente','Parece que no existe el mail ingresado')
    elif response == False:
      messagebox.showerror('Password incorrecto', 'El password introducido es incorrecto')
    elif response == True:
      if userType == 'administradores':
        self.menuAdmin()
      elif userType == 'alumnos':
        self.menuAlumno(mail)
      elif userType == 'maestros':
        self.menuMaestro(mail)
  def menuAdmin(self):
    for widget in self.winfo_children():
      widget.destroy()
    self.title('Control Escolar -Coordinador-')
    self.geometry('600x400')
    nb = ttk.Notebook(self)
    frameCoordinadores = FCC.FrameCoordinador(nb)
    frameAlumnos = FCA.FrameAlumnos(nb)
    frameMaestros = FCM.FrameMaestros(nb)
    frameMaterias = FCMa.FrameMaterias(nb)
    frameGrupos = FCG.FrameGrupos(nb)
    frameHorarios = FCH.FrameHorarios(nb)
    frameSalones = FCS.FrameSalon(nb)
    frameCarreras = FCCa.FrameCarrera(nb)
    framePlaneacion = FCP.FramePlaneacion(nb)
    nb.add(frameCoordinadores, text='Coordinadores')
    nb.add(frameAlumnos, text='Alumnos')
    nb.add(frameMaestros, text='Maestros')
    nb.add(frameMaterias, text='Materias')
    nb.add(frameGrupos, text='Grupos')
    nb.add(frameHorarios, text='Horario')
    nb.add(frameSalones, text='Salon')
    nb.add(frameCarreras, text='Carrera')
    nb.add(framePlaneacion, text='Planeacion')
    nb.pack(fill='both', expand='yes')
    
  def menuAlumno(self, mail):
    for widget in self.winfo_children():
      widget.destroy()
    self.title('Control Escolar -Alumno-')
    self.geometry('600x400')
    nba = ttk.Notebook(self)
    frameDatos = FAD.FrameDatos(nba, mail)
    frameAgenda = FAA.FrameAgenda(nba, mail)
    frameHorario = FAH.FrameHorario(nba, mail)
    
    nba.add(frameDatos, text='Datos')
    nba.add(frameAgenda, text='Agendar Materias')
    nba.add(frameHorario, text='Horario')
    
    nba.pack(fill='both', expand='yes') 
    
  def menuMaestro(self, mail):
    for widget in self.winfo_children():
      widget.destroy()
    self.title('Control Escolar -Alumno-')
    self.geometry('600x400')
    nba = ttk.Notebook(self)
    frameDatos = FMD.FrameDatos(nba, mail)
    frameMaterias = FMM.FrameMaterias(nba, mail)
    frameHorario = FMH.FrameHorario(nba, mail)
    
    nba.add(frameDatos, text='Datos')
    nba.add(frameMaterias, text='Registrar asignaturas')
    nba.add(frameHorario, text='Horario')
    
    nba.pack(fill='both', expand='yes') 



if __name__ == '__main__':
  app = App()
  app.mainloop()