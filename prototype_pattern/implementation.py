class Shape:  # Prototype
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def clone(self):
        pass


class Rectangle(Shape):  # Concrete Prototype
    def __init__(self, x=None, y=None, color=None, width=None, height=None, rectangle=None):
        if not rectangle:
            super().__init__(x, y, color)
            self.width = width
            self.height = height
        else:
            super().__init__(rectangle.x, rectangle.y, rectangle.color)
            self.width = rectangle.width
            self.height = rectangle.height

    def clone(self):
        return Rectangle(rectangle=self)

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}, color: {self.color}, width: {self.width}, height: {self.height}."


class Circle(Shape):  # Concrete Prototype
    def __init__(self, x=None, y=None, color=None, radius=None, circle=None):
        if not circle:
            super().__init__(x, y, color)
            self.radius = radius
        else:
            super().__init__(circle.x, circle.y, circle.color)
            self.radius = circle.radius

    def clone(self):
        return Circle(circle=self)

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}, color: {self.color}, radius: {self.radius}."


if __name__ == "__main__":
    circle = Circle(1, 4, "red", 5)
    print(circle)
    copy_circle = circle.clone()
    print(copy_circle)

    rectangle = Rectangle(7, -1, "green", 3, 2)
    print(rectangle)
    copy_rectangle = rectangle.clone()
    print(copy_rectangle)
