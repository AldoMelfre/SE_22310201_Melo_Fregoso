import random

artistas = [
    "Shakira", "Bad Bunny", "Taylor Swift", "Ed Sheeran", "Adele", "Drake", "Beyoncé", "Rihanna",
    "Bruno Mars", "Lady Gaga", "Justin Bieber", "Selena Gomez", "Dua Lipa", "J Balvin", "Karol G",
    "Maluma", "Camila Cabello", "Billie Eilish", "The Weeknd", "Harry Styles", "Luis Miguel",
    "Juanes", "Rosalía", "Enrique Iglesias", "Daddy Yankee", "Ozuna", "Natti Natasha", "Anitta",
    "Sam Smith", "Katy Perry", "Shawn Mendes", "Ariana Grande", "Jennifer Lopez", "Marc Anthony",
    "Gloria Trevi", "Alejandro Sanz", "Pablo Alborán", "Manuel Turizo", "Sebastián Yatra",
    "Carlos Vives", "Lali Espósito"
]

artistas_nuevos = {}

caracteristicas_generales = [
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
    {"pregunta": "¿Es de América?", "si": [
        "Shakira", "Bad Bunny", "Drake", "Beyoncé", "Rihanna", "Bruno Mars", "Lady Gaga", "Justin Bieber",
        "Selena Gomez", "J Balvin", "Karol G", "Maluma", "Camila Cabello", "Billie Eilish", "The Weeknd",
        "Luis Miguel", "Juanes", "Daddy Yankee", "Ozuna", "Natti Natasha", "Anitta", "Katy Perry",
        "Ariana Grande", "Jennifer Lopez", "Marc Anthony", "Gloria Trevi", "Manuel Turizo", "Sebastián Yatra",
        "Carlos Vives", "Lali Espósito"
    ], "no": [
        "Taylor Swift", "Ed Sheeran", "Adele", "Dua Lipa", "Harry Styles", "Rosalía", "Enrique Iglesias",
        "Sam Smith", "Alejandro Sanz", "Pablo Alborán"
    ]},
    {"pregunta": "¿Canta reggaetón?", "si": [
        "Bad Bunny", "J Balvin", "Karol G", "Maluma", "Daddy Yankee", "Ozuna", "Natti Natasha", "Anitta",
        "Manuel Turizo", "Sebastián Yatra"
    ], "no": []},
    {"pregunta": "¿Canta pop?", "si": [
        "Shakira", "Taylor Swift", "Ed Sheeran", "Adele", "Drake", "Beyoncé", "Rihanna", "Bruno Mars",
        "Lady Gaga", "Justin Bieber", "Selena Gomez", "Dua Lipa", "Camila Cabello", "Billie Eilish",
        "The Weeknd", "Harry Styles", "Sam Smith", "Katy Perry", "Shawn Mendes", "Ariana Grande",
        "Jennifer Lopez", "Marc Anthony", "Rosalía", "Alejandro Sanz", "Pablo Alborán", "Carlos Vives", "Lali Espósito"
    ], "no": []},
    {"pregunta": "¿Canta en español?", "si": [
        "Shakira", "J Balvin", "Karol G", "Maluma", "Luis Miguel", "Juanes", "Daddy Yankee", "Ozuna",
        "Natti Natasha", "Anitta", "Jennifer Lopez", "Marc Anthony", "Gloria Trevi", "Rosalía",
        "Alejandro Sanz", "Pablo Alborán", "Manuel Turizo", "Sebastián Yatra", "Carlos Vives", "Lali Espósito"
    ], "no": []},
    {"pregunta": "¿Canta en inglés?", "si": [
        "Taylor Swift", "Ed Sheeran", "Adele", "Drake", "Beyoncé", "Rihanna", "Bruno Mars", "Lady Gaga",
        "Justin Bieber", "Selena Gomez", "Dua Lipa", "Camila Cabello", "Billie Eilish", "The Weeknd",
        "Harry Styles", "Sam Smith", "Katy Perry", "Shawn Mendes", "Ariana Grande"
    ], "no": []},
    {"pregunta": "¿Ha ganado un Grammy?", "si": [
        "Shakira", "Taylor Swift", "Ed Sheeran", "Adele", "Drake", "Beyoncé", "Rihanna", "Bruno Mars",
        "Lady Gaga", "Justin Bieber", "Dua Lipa", "J Balvin", "Karol G", "Maluma", "Camila Cabello",
        "Billie Eilish", "The Weeknd", "Harry Styles", "Luis Miguel", "Juanes", "Daddy Yankee",
        "Ozuna", "Sam Smith", "Katy Perry", "Shawn Mendes", "Ariana Grande", "Jennifer Lopez",
        "Marc Anthony", "Rosalía", "Alejandro Sanz", "Pablo Alborán", "Manuel Turizo", "Sebastián Yatra",
        "Carlos Vives"
    ], "no": []}
]

caracteristicas_personales = [
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
    posibles = set(artistas)
    for c in caracteristicas_generales:
        resp = hechos.get(c["pregunta"])
        if resp == "si":
            posibles &= set(c["si"])
        elif resp == "no":
            if c["no"]:
                posibles &= set(c["no"])
            else:
                posibles -= set(c["si"])
        elif resp == "nose":
            continue
    for c in caracteristicas_personales:
        resp = hechos.get(c["pregunta"])
        if resp == "si":
            posibles &= set(c["si"])
        elif resp == "no":
            if c["no"]:
                posibles &= set(c["no"])
            else:
                posibles -= set(c["si"])
        elif resp == "nose":
            continue
    for nombre, inf in artistas_nuevos.items():
        coincide = True
        for k, v in hechos.items():
            if k in inf and inf[k] != v and v != "nose":
                coincide = False
                break
        if coincide:
            posibles.add(nombre)
    return list(posibles)

def aprender():
    print("\nNo pude adivinar. ¡Ayúdame a aprender para la próxima vez!")
    nuevo_artista = input("¿Cuál era el artista correcto? ").strip()
    inferencias = {}
    for c in caracteristicas_generales + caracteristicas_personales:
        resp = input(f"{c['pregunta']} (si/no/nose): ").strip().lower()
        inferencias[c["pregunta"]] = resp
        if resp == "si" and nuevo_artista not in c["si"]:
            c["si"].append(nuevo_artista)
        elif resp == "no" and "no" in c and nuevo_artista not in c["no"]:
            c["no"].append(nuevo_artista)
    if nuevo_artista not in artistas:
        artistas.append(nuevo_artista)
        print(f"Agregado artista: {nuevo_artista}")
    artistas_nuevos[nuevo_artista] = inferencias
    print(f"Inferencias guardadas para {nuevo_artista}: {inferencias}")
    nueva_pregunta = input("Agrega una pregunta exclusiva para este artista (o deja vacío para omitir): ").strip()
    if nueva_pregunta:
        nueva_respuesta = input(f"¿La respuesta para {nuevo_artista} es 'si', 'no' o 'nose'? ").strip().lower()
        caracteristicas_personales.append({"pregunta": nueva_pregunta, "si": [nuevo_artista] if nueva_respuesta == "si" else [],
                               "no": [nuevo_artista] if nueva_respuesta == "no" else []})

def jugar():
    print("¡Piensa en un artista internacional y yo intentaré adivinarlo!")
    hechos = {}
    preguntas_respondidas = 0
    MAX_PREGUNTAS = 10
    preguntas_ya_preguntadas = set()
    preguntas = caracteristicas_generales + caracteristicas_personales
    while preguntas_respondidas < MAX_PREGUNTAS and preguntas:
        for c in preguntas:
            if c["pregunta"] not in preguntas_ya_preguntadas:
                pregunta_actual = c
                break
        else:
            pregunta_actual = random.choice([c for c in preguntas if c["pregunta"] not in preguntas_ya_preguntadas])
        print(f"Pregunta: {pregunta_actual['pregunta']}")
        respuesta = input(f"{pregunta_actual['pregunta']} (si/no/nose): ").strip().lower()
        hechos[pregunta_actual["pregunta"]] = respuesta
        preguntas_ya_preguntadas.add(pregunta_actual["pregunta"])
        preguntas_respondidas += 1
        posibles = inferencia(hechos)
        print(f"Posibles artistas según tus respuestas: {', '.join(posibles) if posibles else 'Ninguno'}")
        if len(posibles) == 1:
            print(f"¡Creo que el artista es: {posibles[0]}!")
            return
    aprender()

if __name__ == "__main__":
    jugar()