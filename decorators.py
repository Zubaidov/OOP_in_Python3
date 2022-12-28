# def hello(name):
#     def greet():
#         print('This is the greet() func inside hello!')
#     def welcome():
#         print('This is welcome() inside the hello')
#
#     if name == 'Shohruz':
#         return greet()
#     else:
#         return welcome()
#
# #my_new_func = hello('Shohruz')
#
#
# def helllo():
#     return 'Hi Jose'
#
# def other(some_def_func):
#     print('Ohter CODE runs here')
#     print(some_def_func())
#
# other(helllo)


def new_decorator(original_func):

    def wrap_func():
        print('Some extra code, before the original function')

        original_func()

        print('Some extra code, after the original function')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('I want to be decorated!!')

func_needs_decorator()

# decorated_func = new_decorator(func_needs_decorator)
# decorated_func()
