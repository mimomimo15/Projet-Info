from PIL import Image
import numpy as np
def appliquer_rgb_to_gry(chemin_image_couleur,chemin_sauvegarde_gris):

    img_gris = []
    with open(chemin_image_couleur,'r') as img_couleur:
        str_couleur = img_couleur.read()

        # calcul le niveaux de gris pour chaque pixel
        for i in range(len(str_couleur)):
                r, g, b = str_couleur[i][0], str_couleur[i][1], str_couleur[i][2]
                niveau_gris = (r+g+b) // 3
                img_gris.append(niveau_gris)
                #Reset la moyenne
                moyenne = 0
    with open(chemin_sauvegarde_gris, 'w') as image_grise:
        image_grise.write(img_gris)

def appliquer_transformation_1(tab_gris):

    tab_trans = np.zeros(shape = (len(tab_gris), len(tab_gris[0])))
    print(tab_gris)



    # i et x == lignes
    # j et y == colonne
    for i in range(1, len(tab_gris)-1):
        for j in range(1, len(tab_gris[0])-1):
            gc = tab_gris[i][j]
            print(gc)
            binaire = []
            res = 0

            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if (x, y) != (i, j):
                        gv = tab_gris[x][y]
                        if gv-gc >= 0:
                            binaire.append(1)
                        else:
                            binaire.append(0)
            print(binaire)


            for r in range(len(binaire)):
                res += binaire[r] * (2**r)
            tab_trans[i][j] = res

    # Mettre les colones et range exterieur a 0
    tab_trans[0, :] = 0
    tab_trans[-1, :] = 0
    tab_trans[:, 0] = 0
    tab_trans[:, -1] = 0

    print(tab_trans)

    return tab_trans



