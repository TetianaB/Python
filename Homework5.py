class Person_class():
    def __init__(self, name, hair_color, eye_color, age):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.age = age

    def __hobby(self):
        print('I have a hobby')

    def travel(self, country, year):
        self.country = country
        self.year = year
        print(f'I visited {country} in {year}')


tanya=Person_class('Tanya', 'blond', 'blue', 51)
print(tanya.hobby)