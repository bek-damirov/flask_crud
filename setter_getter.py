class Student:
    def __init__(self, name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name.isalpha():
            self.__name = new_name
        else:
            raise Exception('в имени не должно быть цифр')

    @name.deleter
    def name(self):
        raise Exception('удалять нельзя')


s = Student(name='Iman')
print(s.name)
s.name = 'Bek'
print(s.name)
