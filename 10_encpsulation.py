#  Python does not have function overloading in the traditional sense like some other languages (e.g., C++, Java).


class Person:
    def __init__(self, name, age, gender):
        self.__name = name  # `__name` is private
        self.__age = age
        self.__gender = gender

    @property
    def name(self):  # to print val
        return self.__name

    @name.setter  # to assign val
    def name(self, value):
        self.__name = value

    @staticmethod
    def mymethod():
        print(
            "Hello World"
        )  # no self because, it is not related to single instance/object


p1 = Person("Mike", 20, "m")
print(p1.name)

p1.name = "ABC"
print(p1.name)

Person.mymethod()
