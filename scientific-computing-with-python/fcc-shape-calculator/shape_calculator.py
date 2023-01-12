class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        if self.__class__.__name__ == "Rectangle":
            self.width = width
        else:
            self.width = width
            self.height = width

    def set_height(self, height):
        if self.__class__.__name__ == "Rectangle":
            self.height = height
        else:
            self.height = height
            self.width = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def __str__(self):
        if self.width != self.height:
            return f"{self.__class__.__name__}(width={self.width}, height={self.height})"
        else:
            return f"{self.__class__.__name__}(side={self.width})"

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = "*"*self.width + "\n"
            picture = picture*self.height

        return picture

    def get_amount_inside(self, other):
        area_1 = self.get_area()
        area_2 = other.get_area()
        amount_inside = int(area_1 / area_2)

        return amount_inside

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(width = length, height = length)

    def set_side(self, length):
        self.width = length
        self.height = length