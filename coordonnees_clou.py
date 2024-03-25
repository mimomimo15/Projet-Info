from transformation_geometrique import *

def calculer_coordonnees_clou(A, B, C, D, E):
    pt_0 = (-B/2, C/2)
    pt_1 = (-B/2, -C/2)
    pt_2 = (-B/2 -D, -A/2)
    pt_3 = (-B/2 - D, A/2)

    pk_0 = (B/2 + E, 0)
    pk_1 = (B/2, -C/2)
    pk_2 = (B/2, C/2)
    list = [
        ('pt_0', pt_0),
        ('pt_1', pt_1),
        ('pt_2', pt_2),
        ('pt_3', pt_3),
        ('pk_2', pk_2),
        ('pk_0', pk_0),
        ('pk_1', pk_1)
    ]

    return list

def appliquer_transormation_clou(liste, center_rotation, angle_rotation, direction, angle_inclinaison, axe_reflexion):
    liste_reflexion = []
    liste_rotate = []
    liste_inclinaison = []

    for i in range(len(liste)):
        liste_reflexion.append(calculer_reflexion_point(liste[i][1], axe_reflexion))
        liste_rotate.append(calculer_rotate_point(liste[i][1], angle_rotation, center_rotation))
        liste_inclinaison.append(calculer_inclinaison_point(liste[i][1], angle_inclinaison, direction))

    return liste_reflexion, liste_rotate, liste_inclinaison
