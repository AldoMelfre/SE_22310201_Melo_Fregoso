# Modus Tollens: Si P entonces Q. No Q, por lo tanto no P.

def modus_tollens(P, Q):
    """
    Si P entonces Q.
    No Q, por lo tanto no P.
    Retorna True si se puede inferir no P, False en caso contrario.
    """
    if not Q:
        return True  # Se puede inferir no P
    else:
        return False

# Ejemplo: Si estudio (P), entonces paso el examen (Q)
estudio = input("¿Estudiaste para el examen? (si/no): ").strip().lower() == 'si'
paso_examen = input("¿Pasaste el examen? (si/no): ").strip().lower() == 'si'

resultado = modus_tollens(estudio, paso_examen)

if resultado:
    print("Por Modus Tollens: No estudiaste para el examen.")
else:
    print("No se puede inferir que no estudiaste para el examen.")