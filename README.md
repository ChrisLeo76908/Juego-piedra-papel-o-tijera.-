PIEDRA, PAPEL O TIJERA - JUEGO INTERACTIVO EN PYTHON

¡BIENVENIDO!

Este proyecto consiste en una versión digital del clásico juego Piedra, Papel o Tijera, desarrollado en Python utilizando la biblioteca Tkinter para la interfaz gráfica. Es un proyecto educativo que busca combinar la lógica de programación con la creación de una experiencia visual amigable e interactiva. 

  - Además del juego en sí, el proyecto incluye funcionalidades como:
    - Dos modos de juego: contra la CPU o entre dos jugadores
    - Dos tipos de partida: una ronda o mejor de tres
    - Registro y actualización de estadísticas en tiempo real
    - Retroalimentación inmediata de los resultados por ronda y al finalizar la partida
Q   - Archivos complementarios: Informe general sobre el proyecto en PDF, Diagrama de flujo en PDF y video explicativo


INSTRUCCIONES DEL JUEGO

-Inicio del Juego
  - Al abrir la aplicación, haz clic en "Iniciar".

-Seleccionar Modo de Juego
  Escoge entre:
    - "Contra la CPU"
    - "Dos Jugadores"
    
-Elegir tipo de partida:
  - Una sola jugada
  - Mejor de 3 rondas

-Realizar jugadas:
  - Cada jugador selecciona su opción: Piedra, Papel o Tijera
  - En el modo CPU, el segundo jugador es la computadora

-Resultados:
  - Se muestra el resultado de cada ronda
  - Al finalizar, se muestran los puntajes finales, el ganador y las estadísticas generales acumuladas.

-Opciones Finales:
  - Puedes elegir "Jugar otra vez" o "Salir"


REQUISITOS
- Requisitos Funcionales:
  - El sistema debe permitir al usuario:
    - Seleccionar entre uno o dos jugadpres
    - Elegir el tipo de partida
    - Realizar una jugada válida
    - Visualizar el resultado de cada ronda
    - Ver estadísticas históricas

- EL sistema debe:
    - Registrar las estadísticas en un archivo '.json'
    - Actualizar las estadísticas es tiempo real
    - Gestionar turnos correctamente en el modo de dos jugadores
    - Mostrar pantallas de manera dinámica: Inicio, Selección, Juego, Resultados

- Requisitos NO Funcionales:
  - Interfaz simple, clara y funcional
  - Tiempo de respuesta inmediato tras cada jugada
  - Persistencia de datos entre sesiones, estadísticas 
  - Aplicación autocontenida: no requiere conexión a internet ni dependencias externas


- CRITERIOS DE USABILIDAD
    - Simplicidad: Interfaz intuitiva con botones claros y textos legibles
    - Accesibilidad: Emplea emojis y colores para facilitar la comprensión visual
    - Flujo guiado: El sistema guía al usuario a través de cada etapa del juego
    - Contraste visual: Se utilizaron colores de fondo suaves y botones con colores contrastantes para mejorar la accesibilidad, azul, verde y rojo
    - Retroalimentación Inmediata: El resultado de cada jugada y de la partida completa se muestra en pantalla de manera clara y animada

- Mensajes de Error y estado:
    - Se notifica si falta alguna elección antes de continuar
    - Se actualiza el mansaje de turno entre jugadores en tiempo real
    - Se evita que un jugador juegue dos veces seguidas por error

ACTUALIZACIÓN DE ESTADÍSTICAS EN TIEMPO REAL
  - Las estadísticas de partidas ganadas por Jugador 1, Jugador 2, la CPU y los empates se almacenan en el archivo 'estadísticas.json'
  - Al finalizar cada partida, las estadísticas se actualizan automáticamente sin intervención del usuario
  - Estas estadísticas se muestran al usuario al final de cada partida para ofrecer retroalimentación histórica


MATERIALES COMPLEMENTARIOS INCLUIDOS EN EL REPOSITORIO
  - Informe del Proyecto
    - Contiene el análisis completo, diseño del sistema, estructura del código, motivación, resultados, limitaciones y conclusiones
  - Diagrama de Flujo 
    - Representación visual del flujo lógico del juego, desde el inicio hasta el final
  - Video Explicativo
    - Demostración visual del funcionamiento del juego y explicación de su código


REQUISITOS TÉCNICOS
- Sistema operativo: Windows 11 Versión 24H2 Compilación SO 26100.6584, probado en ésta versión
    - Visual Studio Code
      - Version 1.105.1, probado en ésta versión
    - Lenguaje
      - Python 3.11.9 Probado en ésta versión
     
  - Librerías necesarias:
    - 'tkinter' incluida por defecto en la mayoría de instalaciones de Python
    - 'random' incluída
    - 'json' incluída
    - 'os' incluída

>**NO es necesario instalar paquetes externos. El juego puede ejecutarse directamente con Python**

COMO EJECUTAR EL JUEGO
  1. Clona este repositorio o descarga los archivos
  2. Asegúrate de tener Python 3.x instalado
  3. Ejecuta el archivo principal del juego

''bash
python juego_piedra_papel_tijera.py

