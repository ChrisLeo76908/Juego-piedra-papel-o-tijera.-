import tkinter as tk
from tkinter import messagebox
import random

# Ventana principal
ventana = tk.Tk()
ventana.title("Juego: Piedra, Papel o Tijera")
ventana.geometry("500x500")
ventana.configure(bg="#f0f0f0")

# Variables globales
modo_juego = tk.StringVar(value="CPU")
opciones = ["Piedra", "Papel", "Tijera"]

# Función para determinar el ganador
def determinar_ganador(j1, j2):
    if j1 == j2:
        return "Empate"
    elif (j1 == "Piedra" and j2 == "Tijera") or \
         (j1 == "Papel" and j2 == "Piedra") or \
         (j1 == "Tijera" and j2 == "Papel"):
        return "Jugador 1 Gana"
    else:
        return "Jugador 2 Gana"

# Función para jugar contra la CPU
def jugar_contra_cpu(eleccion_j1):
    eleccion_cpu = random.choice(opciones)
    resultado = determinar_ganador(eleccion_j1, eleccion_cpu)
    messagebox.showinfo("Resultado", f"Tú elegiste: {eleccion_j1}\nCPU eligió: {eleccion_cpu}\n\n{resultado}")

# Variables para dos jugadores
jugador1_eleccion = None

def jugar_dos_jugadores(eleccion, jugador):
    global jugador1_eleccion
    if jugador == 1:
        jugador1_eleccion = eleccion
        messagebox.showinfo("Turno", "Turno del Jugador 2")
    else:
        resultado = determinar_ganador(jugador1_eleccion, eleccion)
        messagebox.showinfo("Resultado", f"Jugador 1 eligió: {jugador1_eleccion}\nJugador 2 eligió: {eleccion}\n\n{resultado}")
        jugador1_eleccion = None

# Función principal de botones
def seleccionar_opcion(eleccion):
    if modo_juego.get() == "CPU":
        jugar_contra_cpu(eleccion)
    else:
        if jugador1_eleccion is None:
            jugar_dos_jugadores(eleccion, 1)
        else:
            jugar_dos_jugadores(eleccion, 2)

# --- Interfaz gráfica ---
titulo = tk.Label(ventana, text="Piedra, Papel o Tijera", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
titulo.pack(pady=20)

frame_modo = tk.Frame(ventana, bg="#f0f0f0")
frame_modo.pack()

tk.Label(frame_modo, text="Modo de Juego:", font=("Arial", 12), bg="#f0f0f0").pack(side="left")
tk.Radiobutton(frame_modo, text="Contra CPU", variable=modo_juego, value="CPU", bg="#f0f0f0").pack(side="left")
tk.Radiobutton(frame_modo, text="2 Jugadores", variable=modo_juego, value="2P", bg="#f0f0f0").pack(side="left")

frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=40)

btn_piedra = tk.Button(frame_botones, text="🪨 Piedra", width=12, height=2, bg="#cce5ff", command=lambda: seleccionar_opcion("Piedra"))
btn_piedra.grid(row=0, column=0, padx=10, pady=10)

btn_papel = tk.Button(frame_botones, text="📄 Papel", width=12, height=2, bg="#d4edda", command=lambda: seleccionar_opcion("Papel"))
btn_papel.grid(row=0, column=1, padx=10, pady=10)

btn_tijera = tk.Button(frame_botones, text="✂️ Tijera", width=12, height=2, bg="#f8d7da", command=lambda: seleccionar_opcion("Tijera"))
btn_tijera.grid(row=0, column=2, padx=10, pady=10)

ventana.mainloop()
