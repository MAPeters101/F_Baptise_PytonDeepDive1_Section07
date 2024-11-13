def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

counter1 = counter()
print(counter1())
print(counter1())

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f'{fn.__name__} has been called {cnt} times')
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

counter_add = counter(add)
print(counter_add.__closure__)
print(counter_add.__code__.co_freevars)
print(counter_add(10, 20))
result = counter_add(10, 20)
print(result)

counter_mult = counter(mult)
print(counter_mult(2, 5))

