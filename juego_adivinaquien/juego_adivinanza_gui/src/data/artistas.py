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