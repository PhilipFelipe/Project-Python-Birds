class Person:
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
