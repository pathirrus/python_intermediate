from python_intermediate.figures_exercises_oop.figures_entities import Circle, Triangle, Rectangle, Figure, \
    count_area_function


def main():
    circle = Circle(5)
    circle2 = Circle(8)

    triangle = Triangle(3, 7)
    triangle2 = Triangle(12, 3)

    rectangle = Rectangle(3, 3)
    rectangle2 = Rectangle(4, 6)

    print(circle.get_area(), triangle.get_area(), rectangle.get_area())

    area = Figure.count_area([circle, triangle2, rectangle2, rectangle, circle2])
    print(area)

    area = count_area_function(circle, triangle, rectangle2)
    print(area)

    check_area = Figure.check_area(100, [circle,  triangle2])
    print(check_area)
    print(Figure.count_area([circle,  triangle2]))


if __name__ == "__main__":
    main()