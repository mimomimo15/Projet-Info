from traitement_image import *
def test_appliquer_transformation_1_a():

    tableau = np.array([
        [2, 5, 3, 9, 15],
        [6, 7, 9, 1, 5],
        [3, 8, 4, 2, 9],
        [2, 3, 5, 8, 2],
        [1, 2, 3, 2, 1]
    ])
    tableau_attendu = np.array([
        [0, 0, 0, 0, 0],
        [0, 20, 32, 255, 0],
        [0, 32, 205, 191, 0],
        [0, 248, 144, 32, 0],
        [0, 0, 0, 0, 0]
    ])

    assert np.array_equal(appliquer_transformation_1(tableau), tableau_attendu)