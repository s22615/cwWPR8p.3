class Basics:
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return "basic {x}".format(x=self.field)

    def print_field(self):
        return print(self.field)

    def __qt__(self, other):
        return self.field > other.field


class X:
    def __init__(self, field):
        self.field = field


def print_field(x):
    return print(x.field)


b = Basics(10)
b = Basics(15)
x = X("Hello")
print(b)
print_field(b)
b.print_field()
Basics.print_field(b)
print_field(x)
Basics.print_field(x)