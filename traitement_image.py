from PIL import Image
import numpy as np
from math import log10

#  ____________CORRIGER LES TABLEAUX LES UTILISER ET RETOURNER EN NUMPY__________________

def appliquer_rgb_to_gry(chemin_image_couleur, chemin_sauvegarde_gris):

    imcolor = Image.open(chemin_image_couleur)
    width_x = imcolor.size[0]
    width_y = imcolor.size[1]
    pixel = imcolor.load()
    for i in range(width_x):
        for j in range(width_y):
            rgb_value = pixel[i, j]
            r = rgb_value[0]
            g = rgb_value[1]
            b = rgb_value[2]
            average = (r + g + b) / 3
            pixel[i, j] = (int(average), int(average), int(average))

    imcolor.save(chemin_sauvegarde_gris)
def appliquer_transformation_1(tab_gris):

    #Création du tableau transformé de dimensions identique au tableau recus
    tab_trans = np.zeros(shape = (len(tab_gris), len(tab_gris[0])))
    # La première boucle positionne le gc
    for i in range(1, len(tab_gris)-1):
        for j in range(1, len(tab_gris[0])-1):
            gc = tab_gris[i][j]

            # Énumeration et création du tableau des voisins du centre afin qu'ils soit dans le bon ordre
            v0 = tab_gris[i-1][j-1]
            v1 = tab_gris[i-1][j]
            v2 = tab_gris[i-1][j+1]
            v3 = tab_gris[i][j+1]
            v4 = tab_gris[i+1][j+1]
            v5 = tab_gris[i+1][j]
            v6 = tab_gris[i+1][j-1]
            v7 = tab_gris[i][j-1]
            #le tableau de voisin represente le parcours que doit faire la boucle, (matrice 3x3 sans le centre)
            tab_voisin = [v0, v1, v2, v3, v4, v5, v6, v7]
            # Initialisation des données nécéssaire dans la prochaine boucle
            binaire = []
            res = 0
            multi = 0

            # Boucle qui parcours le tableau de voisin et qui crée ensuite le nombre binaire correspondant au centre
            for x in range(len(tab_voisin)):
                if tab_voisin[x] >= gc:
                    binaire.append(1)
                else:
                    binaire.append(0)
            #Boucle qui parcour la liste binaire à l'envers pour ensuite le transformer en décimal
            for y in range(len(binaire)-1, -1, -1):
                res += binaire[y] * (2**multi)
                multi += 1

            # intergrer les nombres décimal calculé dans le tableaux transformé
            tab_trans[i][j] = res


    # Mettre les colones et range exterieur a 0
    tab_trans[0, :] = 0
    tab_trans[-1, :] = 0
    tab_trans[:, 0] = 0
    tab_trans[:, -1] = 0

    return tab_trans

def appliquer_transformation_2(tab_gris, r):

    # Création du tableau transformé de dimensions identique au tableau recus
    tab_trans = np.zeros(shape=(len(tab_gris), len(tab_gris[0])))

    # La première boucle positionne I(x,y)
    for x in range(r, len(tab_gris) - r):
        for y in range(r, len(tab_gris[0]) - r):

            #Calcul des valeurs intermediaires
            v1 = 1 + np.abs(tab_gris[x][y + r] - 2 * tab_gris[x][y] + tab_gris[x][y-r])
            v2 = 1 + np.abs(tab_gris[x+r][y] - 2 * tab_gris[x][y] + tab_gris[x-r][y])
            v3 = 1 + np.abs(tab_gris[x-r][y+r] - 2 * tab_gris[x][y] + tab_gris[x+r][y-r])

            #Calcul de la valeur final et le // 1 sert a garder seulement l'entier
            o_xy = (np.log10(v1) + np.log10(v2) + np.log10(v3))//1
            tab_trans[x][y] = o_xy

    # Mettre les colones et range exterieur a 0
    tab_trans[0, :] = 0
    tab_trans[-1, :] = 0
    tab_trans[:, 0] = 0
    tab_trans[:, -1] = 0

    return tab_trans







