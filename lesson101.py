
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







