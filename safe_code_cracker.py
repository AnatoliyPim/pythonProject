import time
from random import randint, randrange


def fitness(combo, attempt):
    """Сравнить элементы в двух списках и подсчитать
       число совпадений."""
    grade = 0

    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1
    return grade


def main():
    """Применить алгоритм восхождения к вершине холма
       для решения комбинации замков."""
    combination = '2554176927'
    print(f"Комбинация = {combination}")

    combo = [int(i) for i in combination]

    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0

    while best_attempt != combo:
        next_try = best_attempt[:]
        lock_wheel = randrange(0, len(combo))
        next_try[lock_wheel] = randint(0, 9)

        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        print(next_try, best_attempt)
        count += 1
    print()
    print(f"Взломано! {best_attempt}", end=' ')
    print(f"За {count} попыток!")


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"\nВремя выполнения этой программы составило {duration:.5f} секунд.")