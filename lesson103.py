
def outer():
    x = 'python'
    def inner():
        print(x)
    return inner

fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print()
print()

def outer1():
    x = [1, 2, 3]
    print(hex(id(x)), x)

    def inner():
        x = [2, 3]
        print('inner', hex(id(x)), x)
    return inner

fn = outer1()
fn()
#print(fn.x)

print(fn.__code__.co_freevars)
print(fn.__closure__)
print()
print()

def outer2():
    x = [1, 2, 3]
    print(hex(id(x)), x)

    def inner():
        y = x
        print('inner', hex(id(x)), x, hex(id(y)), y)
    return inner

fn = outer2()
fn()
#print(fn.x)

print(fn.__code__.co_freevars)
print(fn.__closure__)
print('='*40)


def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(hex(id(0)))

print(fn())
print(fn.__closure__)
print(hex(id(1)))
print()

def outer1():
    count = 0
    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2

fn1, fn2 = outer1()
print(fn1.__code__.co_freevars, fn2.__code__.co_freevars)
print(fn1.__closure__)
print(fn2.__closure__)
print(hex(id(0)))
print()

print(fn1())
print(fn1.__code__.co_freevars, fn2.__code__.co_freevars)
print(fn1.__closure__)
print(fn2.__closure__)
print(hex(id(1)))
print()

print(fn2())
print(fn1.__code__.co_freevars, fn2.__code__.co_freevars)
print(fn1.__closure__)
print(fn2.__closure__)
print(hex(id(2)))
print()
print('+'*30)

def pow(n):
    def inner(x):
        return x ** n
    return inner

square = pow(2)
print(square.__closure__)
print(hex(id(2)))
print(square)
print(square(5))
print()

cube = pow(3)
print(cube.__closure__)
print(hex(id(3)))
print(cube)
print(cube(5))
print('-'*80)

def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
print(add_1.__closure__)
print(add_2.__closure__)
print(add_3.__closure__)
print(hex(id(1)))
print(hex(id(2)))
print(hex(id(3)))
print(add_1(10))
print(add_2(10))
print(add_3(10))
print()

adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)

print(adders)
print(n)
print(adders[0].__closure__)
print(adders[0](10))
print('='*80)


def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x + n)
    return adders

adders = create_adders()
print(adders)
print(n)
print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[2].__closure__)
print(adders[0](10))
print(adders[1](10))
print(adders[2](10))











