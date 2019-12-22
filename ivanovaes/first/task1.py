"""
Вивести із списку всі елементи типу рядок
"""


list = ["jdvhbjv", "GVfdjv", 4567, -4576, "fjvhb", 78.65]
for element in list:
    if type(element) is str:
        print(element)
    else:
        continue