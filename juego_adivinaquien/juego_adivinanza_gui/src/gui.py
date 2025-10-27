import random
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import juegoadivinanza as juego

MAX_PREGUNTAS = 10

def center_window(win, width=None, height=None):
    win.update_idletasks()
    w = width if width is not None else win.winfo_reqwidth()
    h = height if height is not None else win.winfo_reqheight()
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    x = (sw // 2) - (w // 2)
    y = (sh // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

class ArtistGuessingGame:
    """
    Interfaz en UNA sola ventana (sin diálogos Toplevel para preguntar).
    - Botones Sí/No/No sé para responder la pregunta mostrada.
    - Historial a la izquierda, controles a la derecha.
    - Aprende artista usando simpledialog (puede seguir siendo modal).
    """
    def __init__(self, master):
        self.master = master
        master.title("Adivina el artista - Interfaz unificada")
        master.geometry("900x540")
        center_window(master, 900, 540)

        # Layout: izquierda historial, centro pregunta, derecha controles
        main = tk.Frame(master, padx=8, pady=8)
        main.pack(fill=tk.BOTH, expand=True)

        left = tk.Frame(main)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        center = tk.Frame(main, width=420, padx=10)
        center.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        right = tk.Frame(main, width=220, padx=6)
        right.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(left, text="Historial de interacción", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        self.history = tk.Text(left, state="disabled", wrap="word", width=60)
        self.history.pack(fill=tk.BOTH, expand=True, padx=(0,8))

        # Pregunta actual
        tk.Label(center, text="Pregunta actual", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        self.q_label = tk.Label(center, text="Presiona 'Iniciar juego' para comenzar", wraplength=380, justify="left", font=("Segoe UI", 10))
        self.q_label.pack(pady=(6,12), anchor="w")

        btn_frame = tk.Frame(center)
        btn_frame.pack(pady=(0,6), anchor="w")
        self.btn_si = tk.Button(btn_frame, text="Sí", width=10, state="disabled", command=lambda: self._answer("si"))
        self.btn_si.pack(side=tk.LEFT, padx=4)
        self.btn_no = tk.Button(btn_frame, text="No", width=10, state="disabled", command=lambda: self._answer("no"))
        self.btn_no.pack(side=tk.LEFT, padx=4)
        self.btn_ns = tk.Button(btn_frame, text="No sé", width=10, state="disabled", command=lambda: self._answer("nose"))
        self.btn_ns.pack(side=tk.LEFT, padx=4)

        tk.Label(center, text="Preguntas restantes:", font=("Segoe UI", 9)).pack(anchor="w", pady=(10,0))
        self.q_remaining_var = tk.StringVar(value=str(MAX_PREGUNTAS))
        tk.Label(center, textvariable=self.q_remaining_var, font=("Segoe UI", 12, "bold"), fg="blue").pack(anchor="w")

        # Controles a la derecha
        tk.Label(right, text="Controles", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        tk.Button(right, text="Iniciar juego", width=20, command=self.start_game).pack(pady=6)
        tk.Button(right, text="Siguiente pregunta", width=20, command=self.next_question).pack(pady=6)
        tk.Button(right, text="Mostrar candidatos", width=20, command=self.show_candidates).pack(pady=6)
        tk.Button(right, text="Intentar adivinar", width=20, command=self.try_guess).pack(pady=6)
        tk.Button(right, text="Enseñar artista", width=20, command=self.learn_artist).pack(pady=6)
        tk.Button(right, text="Reiniciar", width=20, command=self.start_game).pack(pady=6)
        tk.Button(right, text="Salir", width=20, command=master.quit).pack(side=tk.BOTTOM, pady=12)

        # Estado interno
        self.current_question = None
        self.hechos = {}
        self.preguntas_respondidas = 0
        self.preguntas_list = []
        self.preguntas_usadas = set()

    # helpers historial
    def _append(self, text):
        self.history.configure(state="normal")
        self.history.insert(tk.END, text + "\n")
        self.history.see(tk.END)
        self.history.configure(state="disabled")

    def _set_question_text(self, text):
        self.q_label.configure(text=text)

    # nuevo helper: intento automático final
    def _final_guess_auto(self):
        candidatos = juego.inferencia(self.hechos)
        if not candidatos:
            # No hay candidatos: ofrecer aprender
            self._append("No se encontraron candidatos al final. Puedes enseñar un nuevo artista.")
            if messagebox.askyesno("Aprender", "No pude averiguar. ¿Deseas enseñarme el artista correcto ahora?", parent=self.master):
                self.learn_artist()
            return

        # intentar adivinar con el primer candidato
        candidato = candidatos[0]
        self._append(f"Intento final: creo que es {candidato}")
        if messagebox.askyesno("Adivinar (final)", f"Creo que el artista es: {candidato}\n¿Es correcto?", parent=self.master):
            messagebox.showinfo("Acertado", "¡He adivinado correctamente!", parent=self.master)
            self.enable_answer_buttons(False)
            return
        else:
            # si falla, mostrar lista y ofrecer aprender
            self._append(f"No acerté con {candidato}.")
            if messagebox.askyesno("No acerté", "No acerté. ¿Deseas enseñarme el artista correcto ahora?", parent=self.master):
                self.learn_artist()

    # iniciar juego
    def start_game(self):
        self._append("=== Nuevo juego iniciado ===")
        self.hechos = {}
        self.preguntas_respondidas = 0
        self.preguntas_list = juego.caracteristicas_generales + juego.caracteristicas_personales
        self.preguntas_usadas = set()
        self.q_remaining_var.set(str(MAX_PREGUNTAS - self.preguntas_respondidas))
        self.enable_answer_buttons(True)
        self.next_question()

    def enable_answer_buttons(self, enable: bool):
        state = "normal" if enable else "disabled"
        self.btn_si.configure(state=state)
        self.btn_no.configure(state=state)
        self.btn_ns.configure(state=state)

    def next_question(self):
        # elige próxima pregunta no usada
        pendiente = [c for c in self.preguntas_list if c["pregunta"] not in self.preguntas_usadas]
        if not pendiente:
            self._append("No quedan preguntas nuevas. Intentaré adivinar ahora.")
            self._set_question_text("No hay más preguntas disponibles.")
            self.enable_answer_buttons(False)
            # intentar adivinar automáticamente al quedarse sin preguntas
            self._final_guess_auto()
            return
        pregunta = pendiente[0]
        self.current_question = pregunta
        self._set_question_text(pregunta["pregunta"])
        self._append(f"Pregunta mostrada: {pregunta['pregunta']} (esperando respuesta)")

    def _answer(self, resp):
        if not self.current_question:
            self._append("No hay pregunta seleccionada. Pulsa 'Siguiente pregunta'.")
            return
        qtxt = self.current_question["pregunta"]
        self.hechos[qtxt] = resp
        self.preguntas_usadas.add(qtxt)
        self.preguntas_respondidas += 1
        remaining = max(0, MAX_PREGUNTAS - self.preguntas_respondidas)
        self.q_remaining_var.set(str(remaining))
        self._append(f"R: {qtxt} -> {resp}")
        # inferencia
        candidatos = juego.inferencia(self.hechos)
        self._append(f"Candidatos ({len(candidatos)}): {', '.join(candidatos[:10])}{'...' if len(candidatos)>10 else ''}")
        # Si queda uno, preguntar confirmación
        if len(candidatos) == 1:
            candidato = candidatos[0]
            self._append(f"Creo que es: {candidato}")
            if messagebox.askyesno("Confirmar", f"¿El artista es {candidato}?", parent=self.master):
                messagebox.showinfo("Acertado", "¡He adivinado correctamente!", parent=self.master)
                self.enable_answer_buttons(False)
                return
            else:
                self._append("No acerté — continúa o enséñame al final.")
        # Si se agotaron preguntas
        if self.preguntas_respondidas >= MAX_PREGUNTAS:
            self._append("Se completó el número máximo de preguntas. Intentaré adivinar ahora.")
            self.enable_answer_buttons(False)
            # intento automático al terminar el turno
            self._final_guess_auto()
            return
        # preparar siguiente pregunta automáticamente
        self.next_question()

    def show_candidates(self):
        candidatos = juego.inferencia(self.hechos)
        if not candidatos:
            messagebox.showinfo("Candidatos", "No hay candidatos calculados aún.", parent=self.master)
            return
        # mostrar en modal centrado por parent
        messagebox.showinfo("Candidatos", f"Candidatos ({len(candidatos)}):\n" + "\n".join(candidatos), parent=self.master)

    def try_guess(self):
        guess = simpledialog.askstring("Adivinar", "Escribe el nombre del artista:", parent=self.master)
        if not guess:
            return
        guess = guess.strip()
        candidatos = juego.inferencia(self.hechos)
        self._append(f"Intento de adivinanza: {guess}")
        if any(guess.casefold() == c.casefold() for c in candidatos):
            messagebox.showinfo("Correcto", "Tu adivinanza coincide con los candidatos.", parent=self.master)
        else:
            messagebox.showinfo("Incorrecto", "No acertaste. Puedes enseñarme el artista correcto.", parent=self.master)

    def learn_artist(self):
        """Aprende un artista usando las respuestas ya dadas en la sesión.
        Guarda automáticamente las respuestas existentes y solo pregunta las faltantes
        (o las marca como 'nose' si el usuario no quiere completarlas)."""
        nuevo = simpledialog.askstring("Aprender", "Nombre del artista a agregar:", parent=self.master)
        if not nuevo:
            return
        nuevo = nuevo.strip()

        # usar respuestas ya dadas en la sesión si existen
        inferencias = {}
        if getattr(self, "hechos", None):
            for k, v in self.hechos.items():
                val = (v or "nose").strip().lower()
                inferencias[k] = val if val in ("si", "no", "nose") else "nose"

        # preguntas totales y faltantes
        todas_preguntas = [c["pregunta"] for c in (juego.caracteristicas_generales + juego.caracteristicas_personales)]
        faltantes = [q for q in todas_preguntas if q not in inferencias]

        if faltantes:
            completar = messagebox.askyesno(
                "Completar respuestas",
                f"Se guardarán {len(inferencias)} respuestas ya respondidas.\n"
                f"¿Deseas completar las {len(faltantes)} preguntas restantes ahora?",
                parent=self.master
            )
            if completar:
                for q in faltantes:
                    r = simpledialog.askstring("Aprender - completar", f"{q} (si/no/nose) para {nuevo}:", parent=self.master)
                    if r is None:
                        r = "nose"
                    r = r.strip().lower()
                    if r not in ("si", "no", "nose"):
                        r = "nose"
                    inferencias[q] = r
            else:
                for q in faltantes:
                    inferencias[q] = "nose"

        # actualizar estructuras globales según inferencias
        for c in (juego.caracteristicas_generales + juego.caracteristicas_personales):
            resp = inferencias.get(c["pregunta"], "nose")
            if resp == "si":
                if nuevo not in c.get("si", []):
                    c.setdefault("si", []).append(nuevo)
            elif resp == "no":
                if nuevo not in c.get("no", []):
                    c.setdefault("no", []).append(nuevo)

        # agregar a listas globales
        if nuevo not in juego.artistas:
            juego.artistas.append(nuevo)
        juego.artistas_nuevos[nuevo] = inferencias

        self._append(f"Aprendido: {nuevo} (guardadas {len(inferencias)} respuestas)")
        messagebox.showinfo("Aprendido", f"Se agregó/actualizó artista: {nuevo}", parent=self.master)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArtistGuessingGame(root)
    root.mainloop()