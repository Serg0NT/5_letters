import string

ltrs: str = input(
    'Введите буквы, которые содержит слово, и через знак = пропишите позиции, на которых точно нет этих букв.\n'
    'Например, У=2 4, x=3 4 - будет означать, что буква У точно не 2ая и не 4ая буква в загаданном слове.\n')
# print(list(ltrs))
tt = str.maketrans(dict.fromkeys(string.punctuation))

# list_of_ltrs = re.split('=| =|=| | , ', ltrs)
list_of_ltrs = ltrs.translate(tt).split()
print(list_of_ltrs)
positions = {}
for i in list_of_ltrs:
    if i.isalpha():
        x = i
    else:
        positions.setdefault(i, []).append(x)
        # print(type(positions.get(i, [])))

print(positions)
