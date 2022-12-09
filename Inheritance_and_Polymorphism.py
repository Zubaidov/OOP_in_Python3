# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#
#     def __len__(self):
#         return self.pages
#
#     def __del__(self):
#         return "The book object has been deleted"
#
# b = Book('Python rocks', 'Jose', 200)
# print(b)
# print(len(b))
# print(del)

class Line():

    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2
        print(self.x1, self.y1, self.x2, self.y2)

    def distance(self):
        return f"The distance between coordinates: {((self.x1-self.y1)**2+(self.x2-self.y2)**2)**1/2}"

    def slope(self):
        return f"The slope between coordinates: {(self.y2-self.y1)/(self.x2-self.x1)}"

coordinate1 = (3,2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())

pi = 3.14

class Cylinder():
    def __init__(self, height=1, radius=1):
        self.h = height
        self.r = radius
        print(self.h, self.r, pi)

    def volume(self):
        return f"The Volume of the Cylinder: {pi*self.r**2*self.h}"

    def surface_area(self):
        return f"The Surface Area of the Cylinder: {2*pi*self.r*self.h+2*pi*self.r**2}"

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())