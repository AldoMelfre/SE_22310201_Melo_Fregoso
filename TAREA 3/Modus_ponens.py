def modus_ponens(P, Q):
    if P:
        return Q
    else:
        return None  # No se puede inferir

comer = input("¿Ya comiste? (si/no): ").strip().lower() == 'si'
agua = input("¿Ya bebiste agua? (si/no): ").strip().lower() == 'si'

resultado_hambre = modus_ponens(comer, False)  # Si comió, no tiene hambre
resultado_sed = modus_ponens(agua, False)      # Si bebió agua, no tiene sed

# Mostrar resultado real si no se puede inferir
print(f"Tengo hambre: {'No' if resultado_hambre is False else 'Sí'}; Tengo sed: {'No' if resultado_sed is False else 'Sí'}")

