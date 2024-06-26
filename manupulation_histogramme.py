import numpy as np
def calculer_histogramme(image, w):

    hauteur, largeur = len(image), len(image[0])
    #Initialisation du tableau qui stock les histogrammes
    tableau_hist = []
    max_val = np.max(image)

    # Premiere boucle qui bouge la pixel central
    for i in range(w//2, hauteur - w//2):
        for j in range(w//2, largeur - w//2):

            #initialisation de la fenetre
            fenetre = []
            #Deuxieme boucle qui met les valeur du tableau dans la fenetre
            for x in range(i - w//2, i + w//2 + 1):
                for y in range(j - w//2, j + w//2 + 1):
                    fenetre.append(image[x][y])

            #Fonction qui genere l'histogramme
            hist, _ = np.histogram(fenetre, bins=[0,
                                                  max_val / 4,
                                                  max_val / 2,
                                                  3 * max_val / 4,
                                                  max_val],
                                            range=(0, max_val))
            tableau_hist.append(hist)

    return tableau_hist

def calculer_distance_1(h1, h2):

    somme = 0
    for i in range(len(h1)):
        somme += (h1[i] - h2[i])**2
    return round(somme**0.5, 2)


def calculer_distance_2(h1, h2):

    somme = 0
    for i in range(len(h1)):
        somme += abs((h1[i] - h2[i]))
        round(somme, 2)
    return somme















