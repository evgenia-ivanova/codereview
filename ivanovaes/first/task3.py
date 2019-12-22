"""
Перевірити на те, щоб перше число, що водить користувач було цілим та невід'ємним,
а друге -  цілим не додатнім числом"""

number1 = input("Pls, enter 1 number: ")
number2 = input("Pls, enter 2 number: ")
if '.' in number1 and isinstance(number1, float) <= 0 : #
    print("number1 не задовільняє умову")
else:
    print(number1)
if '.' in number2 and isinstance(number2, float) <= 0 and :
    print("number2 не задовільняє умову")
else:
    print(number2)
