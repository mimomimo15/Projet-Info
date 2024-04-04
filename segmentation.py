import random
import numpy as np
from manupulation_histogramme import *
def regrouper_points(data, k =2, max_iterations = 50):

    ind1 = random.randint(0, len(data) - 1)
    ind2 = random.randint(0, len(data) - 1)

    centre1 = data[ind1]
    centre2 = data[ind2]

    for i in range(max_iterations):

        tab_ind = []
        groupe1 = []
        groupe2 = []

        for j in range(len(data)):
            somme1 = 0
            somme2 = 0
            distance_1 = calculer_distance_1(centre1, data[j])
            distance_2 = calculer_distance_1(centre2, data[j])

            if distance_1 > distance_2:
                groupe1.append(data[j])
                tab_ind.append(0)
            else:
                groupe2.append(data[j])
                tab_ind.append(1)

        if len(groupe1) > 0:
            for x in range(len(groupe1)):
                somme1 += groupe1[x]
            centre1 = somme1 / len(groupe1)

        if len(groupe2) > 0:
            for y in range(len(groupe2)):
                somme2 += groupe2[y]
            centre2 = somme2 / len(groupe2)

    return np.array(tab_ind)











