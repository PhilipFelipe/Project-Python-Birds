class Person:
    def __init__(self, name=None, age=20):
        #Atributo = parâmetro
        self.name = name
        self.age = age

    def greet(self):
        return f'Hey {id(self)}'


if __name__ == '__main__':
    p = Person('Alan')
    print(Person.greet(p))
    print(id(p))
    print(p.greet())
    print(p.name)
    p.name = 'Felipe'
    print(p.name)
    print(p.age)
