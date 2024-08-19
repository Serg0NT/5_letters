from words import get_all_words

ru_letters = {
    "а": 0,
    "б": 0,
    "в": 0,
    "г": 0,
    "д": 0,
    "е": 0,
    "ж": 0,
    "з": 0,
    "и": 0,
    "й": 0,
    "к": 0,
    "л": 0,
    "м": 0,
    "н": 0,
    "о": 0,
    "п": 0,
    "р": 0,
    "с": 0,
    "т": 0,
    "у": 0,
    "ф": 0,
    "х": 0,
    "ц": 0,
    "ч": 0,
    "ш": 0,
    "щ": 0,
    "ь": 0,
    "ы": 0,
    "ъ": 0,
    "э": 0,
    "ю": 0,
    "я": 0,
}
all_words = get_all_words("words.txt")
count_letters = {}
w1 = 'коран'
w2 = 'метис'
w3 = 'выгул'
top_letters = ["а", "о", "к", "р", "е", "т", "и", "н", "л", "с", "у", "м", "в",
               "п"]


def get_count_letters(all_words: list[str]) -> dict:
    for word in all_words:
        for letter in word:
            count_letters[letter] = count_letters.get(letter, 0) + 1

    return count_letters


dict_ltrs = get_count_letters(all_words)

for ltrs in ru_letters.keys():
    for word in all_words:
        if ltrs in word:
            ru_letters[ltrs] = ru_letters.get(ltrs, 0) + 1

sorted_dict = sorted(dict_ltrs.items(), key=lambda item: -item[1])
print(sorted_dict)
