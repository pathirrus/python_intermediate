from python_intermediate.car import Car
from python_intermediate.cat import Cat
from python_intermediate.dog import Dog
from python_intermediate.vet import Vet


def main():
    cat_object = Cat("Filemon")
    # sound = cat_object.make_sound()
    cat_object2 = Cat("Bonifacy", "miałmiał")
    cat_object3 = Cat("Kitek")
    cat_object4 = Cat("Mruczek", "meow")

    # list_cats = [cat_object, cat_object2, cat_object3, cat_object4]
    # for cat in list_cats:
    #     cat_sound = cat.make_sound()
    #     print(cat_sound)

    cat_object.eat_mouse()
    cat_object.eat_mouse()
    cat_object.eat_mouse()

    print("Teraz bedzie zarl drugi kot")
    cat_object3.eat_mouse()

    dog_object = Dog("Burek", "wowwow")
    dog_object1 = Dog("Ciapek", "wowwow")
    dog_object2 = Dog("Buli", "wowwow")

    print(dog_object.make_sound())

    anima_list = [cat_object4, cat_object, cat_object2, dog_object2, dog_object1]
    for animal in anima_list:
        animal_sound = animal.make_sound()
        print(animal_sound)

    car = Car()
    print(car.move())

    cat = Cat("Mudżin")
    print(cat.move())

    dog = Dog("Pieseł")

    print(Vet.say_cat_hello(cat))

    Vet.say_dog_hello(dog)

    # vet = Vet()
    # vet.say_dog_hello_hello(dog)

    vet = Vet()
    vet.say_dog_hello(dog)
    vet.say_cat_hello(cat)


if __name__ == "__main__":
    main()
