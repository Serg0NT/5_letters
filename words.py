from typing import Sequence


def get_all_words(file: str) -> Sequence:
    """Get all words from file and return list of strings"""
    with open(file, 'r', encoding='utf-8') as f:
        words = f.read()
    return list(words.split())
