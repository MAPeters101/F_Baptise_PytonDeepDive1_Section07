
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





