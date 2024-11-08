import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import database
import administrador
import frames.coordinador.frameCoordinadores as FC

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

    frameRadio = tk.Frame(self)
    frameRadio.config(relief="groove")
    frameRadio.config(bd=5)
    frameRadio.grid(row=3, column=1)
    userType = tk.StringVar()

    radioAdmin = tk.Radiobutton(frameRadio, text="Coordinador", variable=userType, value='administradores')
    radioAdmin.pack(side="left", padx=3)
    radioStudent = tk.Radiobutton(frameRadio, text="Alumno", variable=userType, value='alumnos')
    radioStudent.pack(side="left", padx=3)
    radioTeacher = tk.Radiobutton(frameRadio, text="Maestro", variable=userType, value='maestros')
    radioTeacher.pack(side="left", padx=3)

    lbUser = ttk.Label(self, text='Email:')
    lbPassword = ttk.Label(self, text='Password:')

    entryUser = ttk.Entry(self)
    entryPassword = ttk.Entry(self, show='*')

    lbTittle.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    lbUser.grid(row=1, column=1, sticky=W)
    lbPassword.grid(row=2, column=1, sticky=W)

    entryUser.grid(row=1, column=1, padx=(60, 0), sticky=W+E)
    entryPassword.grid(row=2, column=1, padx=(60,0), sticky=W+E)

    buttonLogin = ttk.Button(self, text='Login', command=lambda: self.login(userType.get(), entryUser.get(), entryPassword.get()))
    buttonLogin.grid(row=4, column=1, padx=5, pady=5)

  def login(self, userType, mail, password):
    if userType == '':
      messagebox.showwarning('Error de login', 'Por favor selecciones que tipo de usuario es')
    else:
      response = database.login(userType, mail, password)
      if response == 'noUser':
        messagebox.showerror('Usuario inexistente','Parece que no existe el mail ingresado')
      elif response == False:
        messagebox.showerror('Password incorrecto', 'El password introducido es incorrecto')
      elif response == True:
        print(userType)
        if userType == 'administradores':
          self.menuAdmin()
        elif userType == 'alumnos':
          pass
        elif userType == 'maestros':
          pass
  def menuAdmin(self):
    for widget in self.winfo_children():
      widget.destroy()
    self.title('Control Escolar -Coordinador-')
    self.geometry('600x400')
    nb = ttk.Notebook(self)
    nb.pack(fill='both', expand='yes')

    frameCoordinadores = FC.FrameCoordinador(nb)
    frameAlumnos = ttk.Frame(nb)
    frameMaestros = ttk.Frame(nb)
    frameMaterias = ttk.Frame(nb)
    frameGrupos = ttk.Frame(nb)
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