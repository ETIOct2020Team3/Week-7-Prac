from fn import *
import pytest



# def test_div():
#     value = divide(10,2)
#     assert value == 5
# #1
# def test_over_ten_variables():
#     value = add(1,2,3,4,5,6,7,8,9,10,11, 12)
#     assert value == "Input more than 10"
# #2
# def test_div():
#     value = divide(1,2)
#     assert value == 0.5
# #3
# def test_multiply():
#     value = multiply(1,3)
#     assert value ==3
# #4
# def test_divby0():
#     value = divide(1,0)
#     assert value == "ZeroDivideError"
# #5
# def test_positive_div_negative():
#     value = divide(1,-10)
#     assert value == -0.1
# #6
# def test_add():
#     value = add(1,4)
#     assert value == 5
# #7
# def test_subtract():
#     value = subtract(1,5)
#     assert value == -4

# #9
# def test_positive_time_negative():
#     value = multiply(5,-5)
#     assert value == -25
#10
def test_zero_divothervalue():
    value = divide(0,2)
    assert value == 0
11
def test_multiply_by_zero():
    value = multiply(5,0)
    assert value == 10
