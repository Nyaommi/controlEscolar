import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database


def FramePlaneacion(nb):
    # Crear el contenedor del Canvas
    contenedor = ttk.Frame(nb)
    canvas = tk.Canvas(contenedor)
    scrollbar_x = ttk.Scrollbar(contenedor, orient="horizontal", command=canvas.xview)
    scrollbar_y = ttk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    canvas.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

    # Crear el frame dentro del Canvas
    framePlaneacion = ttk.Frame(canvas)
    
    def crear_cuadricula(frame, filas, columnas, datos):
        for i in range(filas):
            for j in range(columnas):
                # Crear un marco para cada celda
                celda = tk.Frame(frame, bg="white", borderwidth=1, relief="solid", width=200, height=100)
                celda.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")
                
                # Obtener contenido para esta celda
                contenido = datos.get((i, j), "")  # Buscar información específica para la celda o dejarla vacía
                
                # Crear etiqueta para mostrar el contenido
                etiqueta = tk.Label(celda, text=contenido, bg="white", wraplength=180, justify="center")
                etiqueta.pack(expand=True, fill=tk.BOTH)
    
    filas = 15
    columnas = 5
    
    auxdatos = database.getPlaneacion()
    
    datos = {}
    
    fila = 0
    columna = 0
    
    for cadena in auxdatos:
      datos[(fila, columna)] = cadena
      columna+=1
      
      if columna == 4:
        columna=0
        fila+=1
    
    crear_cuadricula(framePlaneacion, filas, columnas, datos)

    # Configuración de ajuste dinámico
    for i in range(filas):
        framePlaneacion.rowconfigure(i, weight=1)
    for j in range(columnas):
        framePlaneacion.columnconfigure(j, weight=1)

    # Agregar framePlaneacion al Canvas
    canvas.create_window((0, 0), window=framePlaneacion, anchor="nw")

    # Ajustar el tamaño del Canvas al contenido
    def ajustar_canvas(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    framePlaneacion.bind("<Configure>", ajustar_canvas)

    # Posicionar elementos en el contenedor
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar_x.grid(row=1, column=0, sticky="ew")
    scrollbar_y.grid(row=0, column=1, sticky="ns")
    contenedor.rowconfigure(0, weight=1)
    contenedor.columnconfigure(0, weight=1)

    return contenedor
