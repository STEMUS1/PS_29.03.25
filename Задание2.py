class Rectangle:
    def __init__(self, height=1, width=1):
        self.__height = height
        self.__width = width
        self.__square = self.__calculate_square()
        self.__perimeter = self.__calculate_perimeter()

    def __calculate_square(self):
        return self.__height * self.__width

    def __calculate_perimeter(self):
        return 2 * (self.__height + self.__width)

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height
        self.__update_properties()

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width
        self.__update_properties()

    def get_square(self):
        return self.__square

    def get_perimeter(self):
        return self.__perimeter

    def __update_properties(self):
        self.__square = self.__calculate_square()
        self.__perimeter = self.__calculate_perimeter()

rect = Rectangle(5, 10)
print("Высота:", rect.get_height())
print("Ширина:", rect.get_width())
print("Площадь:", rect.get_square())
print("Периметр:", rect.get_perimeter())

rect.set_height(7)
rect.set_width(3)
print("Новая высота:", rect.get_height())
print("Новая ширина:", rect.get_width())
print("Новая площадь:", rect.get_square())
print("Новый периметр:", rect.get_perimeter())