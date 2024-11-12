a = 10

print(a)
print()

def my_func1(n):
    c = n ** 2
    return c

print(my_func1(5))
print()

def my_func(n):
    print('global a:', a)
    c = a ** n
    return c

print(my_func(2))
print()

def my_func2(n):
    a = 20
    print(f'{a=}')
    c = a ** n
    return c

print(f'{a=}')
print(my_func2(2))
print(f'main: {a=}')
print()

def my_func3(n):
    global a
    a = 20
    print(f'my_func3: {a=}')
    c = a ** n
    return c

print(f'main: {a=}')
print(my_func3(2))
print(f'main: {a=}')
print()







