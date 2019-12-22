"""
Перевірити введений шлях до файлу на коректність та поступово!!! дійти до визначеного файла,
відкриваючи папки у правилльному порядці
"""

folder = []
def create_list():
    file_name = input("Введіть назву папки: ")
    folder.append(file_name)
    question = str(input("Відкрити наступну папку, натисніть yes/no: "))
    if question == "yes":
        create_list()
    else:
        name_list = input("Введіть назву документів через коми: ")
        folder.append(name_list)
    return folder
create_list()
def path():
    create_list()
    for element in create_list():
        str()

def file_search(folder, file_path):