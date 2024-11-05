from my_package import my_module

def test_top_n():
    assert my_module.top_n([7, 3, 4, 2, 1, 9, 8], 3) == [9, 8, 7], "incorrect"
    assert my_module.top_n([3, 2, 9, 7, 4], 2) == [9, 7], "incorrect"