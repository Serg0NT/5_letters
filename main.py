from typing import Sequence

from words import get_all_words
from letters import (get_contained_letters,
                     get_not_contained_letters,
                     get_position_letters)
from filter_out import (filter_by_contained_letters,
                        filter_by_not_contained_letters,
                        filter_by_positional_letters)


def main() -> Sequence:
    words = get_all_words("words.txt")
    words = filter_by_positional_letters(get_position_letters(), words)
    words = filter_by_not_contained_letters(get_not_contained_letters(), words)
    return filter_by_contained_letters(get_contained_letters(), words)


if __name__ == "__main__":
    result = main()
    for item in result:
        print(item)
    print(len(result))
