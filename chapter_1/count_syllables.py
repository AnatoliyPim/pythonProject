import sys
from string import punctuation
import json
from nltk.corpus import cmudict


with open('missing_words.json') as f:
    missing_words = json.load(f)

cmudict = cmudict.dict()


def count_syllables(words):
    """Использовать корпусы для подсчета слогов в английском слове
       или словосочетании."""
    words = words.replace('-', ' ')
    words = words.lower().split()
    num_sylls = 0
    for word in words:
        word = word.strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word in missing_words:
            num_sylls += missing_words[word]
        else:
            for phonemes in cmudict[word][0]:
                for phoneme in phonemes:
                    if phoneme[-1].isdigit():
                        num_sylls += 1
    return num_sylls


def main():
    while True:
        print("Счетчик слогов")
        word = input("Введите слово или словосочетание либо нажмите Enter, чтобы выйти: ")
        if word == '':
            sys.exit()
        try:
            num_syllables = count_syllables(word)
            print(f"Число слогов в {word} ровно: {num_syllables}")
            print()
        except KeyError:
            print("Слово не найдено. Попробуйте еще раз.\n", file=sys.stderr)


if __name__ == '__main__':
    main()
