import shapes


def test_areaRec():
    x=5
    y=7
    result=shapes.rectangle(x,y)
    assert x*y==result

def test_periRec():
    x=5
    y=8
    result=shapes.perimeter(x,y)
    assert x+x+y+y==result

def test_areaSquare():
    x=8
    result=shapes.square(x)
    assert x*x==result