class Dog():
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def Energy(self):
        if self.energy is True:
            print("Guf Guf")
        else:
            print("bing bing")

my_dog1 = Dog(name='Gretta', energy=True)
my_dog2 = Dog(name='Halo', energy=False)

list1 = [my_dog1, my_dog2]

for key in list1:
    print(key.name), Dog.Energy(key)