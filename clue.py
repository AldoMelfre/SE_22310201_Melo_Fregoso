import random
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# Juego jugable tipo "Clue" simplificado con menús y GUI:
# - Selecciono secretamente (culpable, locación, item)
# - Tú preguntas (máx 8) usando botones GUI: Personaje / Escenario / Item
# - Cada respuesta da hechos observados y pistas inferidas (MP simple)
# - Puedes intentar adivinar en cualquier momento
# - Interfaz Tkinter añadida

suspects = {
    "Ada": "Programador",
    "Bruno": "Diseñador UX",
    "Carla": "Mentor",
    "Diego": "Jurado",
    "Elena": "Soporte TI"
}

rooms = ["Laboratorio", "Auditorio", "Sala de servidores", "Biblioteca", "Cafetería 24/7"]

objects = ["Laptop clonada", "Token perdido", "USB", "Adaptador HDMI", "Protoboard"]

MAX_PREGUNTAS = 8

def elegir_secreto():
    culp = random.choice(list(suspects.keys()))
    loc = random.choice(rooms)
    obj = random.choice(objects)
    return culp, loc, obj

def construir_mundo(secreto):
    culp, loc, obj = secreto
    mundo = {
        "suspect_locations": {},
        "item_locations": {},
        "suspect_items": {},
        "observations": []
    }
    mundo["suspect_locations"][culp] = loc
    mundo["item_locations"][obj] = loc
    mundo["suspect_items"][culp] = [obj]

    otros = [s for s in suspects.keys() if s != culp]
    vistos = random.sample(otros, k=2)
    salas_disponibles = [r for r in rooms if r != loc]
    for s in vistos:
        sala = random.choice(salas_disponibles)
        mundo["suspect_locations"][s] = sala
        it = random.choice([o for o in objects if o != obj])
        mundo["suspect_items"][s] = [it]
        mundo["item_locations"][it] = sala

    for o in objects:
        if o not in mundo["item_locations"]:
            r = random.choice(rooms)
            mundo["item_locations"][o] = r

    mundo["observations"].append(f"Se encontró '{obj}' en {loc}.")
    mundo["observations"].append(f"Se vio a {culp} en {loc}.")
    for s in vistos:
        mundo["observations"].append(f"Se vio a {s} en {mundo['suspect_locations'][s]}.")
    return mundo

def pista_inferida(mundo):
    candid = set()
    fuerte = set()
    critico = "Token perdido"
    if critico in mundo["item_locations"]:
        loc_token = mundo["item_locations"][critico]
        for s, r in mundo["suspect_locations"].items():
            if r == loc_token:
                candid.add(s)
    for s, items in mundo["suspect_items"].items():
        if any(it == critico for it in items):
            fuerte.add(s)
    return sorted(fuerte), sorted(candid)

# ---------- GUI ----------

class SelectionDialog(tk.Toplevel):
    def __init__(self, parent, title, options):
        super().__init__(parent)
        self.title(title)
        self.resizable(False, False)
        self.selected = None
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self.listbox = tk.Listbox(self, width=40, height=min(10, len(options)))
        for opt in options:
            self.listbox.insert(tk.END, opt)
        self.listbox.pack(padx=10, pady=(10, 5))

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=(0,10))
        ok = tk.Button(btn_frame, text="OK", width=10, command=self._on_ok)
        ok.pack(side=tk.LEFT, padx=5)
        cancel = tk.Button(btn_frame, text="Cancelar", width=10, command=self._on_close)
        cancel.pack(side=tk.LEFT, padx=5)

        # center
        self.transient(parent)
        self.grab_set()
        self.listbox.focus_set()
        self.wait_window(self)

    def _on_ok(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Selecciona", "Selecciona una opción antes de confirmar.")
            return
        self.selected = self.listbox.get(sel[0])
        self.destroy()

    def _on_close(self):
        self.selected = None
        self.destroy()

class ClueGUI:
    def __init__(self, root):
        self.root = root
        root.title("Clue - Token Perdido (Interfaz)")
        root.geometry("820x520")

        self._build_widgets()
        self.reset_case()

    def _build_widgets(self):
        left = tk.Frame(self.root, padx=8, pady=8)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        right = tk.Frame(self.root, padx=8, pady=8)
        right.pack(side=tk.RIGHT, fill=tk.Y)

        lbl = tk.Label(left, text="Observaciones y pistas (historial):", font=("Segoe UI", 10, "bold"))
        lbl.pack(anchor="w")

        self.history = tk.Text(left, width=60, height=28, state="disabled", wrap="word")
        self.history.pack(fill=tk.BOTH, expand=True)

        # right controls
        tk.Label(right, text="Acciones", font=("Segoe UI", 10, "bold")).pack(anchor="w")

        self.q_count_var = tk.StringVar()
        self.q_count_var.set(f"Preguntas restantes: {MAX_PREGUNTAS}")
        tk.Label(right, textvariable=self.q_count_var, fg="blue").pack(anchor="w", pady=(6,4))

        btn_personaje = tk.Button(right, text="Preguntar Personaje", width=22, command=self.on_personaje)
        btn_personaje.pack(pady=4)
        btn_escenario = tk.Button(right, text="Preguntar Escenario", width=22, command=self.on_escenario)
        btn_escenario.pack(pady=4)
        btn_item = tk.Button(right, text="Preguntar Item", width=22, command=self.on_item)
        btn_item.pack(pady=4)

        tk.Label(right, text="Otras opciones", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(10,2))
        btn_infer = tk.Button(right, text="Mostrar pistas inferidas", width=22, command=self.on_infer)
        btn_infer.pack(pady=4)
        btn_guess = tk.Button(right, text="Intentar adivinar", width=22, command=self.on_guess)
        btn_guess.pack(pady=4)
        btn_restart = tk.Button(right, text="Reiniciar caso", width=22, command=self.reset_case)
        btn_restart.pack(pady=4)
        btn_quit = tk.Button(right, text="Salir", width=22, command=self.root.quit)
        btn_quit.pack(pady=20)

        self._action_buttons = [btn_personaje, btn_escenario, btn_item, btn_infer, btn_guess]

    def reset_case(self):
        self.secreto = elegir_secreto()
        self.mundo = construir_mundo(self.secreto)
        self.preguntas_restantes = MAX_PREGUNTAS
        self._update_qcount()
        self._clear_history()
        self._append_history("Nuevo caso generado (secreto aleatorio).")
        self._append_history("Observaciones iniciales:")
        for h in self.mundo["observations"]:
            self._append_history(" - " + h)
        fuerte, candid = pista_inferida(self.mundo)
        if fuerte:
            self._append_history(f"Pista inferida (inicial): fuerte candidato(s): {', '.join(fuerte)}")
        elif candid:
            self._append_history(f"Pista inferida (inicial): candidato(s) por presencia: {', '.join(candid)}")

    def _append_history(self, text):
        self.history.configure(state="normal")
        self.history.insert(tk.END, text + "\n")
        self.history.see(tk.END)
        self.history.configure(state="disabled")

    def _clear_history(self):
        self.history.configure(state="normal")
        self.history.delete(1.0, tk.END)
        self.history.configure(state="disabled")

    def _update_qcount(self):
        self.q_count_var.set(f"Preguntas restantes: {self.preguntas_restantes}")

    def _consume_question(self):
        self.preguntas_restantes -= 1
        if self.preguntas_restantes < 0:
            self.preguntas_restantes = 0
        self._update_qcount()
        if self.preguntas_restantes == 0:
            messagebox.showinfo("Preguntas agotadas", "Se agotaron las preguntas. Intenta adivinar o reinicia.")

    def on_personaje(self):
        if self.preguntas_restantes == 0:
            messagebox.showwarning("Sin preguntas", "No quedan preguntas disponibles.")
            return
        dialog = SelectionDialog(self.root, "Selecciona Personaje", list(suspects.keys()))
        sel = dialog.selected
        if not sel:
            return
        nombre = sel
        loc = self.mundo["suspect_locations"].get(nombre, "No visto")
        items = self.mundo["suspect_items"].get(nombre, [])
        self._append_history(f"Consulta personaje: {nombre}")
        self._append_history(f" - Profesión: {suspects[nombre]}")
        self._append_history(f" - Visto en: {loc}")
        if items:
            self._append_history(f" - Objetos con {nombre}: {', '.join(items)}")
        else:
            self._append_history(f" - No se observaron objetos con {nombre}")
        critico = "Token perdido"
        if critico in items:
            self._append_history("Pista: tiene o tenía el token perdido -> fuerte sospechoso.")
        elif loc != "No visto" and self.mundo["item_locations"].get(critico) == loc:
            self._append_history("Pista: estuvo en la misma locación donde se encontró el token -> candidato.")
        self._consume_question()

    def on_escenario(self):
        if self.preguntas_restantes == 0:
            messagebox.showwarning("Sin preguntas", "No quedan preguntas disponibles.")
            return
        dialog = SelectionDialog(self.root, "Selecciona Locación", rooms)
        sel = dialog.selected
        if not sel:
            return
        loc = sel
        presentes = [s for s, r in self.mundo["suspect_locations"].items() if r == loc]
        objetos = [o for o, r in self.mundo["item_locations"].items() if r == loc]
        self._append_history(f"Consulta locación: {loc}")
        self._append_history(f" - Objetos hallados: {', '.join(objetos)}")
        if presentes:
            self._append_history(f" - Personas vistas: {', '.join(presentes)}")
        else:
            self._append_history(" - No se observaron personas en esta locación")
        if "Token perdido" in objetos:
            self._append_history("Pista: El token perdido está aquí. Cualquiera visto aquí es candidato principal.")
        self._consume_question()

    def on_item(self):
        if self.preguntas_restantes == 0:
            messagebox.showwarning("Sin preguntas", "No quedan preguntas disponibles.")
            return
        dialog = SelectionDialog(self.root, "Selecciona Item", objects)
        sel = dialog.selected
        if not sel:
            return
        it = sel
        loc = self.mundo["item_locations"].get(it, "Desconocido")
        duenos = [s for s, its in self.mundo["suspect_items"].items() if it in its]
        self._append_history(f"Consulta item: {it}")
        self._append_history(f" - Hallado en: {loc}")
        if duenos:
            self._append_history(f" - Observado con: {', '.join(duenos)}")
        else:
            self._append_history(" - No se observó quién lo tenía")
        if it == "Token perdido":
            self._append_history("Pista: Este es el item crítico que impide la presentación.")
        self._consume_question()

    def on_infer(self):
        fuerte, candid = pista_inferida(self.mundo)
        self._append_history("Consulta: pistas inferidas")
        if fuerte:
            self._append_history(f" - Fuertes candidatos (posesión del token): {', '.join(fuerte)}")
        if candid:
            self._append_history(f" - Candidatos por presencia donde se encontró el token: {', '.join(candid)}")
        if not fuerte and not candid:
            self._append_history(" - No se han inferido candidatos fuertes aún")

    def on_guess(self):
        res = simpledialog.askstring("Adivinar", "Ingresa culpable, locación y item separados por '|' (ej: Ada|Laboratorio|Token perdido):", parent=self.root)
        if not res:
            return
        parts = [p.strip() for p in res.split("|")]
        if len(parts) != 3:
            messagebox.showerror("Formato inválido", "Debes ingresar tres partes separadas por '|'")
            return
        cul, loc, it = parts
        correcto = (cul.casefold(), loc.casefold(), it.casefold()) == (self.secreto[0].casefold(), self.secreto[1].casefold(), self.secreto[2].casefold())
        self._append_history(f"Intento de adivinanza: {cul} | {loc} | {it}")
        if correcto:
            messagebox.showinfo("Acertaste", "¡Correcto! Has resuelto el misterio.")
            self._append_history("Resultado: Correcto. Juego finalizado.")
        else:
            messagebox.showinfo("Incorrecto", f"No acertaste. Sigue investigando. (Aún quedan {self.preguntas_restantes} preguntas)")
            self._append_history("Resultado: Incorrecto.")

# ---------- Fin GUI ----------

if __name__ == "__main__":
    root = tk.Tk()
    app = ClueGUI(root)
    root.mainloop()