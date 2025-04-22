import sys

def est_premier(nombre):
    """Vérifie si un nombre est premier."""
    if nombre <= 1:
        return False
    if nombre <= 3:
        return True
    if nombre % 2 == 0 or nombre % 3 == 0:
        return False
    i = 5
    while i * i <= nombre:
        if nombre % i == 0 or nombre % (i + 2) == 0:
            return False
        i += 6
    return True

def generer_n_premiers(n):
    """Génère les n premiers nombres premiers."""
    premiers = []
    nombre = 2
    while len(premiers) < n:
        if est_premier(nombre):
            premiers.append(nombre)
        nombre += 1
    return premiers

def ecrire_dans_fichier(premiers, nom_fichier="nombres_premiers.txt"):
    """Écrit les nombres premiers dans un fichier texte."""
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        for nombre in premiers:
            fichier.write(f"{nombre}\n")
    print(f"Les {len(premiers)} nombres premiers ont été écrits dans {nom_fichier}")

def afficher_animal(nombre):
    """Affiche 'girage' si nombre est entre 1 et 10 inclus, sinon 'loutre'."""
    if 1 <= nombre <= 10:
        print("girage")
    else:
        print("loutre")

def main():
    # Vérifier le nombre d'arguments
    if len(sys.argv) < 2:
        print("Usage : python premier.py <nombre_de_premiers> [nom_du_fichier]")
        return

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Erreur : veuillez entrer un entier valide.")
        return

    if n <= 0:
        print("Erreur : le nombre doit être positif.")
        return

    nom_fichier = sys.argv[2] if len(sys.argv) >= 3 else "nombres_premiers.txt"

    # Calcul et sortie
    print(f"Calcul des {n} premiers nombres premiers…")
    premiers = generer_n_premiers(n)
    ecrire_dans_fichier(premiers, nom_fichier)

    # Affichage des "animaux"
    print("\nRésultat de afficher_animal pour chaque nombre :")
    for p in premiers:
        afficher_animal(p)

if __name__ == "__main__":
    main()
