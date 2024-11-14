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

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Login')
    self.geometry('500x350')
    self.currentUser = None
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
        print('alumnos')
      elif userType == 'maestros':
        print('maestros')
  def menuAdmin(self):
    for widget in self.winfo_children():
      widget.destroy()
    self.title('Control Escolar -Coordinador-')
    self.geometry('600x400')
    nb = ttk.Notebook(self)
    nb.pack(fill='both', expand='yes')

    frameCoordinadores = FCC.FrameCoordinador(nb)
    frameAlumnos = FCA.FrameAlumnos(nb)
    frameMaestros = FCM.FrameMaestros(nb)
    frameMaterias = FCMa.FrameMaterias(nb)
    frameGrupos = FCG.FrameGrupos(nb)
    frameHorarios = ttk.Frame(nb)
    frameSalones = ttk.Frame(nb)
    frameCarreras = ttk.Frame(nb)
    framePlaneacion = ttk.Frame(nb)

    nb.add(frameCoordinadores, text='Coordinadores')
    nb.add(frameAlumnos, text='Alumnos')
    nb.add(frameMaestros, text='Maestros')
    nb.add(frameMaterias, text='Materias')
    nb.add(frameGrupos, text='Grupos')
    nb.add(frameHorarios, text='Horario')
    nb.add(frameSalones, text='Salon')
    nb.add(frameCarreras, text='Carrera')
    nb.add(framePlaneacion, text='Planeacion')
    



if __name__ == '__main__':
  app = App()
  app.mainloop()