def appliquer_rgb_to_gry(chemin_image_couleur,chemin_sauvegarde_gris):

    img_gris = []
    with open(chemin_image_couleur,'r') as img_couleur:
        str_couleur = img_couleur.read()
        # calcul le niveaux de gris pour chaque pixel
        for i in range(len(str_couleur)):
            for j in range(len(str_couleur[0])):
                r = str_couleur[j]
                g = str_couleur[j+1]
                b = str_couleur[j+2]
                niveau_gris = (r+g+b) // 3
                img_gris[i][j] = niveau_gris
                #Reset la moyenne
                moyenne = 0
    with open(chemin_sauvegarde_gris, 'w') as image_grise:
        image_grise.write(img_gris)











