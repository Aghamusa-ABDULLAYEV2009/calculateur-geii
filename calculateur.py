import math

def afficher_menu():
    print("\n=== CALCULATEUR GEII / SCIENTIFIQUE ===")
    print("1. Loi d'Ohm (U = I * R)")
    print("2. Puissance électrique (P = U * I)")
    print("3. Racine carrée")
    print("4. Quitter")

while True:
    afficher_menu()
    choix = input("Choisissez une option (1-4) : ")

    if choix == "1":
        i = float(input("Intensité I (en A) : "))
        r = float(input("Résistance R (en Ohms) : "))
        print(f"-> Tension U = {i * r} V")

    elif choix == "2":
        u = float(input("Tension U (en V) : "))
        i = float(input("Intensité I (en A) : "))
        print(f"-> Tension p = {u * i} W")

    elif choix == "3":
        nbr = float(input("Nombre : "))
        print(f"-> Racine carrée = {math.sqrt(nbr)}")

    elif choix == "4":
        print("Au revoir !")
        break
    else:
        print("Option invalide, réessayez.")
        
