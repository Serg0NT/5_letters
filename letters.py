def get_contained_letters() -> str:
    """Get the letters contained in the word"""
    return input('Введите буквы, которые содержит слово, '
                 'и через знак ПРОБЕЛ пропишите позиции, '
                 'на которых точно нет этих букв.\n'
                 'Например, л 2 р 3 р 4 - будет означать, '
                 'что буква Л точно НЕ 2ая,а Р - НЕ 3ая и 4ая буква '
                 'в загаданном слове.\n')


def get_not_contained_letters() -> tuple:
    """Get the letters not contained in the word"""
    return tuple(input('Введите буквы, НЕ содержащиеся в слове\n'))


def get_position_letters() -> str:
    """Get the mask of the word"""
    position_letters = input \
        ('Введите маску слова с буквами на своих местах, например ПИ*ОН\n')
    if len(position_letters) != 5:
        get_position_letters()
    return position_letters
