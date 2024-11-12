
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




