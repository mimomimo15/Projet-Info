def calculer_coordonnees_clou(A, B, C, D, E):
    pt_0 = (-B/2, C/2)
    pt_1 = (-B/2, -C/2)
    pt_2 = (-B/2 -D, -A/2)
    pt_3 = (-B/2 - D, A/2)

    pk_0 = (B/2 + E, 0)
    pk_1 = (B/2, -C/2)
    pk_2 = (B/2, C/2)
    liste_point = [
        ('pt_0', pt_0),
        ('pt_1', pt_1),
        ('pt_2', pt_2),
        ('pt_3', pt_3),
        ('pk_2', pk_2),
        ('pk_0', pk_0),
        ('pk_1', pk_1)
    ]

    return liste_point

def appliquer_transormation_clou(liste, center_rotation, angle_rotation, angle_inclinaison, direction, axe_reflexion):




