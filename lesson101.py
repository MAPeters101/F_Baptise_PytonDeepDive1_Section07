
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

def outer_func6():
    x = 'hello6'
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
            print('inner:', x)
        print('outer(before inner2):', x)
        inner2()
    print('outer(before inner1):', x)
    inner1()
    print('outer(after inner1):', x)

outer_func6()
#print('outer(after outer):', x)
print('='*30)

# x = 'python'
# def outer_func7():
#     global x
#     x = 'monty7'
#     def inner():
#         nonlocal x
#         x = 'hello7'
#     print('outer(before inner):', x)
#     inner()
#     print('outer(after inner):', x)
#
# outer_func7()
# print()

x = 'python'
def outer_func8():
    x = 'monty8'
    def inner():
        nonlocal x
        x = 'hello8'
    print('outer(before inner):', x)
    inner()
    print('outer(after inner):', x)

outer_func8()
print(x)
print()


x = 'python'
def outer_func8():
    global x
    x = 'monty8'
    def inner():
        global x
        x = 'hello8'
    print('outer(before inner):', x)
    inner()
    print('outer(after inner):', x)

outer_func8()
print(x)
print()





