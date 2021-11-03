import sys
from string import punctuation
import pprint
import json
from nltk.corpus import cmudict

cmudict = cmudict.dict()


def main():
    haiku = load_haiku('train.txt')
    exceptions = cmudict_missing(haiku)
    build_dict = input("\nПостроить словарь исключений вручную (y/n)? \n")
    if build_dict.lower() == 'n':
        sys.exit()
    else:
        missing_words_dict = make_exceptions_dict(exceptions)
        save_exceptions(missing_words_dict)


def load_haiku(filename):
    """Отыскать и вернуть тренировочный корпус хоку в виде множества."""
    with open(filename) as in_file:
        haiku = set(in_file.read().replace('-', ' ').split())
        return haiku


def cmudict_missing(word_set):
    """Отыскать и вернуть слова в множестве слов,
       отсуствующих в cmudict."""
    exceptions = set()
    for word in word_set:
        word = word.lower().strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word not in cmudict:
            exceptions.add(word)
    print("\nисключения:")
    print(*exceptions, sep='\n')
    print(f"\nЧисло уникальных слов в корпусе хокку = {len(word_set)}")
    print(f"Число слов в корпусе слов не из cmudict = {len(exceptions)}")
    membership = (1 - (len(exceptions) / len(word_set))) * 100
    print(f"членство в cmudict = {membership:.1f}{'%'}")
    return exceptions


def make_exceptions_dict(exceptions_set):
    """Вернуть словарь слов и количеств слогов из множества слов."""
    missing_words = {}
    print("Введите число слогов в слове. Ошибки можно исправить в конце. \n")
    for word in exceptions_set:
        while True:
            num_sylls = input(f"Введите число слогов в {word}: ")
            if num_sylls.isdigit():
                break
            else:
                print("              Недопустимый ответ!", file=sys.stderr)
        missing_words[word] = int(num_sylls)
    print()
    pprint.pprint(missing_words, width=1)

    print("\nВнесити изменениям в словарь перед сохранением?")
    print("""
    0 - Выйти и сохранить
    1 - Добавить слово или изменить количество слогов
    2 - Удалить слово
    """)

    while True:
        choice = input("\nСделайте свой выбор: ")
        if choice == '0':
            break
        elif choice == '1':
            word = input("\nДобовляемое или изменяемое слово: ")
            missing_words[word] = int(input(f"Введите число слогов в {word}: "))

        elif choice == '2':
            word = input('\nВведите удаляемое слово: ')
            missing_words.pop(word, None)

    print("\nИзменения в новых словах и слогах:")
    pprint.pprint(missing_words, width=1)

    return missing_words


def save_exceptions(missing_words):
    """Сохранить словарь исключений exceptions как файл json."""
    json_string = json.dumps(missing_words)
    f = open('missing_words.json', 'w')
    f.write(json_string)
    f.close()
    print("\nФайл сохранен как missing_words.json")


if __name__ == '__main__':
    main()
