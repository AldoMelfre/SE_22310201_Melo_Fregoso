# Modus Ponens: Si P entonces Q. P es verdadero, por lo tanto Q es verdadero.

def modus_ponens(P, Q_implicado):
    """
    P: premisa (bool)
    Q_implicado: consecuencia si P es verdadero (bool)
    Retorna True si se puede inferir Q, False en caso contrario.
    """
    if P:
        return Q_implicado
    else:
        return False

#Solicitar datos al usuario
comer = input("Ya comiste? (si/no): ").strip().lower() == 'si'
hambre = false #si ya comio, no tiene hambre


# Ejemplo:
# Si como (P), entonces tengo hambre (Q)
comer = True
hambre = True  # Q

resultado = modus_ponens(comer, hambre)

if resultado:
    print("Por Modus Ponens: Tengo hambre.")
else:
    print("No se puede inferir que tengo hambre.")