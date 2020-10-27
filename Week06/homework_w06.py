class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = speed

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5






if __name__ == '__main__':
    print('Animal class: ')
    an_name = input('Enter animal name: ')
    an_type = input('Enter animal type: ')
    an_age = input('Enter age: ')
    pet = Pet(an_name, an_type, an_age)
    print('Pet info: {}, {}, {}'.format(pet.get_name(), pet.get_animal_type(), pet.get_age()))


    print('Car class: ')
    car = Car('2020', 'Ford')
    for i in range(5):
        car.accelerate()
    for i in range(2):
        car.brake()

    print('Car: {}, {}, {}km/h'.format(car.get_year_model(), car.get_make(), car.get_speed()))
