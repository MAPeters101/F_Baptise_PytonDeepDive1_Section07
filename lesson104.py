class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count

a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(30))
print()

b = Averager()
print(b.add(10))
print(b.add(20))
print(b.add(30))
print('='*40)

def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add

a = averager()
print(a(10))
print(a(20))
print(a(30))
print()

b = averager()
print(b(10))
print(b(20))
print(b(30))
print()










