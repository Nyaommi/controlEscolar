import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import string
import database
import clases.alumno as alumno

def FrameHorario(nba, mail):
  teacher = database.getTeacherByMail(mail)
  frameHorario = ttk.Frame(nba)

  # Frame principal para contener el Treeview y las barras de desplazamiento
  frame = ttk.Frame(frameHorario)
  frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

  # Crear estilo para filas más altas
  style = ttk.Style()
  style.configure("Treeview", rowheight=60)  # Ajusta la altura de las filas

  # Crear barras de desplazamiento
  v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
  h_scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)

  # Crear el Treeview
  columns = ["Hora", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
  tree = ttk.Treeview(
      frame,
      columns=columns,
      show="headings",
      yscrollcommand=v_scrollbar.set,
      xscrollcommand=h_scrollbar.set
  )
  v_scrollbar.config(command=tree.yview)
  h_scrollbar.config(command=tree.xview)

  # Configurar encabezados y tamaños de columnas
  for col in columns:
      tree.heading(col, text=col)
      tree.column(col, width=180, anchor="center")  # Ancho de cada columna aumentado

  # Insertar las horas en la primera columna
  horas = [
      "7:00 - 8:50", "9:00 - 10:50", "11:00 - 12:50",
      "13:00 - 14:50", "15:00 - 16:50", "17:00 - 18:50", "19:00 - 20:50"
  ]
  for hora in horas:
      tree.insert("", tk.END, values=[hora] + [""] * (len(columns) - 1))  # Rellena columnas con valores vacíos

  # Colocar widgets en el frame
  tree.grid(row=0, column=0, sticky="nsew")
  v_scrollbar.grid(row=0, column=1, sticky="ns")
  h_scrollbar.grid(row=1, column=0, sticky="ew")

  # Configurar el diseño para que el Treeview se ajuste
  frame.rowconfigure(0, weight=1)
  frame.columnconfigure(0, weight=1)
  
  def limpiar_tabla(tree):
    # Recorrer todas las filas
    for fila in tree.get_children():
        actuales = tree.item(fila, "values")
        # Mantener la hora (columna 0) y vaciar el resto
        nuevos_valores = (actuales[0],) + ("",) * (len(actuales) - 1)
        tree.item(fila, values=nuevos_valores)

  def insertar_dato_en_celda(tree, hora, dia, nuevo_valor):
    for fila in tree.get_children():
        valores = tree.item(fila, "values")
        if valores[0] == hora:
            dias = ["Hora", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
            
            columna_idx = dias.index(dia)
            
            valores = list(valores)  # Convertir la tupla en lista para modificarla
            valores[columna_idx] = nuevo_valor  # Insertar el nuevo valor en la columna correcta
    
            tree.item(fila, values=tuple(valores))
            break  # Si solo hay una fila que cumple la condición, salimos del bucle
  
  def getHorario(idMaestro):
    horario = []
    horario = database.getHorarioMaestro(idMaestro)
    
    if horario:
      for i in horario:
        insertar_dato_en_celda(tree, i[0], i[1], i[2])
    
  
  getHorario(teacher.getId())
    


  return frameHorario
