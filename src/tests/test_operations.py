from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(4,5)==9
    assert add(-2,5)==3

def test_sub():
    assert sub(4,2)==2
    assert sub(-3,5)==-8
    assert sub(4,8)==-4