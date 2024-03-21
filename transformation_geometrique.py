from math import sin,cos,tan,pi
def calculer_reflexion_point(point, axe):

    if axe == 'y':
        point_r = [point[0], point[1]]
        point_r[0] *= -1
        return tuple(point_r)

    # Si l'axe est X
    point_r = [point[0], point[1]]
    point_r[1] *= -1
    return tuple(point_r)

def calculer_rotate_point(point, angle, centre):

    angle_rad = angle * pi / 180

    if centre[0] == 0 and centre[1] == 0:
        xp = cos(angle_rad) * point[0] - sin(angle_rad) * point[1]
        yp = sin(angle_rad) * point[0] + cos(angle_rad) * point[1]
        xp = round(xp, 2)
        yp = round(yp, 2)
        return xp, yp

    else:
        #Transaltion du centre vers l'origine
        tx = 0 - centre[0]
        ty = 0 - centre[1]
        point_prime = [point[0]+tx,point[1]+ty]

        #Rotation par rappoprt a l'origine
        xp = cos(angle_rad) * point_prime[0] - sin(angle_rad) * point_prime[1]
        yp = sin(angle_rad) * point_prime[0] + cos(angle_rad) * point_prime[1]
        xp = round(xp, 2)
        yp = round(yp, 2)

        #Annuler la translation de depart et trouver le point final
        x_rotated = xp-tx
        y_rotated = yp-ty

        return x_rotated, y_rotated

def calculer_inclinaison_point(point, angle, direction):
    angle_rad = angle * pi / 180
    m = tan(angle_rad)
    y = point[1]
    x = point[0]

    if direction == "x":
        xp = round(x + m*y,2)
        return xp, y

    yp = round(m*x + y,2)
    return x, yp

