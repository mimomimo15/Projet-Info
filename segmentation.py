import random
import numpy as np
from manupulation_histogramme import *
def regrouper_points(data, k =2, max_iterations =50):

    ind1 = random.randint(0, len(data) - 1)
    ind2 = random.randint(0, len(data) - 1)

    centre1 = data[ind1]
    centre2 = data[ind2]

    for i in range(max_iterations):

        tab_ind = []
        groupe1 = []
        groupe2 = []

        for i in range(len(data)):

            distance_1 = calculer_distance_1(centre1, data[i])
            distance_2 = calculer_distance_1(centre2, data[i])

            if distance_1 > distance_2:
                groupe1.append(data[i])
                tab_ind.append(1)
            else:
                groupe2.append(data[i])
                tab_ind.append(2)

                somme1 = 0
                somme2 = 0
            for j in range(len(groupe1)):

                somme1 += groupe1[j]

            if len(groupe1) > 0:
                centre_moyen_1 = somme1 / len(groupe1)

            for x in range(len(groupe2)):
                somme2 += groupe2[x]

            if len(groupe2) > 0:
                centre_moyen_2 = somme2 / len(groupe2)

            centre1 = centre_moyen_1
            centre2 = centre_moyen_2

            if centre1 == centre_moyen_1 and centre2 == centre_moyen_2:
                return tab_ind

    return tab_ind















