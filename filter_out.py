import string
from typing import Sequence


def filter_by_positional_letters(letters: str, words: Sequence) -> Sequence:
    if len(words) == 1:
        return words
    ind = 0
    for letter in letters:
        if letter != "*":
            words = [word for word in words if letter == word[ind]]
        ind += 1
    print(f'Осталось возможных вариантов - {len(words)}\n')
    return words


def filter_by_not_contained_letters(letters: tuple,
                                    words: Sequence) -> Sequence:
    if len(words) == 1:
        return words
    for letter in letters:
        words = [word for word in words if letter not in word]
    print(f'Осталось возможных вариантов - {len(words)}\n')
    return words


def filter_by_contained_letters(letters: str, words: Sequence) -> Sequence:
    if len(words) == 1:
        return words
    tt = str.maketrans(dict.fromkeys(string.punctuation))
    list_of_ltrs = letters.translate(tt).split()
    positions: dict[str, list[str]] = {}
    x = None
    cont_letters = []
    for i in list_of_ltrs:
        if i.isalpha():
            cont_letters.append(i)
            x = i
        else:
            positions.setdefault(i, []).append(x)

    for letter in cont_letters:
        words = [word for word in words if letter in word]

    for k, v in positions.items():
        for i in v:
            words = [word for word in words if i != word[int(k) - 1]]

    print(f'Осталось возможных вариантов - {len(words)}\n')
    return words
