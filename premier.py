import sys
import math
import concurrent.futures
import os
import argparse
import logging
import heapq

# Configuration du logging pour un contrôle fin de la sortie console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


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


def calculer_premiers_mt(n, max_workers=None, chunk_size=10000):
    """Génère les n premiers nombres premiers en parallèle en maintenant un tas limité."""
    if n <= 0:
        return []
    # Estimation de la borne supérieure pour le n-ième premier
    if n < 6:
        borne = 15
    else:
        borne = int(n * (math.log(n) + math.log(math.log(n)))) + 3

    workers = max_workers or os.cpu_count()
    logging.info(f"Slay queen, on utilise {workers} processus pour le calcul...")

    # Utilisation d'un max-heap (avec valeurs négatives) de taille limitée à n
    heap = []  # contiendra les -nombre premier

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        try:
            for start in range(2, borne + 1, chunk_size):
                # Réinitialiser futures à chaque lot pour éviter fuite mémoire
                futures = {}
                end = min(start + chunk_size, borne + 1)
                # Soumission des tâches pour ce lot
                for num in range(start, end):
                    futures[executor.submit(est_premier, num)] = num

                # Traitement des résultats du lot
                for futur in concurrent.futures.as_completed(futures):
                    num = futures[futur]
                    try:
                        if futur.result():
                            neg = -num
                            if len(heap) < n:
                                heapq.heappush(heap, neg)
                            elif neg > heap[0]:
                                heapq.heapreplace(heap, neg)
                            # Arrêt rapide si on a déjà n plus petits
                            if len(heap) == n and -heap[0] <= num:
                                # Lever une exception pour sortir du contexte en toute sécurité
                                raise StopIteration
                    except Exception as exc:
                        if isinstance(exc, StopIteration):
                            # Reconstruction et retour des premiers trouvés
                            result = sorted(-x for x in heap)
                            return result
                        logging.error(f"Erreur pour le nombre {num}: {exc}")
        except StopIteration:
            # Capturé ici si on interrompt prématurément
            result = sorted(-x for x in heap)
            return result
        except Exception as exc:
            logging.error(f"Erreur durant le calcul multithread: {exc}")

    # Si tous les candidats traités
    result = sorted(-x for x in heap)
    return result


def ecrire_dans_fichier(premiers, nom_fichier="nombres_premiers.txt"):  
    """Écrit les nombres premiers dans un fichier texte."""
    try:
        with open(nom_fichier, 'w') as fichier:
            for nombre in premiers:
                fichier.write(str(nombre) + '\n')
        logging.info(f"Les {len(premiers)} nombres premiers ont été écrits dans {nom_fichier}")
    except IOError as e:
        logging.error(f"Impossible d'écrire dans le fichier {nom_fichier}: {e}")


def positive_int(value):
    """Type argparse: entier strictement positif."""
    ivalue = int(value)
    if ivalue < 1:
        raise argparse.ArgumentTypeError(f"'{value}' n'est pas un entier >= 1")
    return ivalue


def main():
    parser = argparse.ArgumentParser(
        description="Calcule les n premiers nombres premiers en parallèle.")
    parser.add_argument(
        'n', type=positive_int,
        help="Nombre de premiers nombres premiers à générer (doit être un entier >= 1)")
    parser.add_argument(
        '-w', '--workers', type=positive_int,
        default=os.cpu_count(),
        help="Nombre de processus à utiliser (défaut: nombre de CPU disponibles, doit être >= 1)")
    parser.add_argument(
        '-o', '--output', type=str,
        default="nombres_premiers.txt",
        help="Nom du fichier de sortie (défaut: nombres_premiers.txt)")
    parser.add_argument(
        '--chunk', type=positive_int,
        default=10000,
        help="Taille du lot pour la soumission des tâches (défaut: 10000, doit être >= 1)")
    args = parser.parse_args()

    logging.info(f"Calcul des {args.n} premiers nombres premiers en cours...")
    premiers = calculer_premiers_mt(
        args.n, max_workers=args.workers, chunk_size=args.chunk
    )
    ecrire_dans_fichier(premiers, args.output)


if __name__ == "__main__":
    main()
