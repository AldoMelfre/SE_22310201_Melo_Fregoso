import json  # Importa el módulo para manejar archivos JSON
import os  # Importa el módulo para operaciones del sistema operativo
import difflib  # Importa el módulo para comparar secuencias y encontrar similitudes
import re  # Importa el módulo para expresiones regulares
from typing import Dict, List, Tuple, Optional  # Importa tipos para anotaciones

DB_PATH = "Practica 3/base_conocimiento.json"  # Ruta relativa del archivo de la base de conocimiento
SIMILARITY_THRESHOLD = 0.85  # Umbral para considerar coincidencia suficiente

# ----------------------------
# Utilidades de normalización
# ----------------------------
def normalizar_texto(s: str) -> str:
    s = s.lower().strip()  # Convierte a minúsculas y elimina espacios al inicio/fin
    s = re.sub(r"[¿?¡!.,;:\-_/\\()\[\]{}\"']", " ", s)  # Elimina signos de puntuación
    s = re.sub(r"\s+", " ", s)  # Colapsa múltiples espacios en uno solo
    return s  # Devuelve el texto normalizado

# --------------------------------
# Capa de persistencia (JSON file)
# --------------------------------
def cargar_base() -> List[Dict[str, str]]:
    """Carga la base de conocimiento. Si no existe, crea una con 3 entradas."""
    if not os.path.exists(DB_PATH):  # Si el archivo no existe
        base = [  # Crea base inicial con 3 entradas
            {"pattern": "hola", "response": "¡Hola! 😄"},
            {"pattern": "como estas", "response": "¡Muy bien! ¿Y tú cómo estás?"},
            {"pattern": "de que te gustaria hablar", "response": "Podemos hablar de tecnología, estudios o tus proyectos."},
        ]
        guardar_base(base)  # Guarda la base inicial en el archivo
        return base  # Devuelve la base

    with open(DB_PATH, "r", encoding="utf-8") as f:  # Abre el archivo en modo lectura
        try:
            data = json.load(f)  # Carga el contenido JSON
            # asegura estructura mínima
            if not isinstance(data, list):  # Verifica que sea una lista
                raise ValueError("Estructura inválida")
            for x in data:  # Verifica cada elemento
                if not isinstance(x, dict) or "pattern" not in x or "response" not in x:
                    raise ValueError("Estructura inválida")
            return data  # Devuelve la base cargada
        except Exception:
            # si algo falla, re-inicializa
            base = [  # Crea base inicial si hay error
                {"pattern": "hola", "response": "¡Hola! 😄"},
                {"pattern": "como estas", "response": "¡Muy bien! ¿Y tú cómo estás?"},
                {"pattern": "de que te gustaria hablar", "response": "Podemos hablar de tecnología, estudios o tus proyectos."},
            ]
            guardar_base(base)  # Guarda la base inicial
            return base  # Devuelve la base

def guardar_base(base: List[Dict[str, str]]) -> None:
    with open(DB_PATH, "w", encoding="utf-8") as f:  # Abre el archivo en modo escritura
        json.dump(base, f, ensure_ascii=False, indent=2)  # Guarda la base en formato JSON

# ------------------------------------
# Búsqueda y coincidencia de preguntas
# ------------------------------------
def mejor_coincidencia(base: List[Dict[str, str]], consulta: str) -> Tuple[Optional[Dict[str, str]], float]:
    """
    Devuelve (entrada_mejor, score_similitud). Usa normalización y difflib.
    """
    consulta_norm = normalizar_texto(consulta)  # Normaliza la consulta del usuario
    if not consulta_norm:  # Si la consulta está vacía
        return None, 0.0  # No hay coincidencia

    patrones_norm = [normalizar_texto(item["pattern"]) for item in base]  # Normaliza todos los patrones
    match = difflib.get_close_matches(consulta_norm, patrones_norm, n=1, cutoff=0.0)  # Busca el patrón más parecido
    if not match:  # Si no hay coincidencia
        return None, 0.0

    mejor_patron_norm = match[0]  # Obtiene el mejor patrón normalizado
    score = difflib.SequenceMatcher(a=consulta_norm, b=mejor_patron_norm).ratio()  # Calcula el score de similitud
    # encuentra el diccionario original que corresponde a ese patrón normalizado
    for item in base:  # Busca el elemento original en la base
        if normalizar_texto(item["pattern"]) == mejor_patron_norm:
            return item, score  # Devuelve el elemento y el score
    return None, 0.0  # Si no encuentra, devuelve None

# -----------------------------
# Adquisición del conocimiento
# -----------------------------
def adquirir_conocimiento(base: List[Dict[str, str]], pregunta: str) -> None:
    """
    Pregunta al usuario cuál debería ser la respuesta, la guarda y persiste.
    """
    print("Bot: No conozco la respuesta a esa pregunta todavía. 🤔")  # Informa que no sabe la respuesta
    print(f"Bot: ¿Qué debería responder la próxima vez cuando alguien diga: \"{pregunta}\"?")  # Solicita respuesta
    print("     (Escribe tu respuesta y presiona Enter; o escribe 'omitir' para no guardar.)")
    nueva_resp = input("Tú: ").strip()  # Lee la respuesta del usuario

    if nueva_resp.lower() == "omitir" or nueva_resp == "":  # Si el usuario omite
        print("Bot: Entendido, no guardaré nada por ahora. 👍")
        return  # No guarda nada

    # Guarda nuevo par pregunta-respuesta
    base.append({
        "pattern": normalizar_texto(pregunta),  # Guarda la pregunta normalizada
        "response": nueva_resp  # Guarda la respuesta del usuario
    })
    guardar_base(base)  # Persiste la base actualizada
    print("Bot: ¡Gracias! He aprendido algo nuevo. 🧠✅")  # Agradece al usuario

# -------------
# Bucle de chat
# -------------
def main():
    print("=== Chat con Adquisición de Conocimiento ===")  # Mensaje de bienvenida
    print("Escribe 'salir' para terminar.")  # Instrucción para salir
    base = cargar_base()  # Carga la base de conocimiento

    # Opcional: muestra cuántas entradas hay
    print(f"(Base cargada con {len(base)} entradas)")  # Muestra el número de entradas

    while True:  # Bucle principal del chat
        usuario = input("\nTú: ").strip()  # Lee la entrada del usuario
        if usuario.lower() == "salir":  # Si el usuario quiere salir
            print("Bot: ¡Hasta luego! 👋")
            break  # Sale del bucle

        # Buscar mejor coincidencia
        item, score = mejor_coincidencia(base, usuario)  # Busca la mejor coincidencia

        if item and score >= SIMILARITY_THRESHOLD:  # Si hay coincidencia suficiente
            print(f"Bot: {item['response']}")  # Muestra la respuesta
        else:
            # No hay match suficiente → activar adquisición
            adquirir_conocimiento(base, usuario)  # Solicita nueva respuesta al usuario

if __name__ == "__main__":  # Punto de entrada principal
    main()  # Ejecuta el chat
