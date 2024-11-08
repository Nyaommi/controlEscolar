import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import database
import administrador

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

    frameCoordinadores = ttk.Frame(nb)
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

    #frameCoordinadores content
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
    buttonNuevo1 = ttk.Button(frameCoordinadores, text='Nuevo', command=lambda:self.buscar('administradores',entryBusqueda1.get()))
    buttonGuardar1 = ttk.Button(frameCoordinadores, text='Guardar', command=lambda:self.buscar('administradores',entryBusqueda1.get()))
    buttonCancelar1 = ttk.Button(frameCoordinadores, text='Cancelar', command=lambda:self.buscar('administradores',entryBusqueda1.get()))
    buttonEditar1 = ttk.Button(frameCoordinadores, text='Editar', command=lambda:self.buscar('administradores',entryBusqueda1.get()))
    buttonBaja1 = ttk.Button(frameCoordinadores, text='Baja', command=lambda:self.buscar('administradores',entryBusqueda1.get()))

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

  def buscar(self, type, id):
    print(f'{type}, {id}')
    



if __name__ == '__main__':
  app = App()
  app.mainloop()