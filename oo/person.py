class Person:
    eyes = 2

    def __init__(self, *children, name=None, age=20):
        #Atributo = parâmetro
        self.name = name
        self.age = age
        self.children = list(children)

    def greet(self):
        return f'Hey {id(self)}'


if __name__ == '__main__':
    felipe = Person(name='Felipe')
    luciano = Person(felipe, name='Luciano')
    print(Person.greet(luciano))
    print(id(luciano))
    print(luciano.greet())
    print(luciano.name)
    print(luciano.age)
    for child in luciano.children:
        print(child.name)
    luciano.last_name = 'Souza'
    del luciano.children
    luciano.eyes = 1
    del luciano.eyes
    print(luciano.__dict__)
    print(felipe.__dict__)
    Person.eyes = 3
    print(Person.eyes)
    print(felipe.eyes)
    print(luciano.eyes)
    print(id(Person.eyes), id(felipe.eyes), id(luciano.eyes))
