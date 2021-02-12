import pytest

from python_intermediate.figures_exercises_oop.figures_entities import Circle, Triangle, Rectangle, Figure


def test_check_area():
    #  given
    circle = Circle(1)
    # circle2 = Circle(8)

    triangle = Triangle(2, 1)
    # triangle2 = Triangle(12, 3)

    rectangle = Rectangle(2, 2)
    # rectangle2 = Rectangle(4, 6)

    #  when
    result = Figure.count_area([circle, triangle, rectangle])

    #  then
    assert result == 8.142


# def test_compare_area():
#     #  given
#     circle = Circle(1)
#     triangle = Triangle(2, 1)
#     rectangle = Rectangle(2, 2)
#
#     some_area_big = Figure.count_area([circle, triangle, rectangle]) + 1
#     some_area_small = Figure.count_area([circle, triangle, rectangle]) - 1
#
#     result_1 = Figure.count_area([circle, triangle, rectangle]) > some_area_small
#     result_2 = Figure.count_area([circle, triangle, rectangle]) > some_area_big
#
#     assert result_1, result_2
