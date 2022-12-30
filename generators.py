def create_cubes(n):
    for x in range(n):
        yield x**3

print(list(create_cubes(0)))

def generator_febonachi(n, a=1, b=1):
    for i in range(n):
        yield a
        a,b = b, a+b

print(list(generator_febonachi(10)))