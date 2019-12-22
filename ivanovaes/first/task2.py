"""
Вивести всі слова, що починаються з великих літер
"""


text = "kdjbvkb kdbvfd jhvb ASddf Ahbhu Ahjbg"
word = text.split(" ")
for element in word:
    letter = element.split()
    if "A" in letter[0]: #якщо 0 елемент списку "letter" є великою літерою
        print(element)
    else:
        continue