import random  # Importa el módulo random para seleccionar elementos aleatoriamente


# Lista de 40 artistas internacionales
artistas = [
    "Shakira", "Bad Bunny", "Taylor Swift", "Ed Sheeran", "Adele", "Drake", "Beyoncé", "Rihanna",
    "Bruno Mars", "Lady Gaga", "Justin Bieber", "Selena Gomez", "Dua Lipa", "J Balvin", "Karol G",
    "Maluma", "Camila Cabello", "Billie Eilish", "The Weeknd", "Harry Styles", "Luis Miguel",
    "Juanes", "Rosalía", "Enrique Iglesias", "Daddy Yankee", "Ozuna", "Natti Natasha", "Anitta",
    "Sam Smith", "Katy Perry", "Shawn Mendes", "Ariana Grande", "Jennifer Lopez", "Marc Anthony",
    "Gloria Trevi", "Alejandro Sanz", "Pablo Alborán", "Manuel Turizo", "Sebastián Yatra",
    "Carlos Vives", "Lali Espósito"
]

# Diccionario para guardar artistas nuevos y sus inferencias exclusivas
artistas_nuevos = {}

# Características generales
caracteristicas_generales = [
    # Cada elemento es un diccionario con una pregunta y listas de artistas que cumplen o no cumplen la característica
    {"pregunta": "¿Es mujer?", "si": [
        "Shakira", "Taylor Swift", "Adele", "Beyoncé", "Rihanna", "Lady Gaga", "Selena Gomez",
        "Dua Lipa", "Karol G", "Camila Cabello", "Billie Eilish", "Natti Natasha", "Anitta",
        "Katy Perry", "Ariana Grande", "Jennifer Lopez", "Gloria Trevi", "Rosalía", "Lali Espósito"
    ], "no": [
        "Bad Bunny", "Ed Sheeran", "Drake", "Bruno Mars", "Justin Bieber", "J Balvin", "Maluma",
        "The Weeknd", "Harry Styles", "Luis Miguel", "Juanes", "Enrique Iglesias", "Daddy Yankee",
        "Ozuna", "Sam Smith", "Shawn Mendes", "Marc Anthony", "Alejandro Sanz", "Pablo Alborán",
        "Manuel Turizo", "Sebastián Yatra", "Carlos Vives"
    ]},
    # ... (más características generales)
    {"pregunta": "¿Es de América?", "si": [
        # Lista de artistas americanos
        "Shakira", "Bad Bunny", "Drake", "Beyoncé", "Rihanna", "Bruno Mars", "Lady Gaga", "Justin Bieber",
        "Selena Gomez", "J Balvin", "Karol G", "Maluma", "Camila Cabello", "Billie Eilish", "The Weeknd",
        "Luis Miguel", "Juanes", "Daddy Yankee", "Ozuna", "Natti Natasha", "Anitta", "Katy Perry",
        "Ariana Grande", "Jennifer Lopez", "Marc Anthony", "Gloria Trevi", "Manuel Turizo", "Sebastián Yatra",
        "Carlos Vives", "Lali Espósito"
    ], "no": [
        # Lista de artistas no americanos
        "Taylor Swift", "Ed Sheeran", "Adele", "Dua Lipa", "Harry Styles", "Rosalía", "Enrique Iglesias",
        "Sam Smith", "Alejandro Sanz", "Pablo Alborán"
    ]},
    # ... (más características generales)
    {"pregunta": "¿Canta reggaetón?", "si": [
        # Lista de artistas que cantan reggaetón
        "Bad Bunny", "J Balvin", "Karol G", "Maluma", "Daddy Yankee", "Ozuna", "Natti Natasha", "Anitta",
        "Manuel Turizo", "Sebastián Yatra"
    ], "no": []},  # Lista vacía para los que no cantan reggaetón
    # ... (más características generales)
    {"pregunta": "¿Canta pop?", "si": [
        # Lista de artistas que cantan pop
        "Shakira", "Taylor Swift", "Ed Sheeran", "Adele", "Drake", "Beyoncé", "Rihanna", "Bruno Mars",
        "Lady Gaga", "Justin Bieber", "Selena Gomez", "Dua Lipa", "Camila Cabello", "Billie Eilish",
        "The Weeknd", "Harry Styles", "Sam Smith", "Katy Perry", "Shawn Mendes", "Ariana Grande",
        "Jennifer Lopez", "Marc Anthony", "Rosalía", "Alejandro Sanz", "Pablo Alborán", "Carlos Vives", "Lali Espósito"
    ], "no": []},
    # ... (más características generales)
    {"pregunta": "¿Canta en español?", "si": [
        # Lista de artistas que cantan en español
        "Shakira", "J Balvin", "Karol G", "Maluma", "Luis Miguel", "Juanes", "Daddy Yankee", "Ozuna",
        "Natti Natasha", "Anitta", "Jennifer Lopez", "Marc Anthony", "Gloria Trevi", "Rosalía",
        "Alejandro Sanz", "Pablo Alborán", "Manuel Turizo", "Sebastián Yatra", "Carlos Vives", "Lali Espósito"
    ], "no": []},
    # ... (más características generales)
    {"pregunta": "¿Canta en inglés?", "si": [
        # Lista de artistas que cantan en inglés
        "Taylor Swift", "Ed Sheeran", "Adele", "Drake", "Beyoncé", "Rihanna", "Bruno Mars", "Lady Gaga",
        "Justin Bieber", "Selena Gomez", "Dua Lipa", "Camila Cabello", "Billie Eilish", "The Weeknd",
        "Harry Styles", "Sam Smith", "Katy Perry", "Shawn Mendes", "Ariana Grande"
    ], "no": []},
    # ... (más características generales)
    {"pregunta": "¿Ha ganado un Grammy?", "si": [
        # Lista de artistas que han ganado un Grammy
        "Shakira", "Taylor Swift", "Ed Sheeran", "Adele", "Drake", "Beyoncé", "Rihanna", "Bruno Mars",
        "Lady Gaga", "Justin Bieber", "Dua Lipa", "J Balvin", "Karol G", "Maluma", "Camila Cabello",
        "Billie Eilish", "The Weeknd", "Harry Styles", "Luis Miguel", "Juanes", "Daddy Yankee",
        "Ozuna", "Sam Smith", "Katy Perry", "Shawn Mendes", "Ariana Grande", "Jennifer Lopez",
        "Marc Anthony", "Rosalía", "Alejandro Sanz", "Pablo Alborán", "Manuel Turizo", "Sebastián Yatra",
        "Carlos Vives"
    ], "no": []}
]

# Características personales (se preguntan después de las generales)
caracteristicas_personales = [
    # Cada elemento es un diccionario con una pregunta y listas de artistas que cumplen o no cumplen la característica
    {"pregunta": "¿Tiene piel clara?", "si": [
        "Taylor Swift", "Ed Sheeran", "Adele", "Lady Gaga", "Selena Gomez", "Dua Lipa", "Billie Eilish",
        "Harry Styles", "Sam Smith", "Katy Perry", "Shawn Mendes", "Ariana Grande", "Jennifer Lopez",
        "Gloria Trevi", "Alejandro Sanz", "Pablo Alborán", "Lali Espósito"
    ], "no": [
        "Shakira", "Bad Bunny", "Drake", "Beyoncé", "Rihanna", "Bruno Mars", "J Balvin", "Karol G",
        "Maluma", "Camila Cabello", "The Weeknd", "Luis Miguel", "Juanes", "Rosalía", "Enrique Iglesias",
        "Daddy Yankee", "Ozuna", "Natti Natasha", "Anitta", "Marc Anthony", "Manuel Turizo",
        "Sebastián Yatra", "Carlos Vives"
    ]},
    # ... (más características personales)
    {"pregunta": "¿Tiene ojos claros?", "si": [
        "Taylor Swift", "Ed Sheeran", "Adele", "Lady Gaga", "Selena Gomez", "Dua Lipa", "Billie Eilish",
        "Harry Styles", "Sam Smith", "Katy Perry", "Shawn Mendes", "Ariana Grande", "Jennifer Lopez",
        "Gloria Trevi", "Alejandro Sanz", "Pablo Alborán", "Lali Espósito"
    ], "no": [
        "Shakira", "Bad Bunny", "Drake", "Beyoncé", "Rihanna", "Bruno Mars", "J Balvin", "Karol G",
        "Maluma", "Camila Cabello", "The Weeknd", "Luis Miguel", "Juanes", "Rosalía", "Enrique Iglesias",
        "Daddy Yankee", "Ozuna", "Natti Natasha", "Anitta", "Marc Anthony", "Manuel Turizo",
        "Sebastián Yatra", "Carlos Vives"
    ]},
    # ... (más características personales)
    {"pregunta": "¿Tiene cabello oscuro?", "si": [
        "Shakira", "Bad Bunny", "Drake", "Beyoncé", "Rihanna", "Bruno Mars", "Lady Gaga", "Justin Bieber",
        "J Balvin", "Karol G", "Maluma", "Camila Cabello", "Billie Eilish", "The Weeknd", "Harry Styles",
        "Luis Miguel", "Juanes", "Rosalía", "Enrique Iglesias", "Daddy Yankee", "Ozuna", "Natti Natasha",
        "Anitta", "Sam Smith", "Shawn Mendes", "Ariana Grande", "Jennifer Lopez", "Marc Anthony",
        "Gloria Trevi", "Alejandro Sanz", "Pablo Alborán", "Manuel Turizo", "Sebastián Yatra",
        "Carlos Vives", "Lali Espósito"
    ], "no": [
        "Taylor Swift", "Ed Sheeran", "Adele", "Selena Gomez", "Dua Lipa", "Katy Perry"
    ]}
]

def inferencia(hechos):
    posibles = set(artistas)  # Inicializa el conjunto de posibles artistas con todos los artistas
    # Aplica primero las generales
    for c in caracteristicas_generales:
        resp = hechos.get(c["pregunta"])  # Obtiene la respuesta del usuario para la pregunta actual
        if resp == "si":
            posibles &= set(c["si"])  # Filtra los artistas que cumplen la característica
        elif resp == "no":
            if c["no"]:
                posibles &= set(c["no"])  # Filtra los artistas que no cumplen la característica
            else:
                posibles -= set(c["si"])  # Elimina los que sí cumplen si no hay lista de "no"
        elif resp == "nose":
            continue  # Si no sabe, no filtra nada
    # Luego aplica las personales
    for c in caracteristicas_personales:
        resp = hechos.get(c["pregunta"])  # Obtiene la respuesta del usuario para la pregunta actual
        if resp == "si":
            posibles &= set(c["si"])  # Filtra los artistas que cumplen la característica
        elif resp == "no":
            if c["no"]:
                posibles &= set(c["no"])  # Filtra los artistas que no cumplen la característica
            else:
                posibles -= set(c["si"])  # Elimina los que sí cumplen si no hay lista de "no"
        elif resp == "nose":
            continue  # Si no sabe, no filtra nada
    # Inferencias exclusivas de artistas nuevos
    for nombre, inf in artistas_nuevos.items():  # Recorre los artistas nuevos y sus inferencias
        coincide = True  # Variable para saber si coincide con las respuestas dadas
        for k, v in hechos.items():  # Recorre cada hecho (pregunta y respuesta)
            if k in inf and inf[k] != v and v != "nose":  # Si la respuesta no coincide y no es "nose"
                coincide = False  # No coincide
                break  # Sale del ciclo
        if coincide:
            posibles.add(nombre)  # Si coincide, agrega el artista nuevo a los posibles
    return list(posibles)  # Devuelve la lista de posibles artistas

def aprender():
    print("\nNo pude adivinar. ¡Ayúdame a aprender para la próxima vez!")  # Mensaje de aprendizaje
    nuevo_artista = input("¿Cuál era el artista correcto? ").strip()  # Pide el nombre del artista correcto
    inferencias = {}  # Diccionario para guardar las inferencias del nuevo artista
    # Pregunta por todas las características generales y personales
    for c in caracteristicas_generales + caracteristicas_personales:
        resp = input(f"{c['pregunta']} (si/no/nose): ").strip().lower()  # Pide la respuesta para cada pregunta
        inferencias[c["pregunta"]] = resp  # Guarda la respuesta en el diccionario
        if resp == "si" and nuevo_artista not in c["si"]:
            c["si"].append(nuevo_artista)  # Agrega el artista a la lista de "si" si corresponde
        elif resp == "no" and "no" in c and nuevo_artista not in c["no"]:
            c["no"].append(nuevo_artista)  # Agrega el artista a la lista de "no" si corresponde
    if nuevo_artista not in artistas:
        artistas.append(nuevo_artista)  # Agrega el artista a la lista principal si no está
        print(f"Agregado artista: {nuevo_artista}")  # Mensaje de confirmación
    artistas_nuevos[nuevo_artista] = inferencias  # Guarda las inferencias del nuevo artista
    print(f"Inferencias guardadas para {nuevo_artista}: {inferencias}")  # Muestra las inferencias guardadas
    nueva_pregunta = input("Agrega una pregunta exclusiva para este artista (o deja vacío para omitir): ").strip()  # Pide una pregunta exclusiva
    if nueva_pregunta:
        nueva_respuesta = input(f"¿La respuesta para {nuevo_artista} es 'si', 'no' o 'nose'? ").strip().lower()  # Pide la respuesta para la pregunta exclusiva
        caracteristicas_personales.append({"pregunta": nueva_pregunta, "si": [nuevo_artista] if nueva_respuesta == "si" else [],
                               "no": [nuevo_artista] if nueva_respuesta == "no" else []})  # Agrega la nueva pregunta a las características personales

def jugar():
    print("¡Piensa en un artista internacional y yo intentaré adivinarlo!")  # Mensaje inicial del juego
    hechos = {}  # Diccionario para guardar las respuestas del usuario
    preguntas_respondidas = 0  # Contador de preguntas respondidas
    MAX_PREGUNTAS = 10  # Número máximo de preguntas
    preguntas_ya_preguntadas = set()  # Conjunto para guardar las preguntas ya hechas
    # Primero pregunta las generales, luego las personales
    preguntas = caracteristicas_generales + caracteristicas_personales  # Lista de todas las preguntas
    while preguntas_respondidas < MAX_PREGUNTAS and preguntas:  # Mientras no se llegue al máximo de preguntas
        for c in preguntas:
            if c["pregunta"] not in preguntas_ya_preguntadas:
                pregunta_actual = c  # Selecciona la siguiente pregunta no hecha
                break
        else:
            pregunta_actual = random.choice([c for c in preguntas if c["pregunta"] not in preguntas_ya_preguntadas])  # Si todas han sido hechas, elige una al azar
        print(f"Pregunta: {pregunta_actual['pregunta']}")  # Muestra la pregunta
        respuesta = input(f"{pregunta_actual['pregunta']} (si/no/nose): ").strip().lower()  # Pide la respuesta al usuario
        hechos[pregunta_actual["pregunta"]] = respuesta  # Guarda la respuesta en el diccionario de hechos
        preguntas_ya_preguntadas.add(pregunta_actual["pregunta"])  # Marca la pregunta como hecha
        preguntas_respondidas += 1  # Incrementa el contador de preguntas respondidas
        posibles = inferencia(hechos)  # Obtiene la lista de posibles artistas según las respuestas
        print(f"Posibles artistas según tus respuestas: {', '.join(posibles) if posibles else 'Ninguno'}")  # Muestra los posibles artistas
        if len(posibles) == 1:
            print(f"¡Creo que el artista es: {posibles[0]}!")  # Si solo queda uno, lo adivina
            return  # Termina el juego
    aprender()  # Si no pudo adivinar, llama a la función de aprendizaje

if __name__ == "__main__":  # Si el archivo se ejecuta directamente
    jugar()  # Inicia el juego