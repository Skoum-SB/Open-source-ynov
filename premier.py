
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


def afficher_animal(nombre):
    """Affiche 'girage' si nombre est entre 1 et 10 inclus, sinon 'loutre'."""
    if 1 <= nombre <= 10:
        print("girage")
    else:
        print("loutre")

def main():
    # Vérifier le nombre d'arguments
    if len(sys.argv) < 2:
            print("Usage: python premier.py <nombre_de_premiers> [nom_du_fichier]")
            print("Exemple: python premier.py 1000 nombres_premiers.txt")
            return
    try: 
        # Récupérer le nombre de nombres premiers depuis les arguments
        n = int(sys.argv[1])
        if n <= 0:
            print("Erreur: Le nombre doit être positif.")
            return
        
        # Récupérer le nom du fichier s'il est fourni
        nom_fichier = "nombres_premiers.txt"  # Valeur par défaut
        if len(sys.argv) >= 3:
            nom_fichier = sys.argv[2]
        
        generer_et_ecrire_n_premiers(n, nom_fichier)

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
    

    # Affichage des "animaux"
    print("\nRésultat de afficher_animal pour chaque nombre :")
    for p in premiers:
        afficher_animal(p)

if __name__ == "__main__":
    main()
