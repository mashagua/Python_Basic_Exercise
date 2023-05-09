from project import divide_two_numbers
def test_divide_two_numbers_method():
    exceptd_data_type=(int,float)
    assert type(divide_two_numbers(4,20)) in exceptd_data_type
    assert type(divide_two_numbers(5, 0)) in exceptd_data_type
