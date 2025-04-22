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
    with open(nom_fichier, 'w') as fichier:
        for nombre in premiers:
            fichier.write(str(nombre) + '\n')
    print(f"Les {len(premiers)} nombres premiers ont été écrits dans {nom_fichier}")

def main():
    try:
        # Vérifier si le script est exécuté sans arguments
        if len(sys.argv) == 1:
            # Vérifier si le nombre est positif mais redemander si ce n'est pas le cas
            n = int(input("Combien de nombres premiers voulez-vous générer ? "))
            while n <= 0:
                print("Erreur: Le nombre doit être positif.")
                n = int(input("Combien de nombres premiers voulez-vous générer ? "))
            #Puis demander le nom du fichier
            nom_fichier = input("Quel est le nom du fichier ? (par défaut 'nombres_premiers.txt') ")
            if nom_fichier == "":
                nom_fichier = "nombres_premiers.txt"
            print(f"Calcul des {n} premiers nombres premiers en cours...")
            premiers = generer_n_premiers(n)
            ecrire_dans_fichier(premiers, nom_fichier)
        elif len(sys.argv) == 2:
            # Vérifier si le nombre est positif mais redemander si ce n'est pas le cas
            n = int(sys.argv[1])
            while n <= 0:
                print("Erreur: Le nombre doit être positif.")
                n = int(input("Combien de nombres premiers voulez-vous générer ? "))
            #Puis demander le nom du fichier
            nom_fichier = input("Quel est le nom du fichier ? (par défaut 'nombres_premiers.txt') ")
            if nom_fichier == "":
                nom_fichier = "nombres_premiers.txt"
            print(f"Calcul des {n} premiers nombres premiers en cours...")
            premiers = generer_n_premiers(n)
            ecrire_dans_fichier(premiers, nom_fichier)
        elif len(sys.argv) == 3:
            # Vérifier si le nombre est positif mais redemander si ce n'est pas le cas
            n = int(sys.argv[1])
            while n <= 0:
                print("Erreur: Le nombre doit être positif.")
                n = int(input("Combien de nombres premiers voulez-vous générer ? "))
            #Vérifier que le nom du fichier est valdie (txt)
            if not sys.argv[2].endswith(".txt"):
                print("Erreur: Le nom du fichier doit se terminer par '.txt'")
                return
            # Récupère le nom du fichier depuis les arguments
            if len(sys.argv) >= 3:
                nom_fichier = sys.argv[2]
                print(f"Calcul des {n} premiers nombres premiers en cours...")
                premiers = generer_n_premiers(n)
                ecrire_dans_fichier(premiers, nom_fichier)
        
    except ValueError:
        print("Erreur: Veuillez entrer un nombre entier valide.")
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")

print("test")
if __name__ == "__main__":
    main()