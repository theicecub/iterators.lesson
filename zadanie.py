#1
text = input("Введите слово")

iterator=iter(text)

for i in text:
    print(next(iterator))

#2
text = (input())

iterator = iter(text)

try:
    while True:
        print(next(iterator))
except StopIteration:
    print("Дошли до конца")

#3
numbers = [8, -3, 2, 4, 102]
iterator = iter(numbers)

for i in numbers:
    print(next(iterator) ** 2)

#4
def generate_numbers():
    for i in range(1, 6):
        yield i ** 2

gen = generate_numbers()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))