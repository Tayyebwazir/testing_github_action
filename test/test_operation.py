from src.math_operation import add, sub


def test_add():
    assert add(2,3)==5
    assert add(1,-1)==0
    
    
def text_sub():    
    assert sub(5,3)==2
    assert sub(10,3)==7
    assert sub(5,8)==-2
