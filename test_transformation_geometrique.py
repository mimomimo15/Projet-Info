from transformation_geometrique import *

def test_transformation_geometrique_1():
    assert calculer_reflexion_point((2,4),'x') == (2,-4)

def test_transformation_geometrique_2():
    assert calculer_reflexion_point((2,4),'y') == (-2,4)

def test_calculer_rotate_point():
    assert calculer_rotate_point((2,4), 30, (3,3)) == (1.63, 3.37)

def test_calculer_inclinaison_point_1():
    assert calculer_inclinaison_point((2,4), 5, 'x') == (2.35,4.0)

def test_calculer_inclinaison_point_2():
    assert calculer_inclinaison_point((2,4), 5, 'y') == (2.0,4.17)