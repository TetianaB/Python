class Person_class():
    biology_class = 'People'
    def __init__(self, name, hair_color, eye_color, age):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.age = age
        print(f'My name is {name}, i am {age}')

    def _hobby(self):
        print('I have a hobby')

    def travel(self, country, year):
        self.country = country
        self.year = year
        print(f'I visited {country} in {year}')

class Gender(Person_class):
    def __init__(self, name, hair_color, eye_color, age, gender, orientation):
        super().__init__(name, hair_color, eye_color, age)
        self.gender = gender
        self.orientation = orientation
        print(f'I am a {gender} and I prefer {orientation}')

    def more_info(self):
        print('I love all')


tanya=Person_class('Tanya', 'blond', 'blue', 51)
print(tanya.name)
print(tanya._hobby())
print(tanya.travel('France', 2002))
print(tanya.biology_class)

ivan=Gender('Ivan', 'brown', 'brown', 43, 'male', 'man')
print(ivan.eye_color)
print(ivan.gender)
print(ivan.more_info())
print(ivan._hobby())