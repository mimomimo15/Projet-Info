from PIL import Image
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











