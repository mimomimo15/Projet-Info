from manupulation_histogramme import *
def test_calculer_histogramme():

    tableau = [[255, 160, 10, 49],
               [20, 170, 1, 121],
               [30, 233, 230, 100],
               [255, 23, 155, 88]]

    tableau_attendu = [[4, 0, 2, 3],
                       [3, 2, 2, 2],
                       [4, 0, 2, 3],
                       [2, 3, 2, 2]]

    assert np.array_equal(calculer_histogramme(tableau, 3), tableau_attendu)

def test_calculer_distance1():

    h1 = [1, 2, 3, 4, 5]
    h2 = [2, 3, 4, 5, 6]

    assert calculer_distance_1(h1, h2) == 2.24

def test_calculer_distance2():

    h1 = [1, 2, 3, 4, 5]
    h2 = [2, 3, 4, 5, 6]

    assert calculer_distance_2(h1, h2) == 5
