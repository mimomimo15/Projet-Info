from transformation_geometrique import *

def test_transformation_geometrique_1():
    assert calculer_reflexion_point((2,4),'x') == (2,-4)

def test_transformation_geometrique_2():
    assert calculer_reflexion_point((2,4),'y') == (-2,4)

def test_calculer_rotate_point():
    assert calculer_rotate_point((2,4), 30, (0,0)) == (-0.27,4.46)
