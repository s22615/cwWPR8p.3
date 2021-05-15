class Shape:
    def __init__(self, n=None):
        self.n = n

    def draw(self, n=None):
        raise NotImplementedError('draw')

    def make_n(self, n):
        if n is None:
            n = self.n
        return n

    def draw(self, n=None):
        n = self.make_n(n)
        for i in range(1, n + 1):
            self.draw_line(i, n)

    def scale(self, f):
        self.n *= f


class Triangle(Shape):
    def draw_line(self, i, n):
        print("*" * i)


class Square(Shape):
    def draw_line(self, i, n):
        print("*" * n)


s = Shape()
# s.draw(5)
t = Triangle(2)
t.draw()
t.draw(4)
q = Square(2)
q.draw()
q.draw(4)

###########################

q = Square(2)
q.draw()
q.scale(3)
q.draw()