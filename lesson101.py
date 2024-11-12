
def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
    inner_func()

outer_func()
print()

def outer_func2():
    x = 'hello2'
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()

outer_func2()
print()

def outer_func3():
    x = 'hello3'
    def inner():
        x = 'python'
        print('inner:', x)
    inner()
    print('outer:', x)

outer_func3()
print()

def outer_func4():
    x = 'hello4'
    def inner():
        nonlocal x
        x = 'python'
        print('inner:', x)
    print('outer(before inner):', x)
    inner()
    print('outer(after inner):', x)

outer_func4()
print('='*80)
print()


def outer_func5():
    x = 'hello5'
    def inner1():
        def inner2():
            nonlocal x
            x = 'python'
            print('inner:', x)
        inner2()
    print('outer(before inner1):', x)
    inner1()
    print('outer(after inner1):', x)

outer_func5()
#print('outer(after outer):', x)
print()







