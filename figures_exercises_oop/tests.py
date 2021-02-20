from python_intermediate.figures_exercises_oop.figures_entities import Circle, Triangle, Rectangle


def test_check_area():
    #  given
    circle = Circle(1)
    # circle2 = Circle(8)

    triangle = Triangle(2, 1)
    # triangle2 = Triangle(12, 3)

    rectangle = Rectangle(2, 2)
    # rectangle2 = Rectangle(4, 6)

    #  when
    result = Figre.count_area([circle, triangle, rectangle])

    #  then
    assert result == 8.142

def test_compare_area():
    #  given
    circle = Circle(1)
    triangle = Triangle(2, 1)
    rectangle = Rectangle(2, 2)