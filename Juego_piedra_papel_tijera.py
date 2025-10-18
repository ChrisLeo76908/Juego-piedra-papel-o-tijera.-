import tkinter as tk
from tkinter import messagebox
import random
import json
import os

# ------------------ VARIABLES GLOBALES ------------------ #
opciones = ["Piedra", "Papel", "Tijera"]
modo_juego = None
tipo_partida = None
jugador1_eleccion = None
rondas_jugadas = 0
puntaje_j1 = 0
puntaje_j2 = 0
estadisticas_file = "estadisticas.json"

# ------------------ FUNCIONES DE ESTADÍSTICAS ------------------ #
def cargar_estadisticas():
    if not os.path.exists(estadisticas_file):
        return {"Jugador 1": 0, "Jugador 2": 0, "CPU": 0, "Empates": 0}
    with open(estadisticas_file, "r") as f:
        return json.load(f)

def guardar_estadisticas(data):
    with open(estadisticas_file, "w") as f:
        json.dump(data, f, indent=4)

def actualizar_estadisticas(ganador):
    data = cargar_estadisticas()
    if ganador in data:
        data[ganador] += 1
    guardar_estadisticas(data)

# ------------------ LÓGICA DEL JUEGO ------------------ #
def determinar_ganador(j1, j2):
    if j1 == j2:
        return "Empate"
    elif (j1 == "Piedra" and j2 == "Tijera") or \
         (j1 == "Papel" and j2 == "Piedra") or \
         (j1 == "Tijera" and j2 == "Papel"):
        return "Jugador 1"
    else:
        return "Jugador 2"

def jugar(eleccion):
    global jugador1_eleccion, rondas_jugadas, puntaje_j1, puntaje_j2

    if modo_juego == "CPU":
        j1 = eleccion
        j2 = random.choice(opciones)
    else:
        if jugador1_eleccion is None:
            jugador1_eleccion = eleccion
            info_label.config(text="Turno del Jugador 2 ✋")
            return
        else:
            j1 = jugador1_eleccion
            j2 = eleccion
            jugador1_eleccion = None

    ganador = determinar_ganador(j1, j2)
    rondas_jugadas += 1

    # Actualizar puntajes
    if ganador == "Jugador 1":
        puntaje_j1 += 1
    elif ganador == "Jugador 2":
        puntaje_j2 += 1

    # Mostrar resultados parciales
    resultado_label.config(
        text=f"Jugador 1 eligió: {j1} | {'CPU' if modo_juego == 'CPU' else 'Jugador 2'} eligió: {j2}\nResultado de la ronda: {ganador}",
        fg="blue",
        font=("Arial", 12, "italic")
    )

    if tipo_partida == "Una Jugada" or rondas_jugadas == 3:
        final = ganador if tipo_partida == "Una Jugada" else (
            "Jugador 1" if puntaje_j1 > puntaje_j2 else
            "Jugador 2" if puntaje_j2 > puntaje_j1 else
            "Empate"
        )
        mostrar_resultado_final(final)
    else:
        info_label.config(text=f"Ronda {rondas_jugadas + 1} - ¡Sigue jugando!")

def mostrar_resultado_final(ganador):
    global puntaje_j1, puntaje_j2, rondas_jugadas

    if ganador == "Empate":
        emoji = "😐"
        mensaje = "¡Es un empate!"
    elif ganador == "Jugador 1":
        emoji = "🏆"
        mensaje = "¡Jugador 1 gana!"
    else:
        emoji = "🥈"
        mensaje = f"¡{ganador} gana!"

    actualizar_estadisticas(ganador if ganador != "Empate" else "Empates")
    data = cargar_estadisticas()

    limpiar_pantalla()

    # Resultado final
    tk.Label(ventana, text=f"{mensaje} {emoji}", font=("Arial", 22, "bold"), bg="#f0f0f0").pack(pady=20)
    tk.Label(ventana, text=f"Puntaje final:\nJugador 1 = {puntaje_j1}  |  {'CPU' if modo_juego == 'CPU' else 'Jugador 2'} = {puntaje_j2}",
             font=("Arial", 14), bg="#f0f0f0", fg="black").pack(pady=10)

    # Línea divisoria
    tk.Label(ventana, text="―" * 60, bg="#f0f0f0").pack()

    # Estadísticas
    tk.Label(ventana, text="📊 Estadísticas generales", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
    tk.Label(
        ventana,
        text=(
            f"🏅 Jugador 1: {data['Jugador 1']} victorias\n"
            f"👤 Jugador 2: {data['Jugador 2']} victorias\n"
            f"🤖 CPU: {data['CPU']} victorias\n"
            f"🤝 Empates: {data['Empates']}"
        ),
        font=("Arial", 12), bg="#f0f0f0"
    ).pack(pady=5)

    # Botones finales
    tk.Button(ventana, text="🔁 Jugar otra vez", command=menu_modo, width=20, height=2, bg="#d4edda").pack(pady=10)
    tk.Button(ventana, text="🚪 Salir", command=ventana.destroy, width=20, height=2, bg="#f8d7da").pack(pady=5)

# ------------------ INTERFAZ GRÁFICA ------------------ #
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("600x500")
ventana.configure(bg="#f0f0f0")

def limpiar_pantalla():
    for widget in ventana.winfo_children():
        widget.destroy()

# --------- PANTALLAS --------- #
def pantalla_inicio():
    limpiar_pantalla()
    tk.Label(ventana, text="✊📄✂️", font=("Arial", 60), bg="#f0f0f0").pack(pady=30)
    tk.Label(ventana, text="¡Bienvenido al juego!", font=("Arial", 24, "bold"), bg="#f0f0f0").pack(pady=10)
    tk.Button(ventana, text="▶️ Iniciar", font=("Arial", 16, "bold"), bg="#cce5ff", width=15, height=2, command=menu_modo).pack(pady=30)

def menu_modo():
    global modo_juego, tipo_partida
    limpiar_pantalla()
    tk.Label(ventana, text="⚙️ Selecciona modo de juego", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)
    modo_juego_var = tk.StringVar(value="CPU")

    frame = tk.Frame(ventana, bg="#f0f0f0")
    frame.pack(pady=10)
    tk.Radiobutton(frame, text="🤖 Contra CPU", variable=modo_juego_var, value="CPU", font=("Arial", 14), bg="#f0f0f0").pack(anchor="w")
    tk.Radiobutton(frame, text="👫 Dos Jugadores", variable=modo_juego_var, value="2P", font=("Arial", 14), bg="#f0f0f0").pack(anchor="w")

    tk.Label(ventana, text="\n🎮 Tipo de partida", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)
    tipo_var = tk.StringVar(value="Una Jugada")

    tk.Radiobutton(ventana, text="⚡ Una Jugada", variable=tipo_var, value="Una Jugada", font=("Arial", 14), bg="#f0f0f0").pack()
    tk.Radiobutton(ventana, text="🔥 Mejor de 3", variable=tipo_var, value="Mejor de 3", font=("Arial", 14), bg="#f0f0f0").pack()

    def confirmar():
        global modo_juego, tipo_partida, puntaje_j1, puntaje_j2, rondas_jugadas
        modo_juego = modo_juego_var.get()
        tipo_partida = tipo_var.get()
        puntaje_j1 = 0
        puntaje_j2 = 0
        rondas_jugadas = 0
        pantalla_juego()

    tk.Button(ventana, text="✅ Confirmar", command=confirmar, bg="#cce5ff", width=20, height=2).pack(pady=25)

def pantalla_juego():
    limpiar_pantalla()
    global info_label, resultado_label

    tk.Label(ventana, text="✊📄✂️ Elige tu jugada", font=("Arial", 22, "bold"), bg="#f0f0f0").pack(pady=20)
    info_label = tk.Label(ventana, text="Turno del Jugador 1", font=("Arial", 14), bg="#f0f0f0")
    info_label.pack(pady=10)

    frame_botones = tk.Frame(ventana, bg="#f0f0f0")
    frame_botones.pack(pady=20)

    tk.Button(frame_botones, text="🪨 Piedra", width=12, height=2, bg="#cce5ff", command=lambda: jugar("Piedra")).grid(row=0, column=0, padx=10)
    tk.Button(frame_botones, text="📄 Papel", width=12, height=2, bg="#d4edda", command=lambda: jugar("Papel")).grid(row=0, column=1, padx=10)
    tk.Button(frame_botones, text="✂️ Tijera", width=12, height=2, bg="#f8d7da", command=lambda: jugar("Tijera")).grid(row=0, column=2, padx=10)

    resultado_label = tk.Label(ventana, text="", bg="#f0f0f0", font=("Arial", 12))
    resultado_label.pack(pady=10)

# Iniciar la app
pantalla_inicio()
ventana.mainloop()
