

class Computer:
    def __init__(self):
        self.name = ''
        self.model = ''

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def to_string(self):
        return "{}, {}".format(self.name, self.model)


if __name__ == '__main__':
    comp = Computer()

    comp.set_name('Macbook')
    comp.set_model('Pro 2020')
    print(comp.to_string())



