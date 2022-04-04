from random import choice

class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.make_greeting()

    def make_greeting(self):
        self.name_ = 'Hello {name}'
        return self.name_.format(name=self.name)


def main():
    people = [
        Person("Noah"),
        Person("Hannah"),
        Person("Johnson")
    ]
    person = choice(people)
    print(person)


if __name__ == '__main__':
    main()
