# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in numbers:
#     print(number)

# iterator = iter(numbers)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) no more than 10

# class Counter:
#     def __init__(self, max_number):
#         self.i=0
#         self.max_number=max_number

#     def __iter__(self):
#         self.i=0
#         return self
    
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
    
# counter = Counter(10)

# for count in counter:
#     print(count)

# def generate_numbers():
#     for i in range(5):
#         yield i #yield делает функцию генератором

# #Вместо того чтобы возвращать все сразу, генератор возвращает по одному элементу

# def generate_numbers2():
#     for i in range(5):
#         return i
    
# print(generate_numbers2())

# gen = generate_numbers()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Декораторы

def decorator(func):
    def wrapper():
        print("Это до вызова функций")
        func()
        print("После вызова функций")
    return wrapper()

@decorator
def say_hello():
    print("Привет")

@decorator
def add():
    print(5+5)