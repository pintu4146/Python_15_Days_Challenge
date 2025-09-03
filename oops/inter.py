

class ClassA:
    def __init__(self, name):
        print('class A constructor invokes')
        self.name = name

    def display_name(self):
        print(f'Name: {self.name}')
        return self.name

    def __repr__(self):
        """ object representation """
        print("class A str reprsentation")



class ClassB(ClassA):
    def __init__(self, name):
        print('Class B constructor invokes')
        self.name = name


classb_object = ClassB(name='Pintu')
print(classb_object)
classa_object = ClassA(name='pin3')
print(ClassA.display_name(classa_object))



