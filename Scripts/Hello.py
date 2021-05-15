class Hello:
    def __init__(self, greetings):
        self.greetings = greetings

    def great(self, person):
        return print("{} {}".format(self.greetings, person))


def hello(person, greetings="Hello"):
    return print("{} {}".format(greetings, person))


hello("Text", "Hi")
new = Hello("Hi")
new.great("Sebastian")
new.great("123")
