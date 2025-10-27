# Juego Adivinanza - Artist Guessing Game

## Descripción
Este proyecto es un juego de adivinanza de artistas internacionales, donde el usuario piensa en un artista y el programa intenta adivinarlo haciendo preguntas sobre sus características. La interfaz gráfica está implementada utilizando Tkinter.

## Estructura del Proyecto
```
juego_adivinanza_gui
├── src
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── gui.py                 # Implementación de la interfaz gráfica
│   ├── juegoadivinanza.py     # Lógica del juego de adivinanza
│   ├── data
│   │   └── artistas.py        # Datos relacionados con los artistas
│   └── tests
│       └── test_inferencia.py # Pruebas unitarias para la lógica de inferencia
├── requirements.txt           # Dependencias del proyecto
├── .gitignore                 # Archivos y directorios a ignorar por Git
└── README.md                  # Documentación del proyecto
```

## Requisitos
Asegúrate de tener Python instalado en tu sistema. Este proyecto utiliza las siguientes dependencias:

- Tkinter (incluido en la mayoría de las instalaciones de Python)

Para instalar las dependencias, ejecuta:
```
pip install -r requirements.txt
```

## Ejecución
Para ejecutar el juego, navega a la carpeta `src` y ejecuta el archivo `main.py`:
```
python main.py
```

## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el juego o agregar nuevas características, siéntete libre de hacer un fork del repositorio y enviar un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT.