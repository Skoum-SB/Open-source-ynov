
import sys
import time

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

def afficher_barre_progression(iteration, total, longueur=50):
    """Affiche une barre de progression dans le terminal."""
    pourcentage = iteration / total
    barre_complete = int(longueur * pourcentage)
    barre = '█' * barre_complete + '░' * (longueur - barre_complete)
    sys.stdout.write(f"\r[{barre}] {int(pourcentage * 100)}% ({iteration}/{total})")
    sys.stdout.flush()


def generer_et_ecrire_n_premiers(n, nom_fichier="nombres_premiers.txt"):
    """Génère les n premiers nombres premiers et les écrit dans un fichier au fur et à mesure."""
    with open(nom_fichier, 'w') as fichier:
        nombre = 2
        compteur = 0
        derniere_mise_a_jour = time.time()
        
        print(f"Calcul et écriture des {n} premiers nombres premiers:")
        afficher_barre_progression(0, n)
        
        while compteur < n:
            if est_premier(nombre):
                fichier.write(str(nombre) + '\n')
                compteur += 1
                
                # Mettre à jour la barre de progression tous les 0.1 secondes pour éviter de ralentir le programme
                maintenant = time.time()
                if maintenant - derniere_mise_a_jour > 0.1 or compteur == n:
                    afficher_barre_progression(compteur, n)
                    derniere_mise_a_jour = maintenant
                    
            nombre += 1
        
        print()  # Saut de ligne après la barre de progression
        print(f"Les {n} nombres premiers ont été écrits dans {nom_fichier}")

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
            generer_et_ecrire_n_premiers(n, nom_fichier)
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
            generer_et_ecrire_n_premiers(n, nom_fichier)
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
                generer_et_ecrire_n_premiers(n, nom_fichier)
        

    except ValueError:
        print("Erreur : veuillez entrer un entier valide.")
        return

    if n <= 0:
        print("Erreur : le nombre doit être positif.")
        return

    nom_fichier = sys.argv[2] if len(sys.argv) >= 3 else "nombres_premiers.txt"

print("test")
if __name__ == "__main__":
    main()
