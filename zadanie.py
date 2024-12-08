#1
text = input("Введите слово")

iterator=iter(text)

for i in text:
    print(next(iterator))
