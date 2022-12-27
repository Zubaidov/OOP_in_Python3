def hello(name):
    def greet():
        print('This is the greet() func inside hello!')
    def welcome():
        print('This is welcome() inside the hello')

    if name == 'Shohruz':
        return greet()
    else:
        return welcome()

my_new_func = hello('Shohruz')