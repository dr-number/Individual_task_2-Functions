from typing import Union
from functools import reduce
from random import randint
import re

COLOR_GREEN = '\033[92m'
COLOR_OKCYAN = '\033[96m'
COLOR_OKBLUE = '\033[94m'
COLOR_WARNING = '\033[93m'
COLOR_FAIL = '\033[91m'
_COLOR_ENDC = '\033[0m'

MIN_VALUE = -10_000
MAX_VALUE = 10_000

_EX_1 = '1'
_EX_2 = '2'
_EX_3 = '3'
_EX_4 = '4'
_EX_5 = '5'
_EX_6 = '6'

_ARRAY_EX = [_EX_1, _EX_2, _EX_3, _EX_4, _EX_5, _EX_6]

def get_text_color(text: str, color: str) -> str:
    return f'{color}{text}{_COLOR_ENDC}'

def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def input_number(text: str, default_value: float = None, min: float = None, max: float = None) -> float:
    while True:
        number = input(f'{get_text_color(text, COLOR_WARNING)} ')
        if number == '':
            if default_value is not None:
                return default_value
            print(get_text_color("Введите число!", COLOR_FAIL))
        elif is_number(number):
            num = float(number)
            if min is not None and num < min:
                print(get_text_color(f"Минимально допустимое число - {min}!", COLOR_FAIL))
            elif max is not None and num > max:
                print(get_text_color(f"Максимально допустимое число - {max}!", COLOR_FAIL))
            else:
                return num
        else:
            print(get_text_color(f"\"{number}\" - не число! Повторите ввод!", COLOR_FAIL))


def _init_ex_1():
    p = [randint(0, 10) for _ in range(10)]
    q = [randint(0, 10) for _ in range(10)]
    r = [randint(0, 10) for _ in range(10)]
    
    print(f"Массив {get_text_color(f'p: {p}', COLOR_WARNING)}")
    print(f"Количество 5: {get_text_color(count_fives(p), COLOR_GREEN)}")
    print(f"Массив {get_text_color(f'q: {q}', COLOR_WARNING)}")
    print(f"Количество 5: {get_text_color(count_fives(q), COLOR_GREEN)}")
    print(f"Массив {get_text_color(f'r: {r}', COLOR_WARNING)}")
    print(f"Количество 5: {get_text_color(count_fives(r), COLOR_GREEN)}")

def count_fives(arr: list) -> int:
    return arr.count(5)

def _init_ex_2():
    # Генерация массивов
    a = [randint(0, 5) for _ in range(20)]
    b = [randint(0, 5) for _ in range(20)]
    c = [randint(0, 5) for _ in range(20)]
    
    print(f"Массив a: {a}")
    a_last_zero = last_zero_index(a)
    print(f"Индекс последнего нуля: {a_last_zero}")
    
    print(f"Массив b: {b}")
    b_last_zero = last_zero_index(b)
    print(f"Индекс последнего нуля: {b_last_zero}")
    
    print(f"Массив c: {c}")
    c_last_zero = last_zero_index(c)
    print(f"Индекс последнего нуля: {c_last_zero}")
    
    total = sum([x if x is not None else 0 for x in [a_last_zero, b_last_zero, c_last_zero]])
    print(f"Сумма индексов: {total}")

def last_zero_index(arr: list) -> Union[int, None]:
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            return i
    return None

def _init_ex_3():
    s1 = "Иванушка пошел за водой. Иванушка встретил медведя."
    s2 = "Иванушка и Иванушка играли вместе."
    s3 = "Здесь нет нужного слова."
    
    print(f"Текст 1: {s1}")
    count1 = count_ivanushka(s1)
    print(f"Количество 'Иванушка': {count1}")
    
    print(f"Текст 2: {s2}")
    count2 = count_ivanushka(s2)
    print(f"Количество 'Иванушка': {count2}")
    
    print(f"Текст 3: {s3}")
    count3 = count_ivanushka(s3)
    print(f"Количество 'Иванушка': {count3}")
    
    max_count = max(count1, count2, count3)
    if max_count == 0:
        print("Ни в одном тексте нет слова 'Иванушка'")
    else:
        texts = []
        if count1 == max_count:
            texts.append("1")
        if count2 == max_count:
            texts.append("2")
        if count3 == max_count:
            texts.append("3")
        print(f"Наибольшее количество 'Иванушка' в тексте(ах): {', '.join(texts)}")

def count_ivanushka(text: str) -> int:
    return len(re.findall(r'\bИванушка\b', text))

def _init_ex_4():
    n = int(input_number("Введите N: ", min=1, max=20))
    m_values = []
    for i in range(5):
        m = int(input_number(f"Введите M{i+1} (0 <= M <= {n}): ", min=0, max=n))
        m_values.append(m)
    
    for m in m_values:
        global _recursion_count
        _recursion_count = 0
        result = combinations(m, n)
        print(f"C({m},{n}) = {result}, рекурсивных вызовов: {_recursion_count}")

_recursion_count = 0

def combinations(m: int, n: int) -> int:
    global _recursion_count
    _recursion_count += 1
    
    if m == 0 or m == n:
        return 1
    if 0 < m < n:
        return combinations(m, n-1) + combinations(m-1, n-1)
    return 0

def _init_ex_5():
    words1 = ["Hello", "world", "from", "Python"]
    words2 = ["This", "is", "a", "test"]
    
    join_words = lambda words: reduce(lambda x, y: f"{x} {y}", words)
    
    print(f"Список 1: {words1}")
    print(f"Результат: '{join_words(words1)}'")
    print(f"Список 2: {words2}")
    print(f"Результат: '{join_words(words2)}'")

def _init_ex_6():
    separator = input("Введите разделитель: ")
    strings = []
    while True:
        s = input("Введите строку (пустая строка для завершения): ")
        if not s:
            break
        strings.append(s)
    
    result = join_strings(separator, *strings)
    print(f"Результат: {result}")

def join_strings(separator: str, *strings: str) -> str:
    return separator.join(strings)

def main():
    while True:
        print(
            f'''\nЛарионов гр. 410з. Программирование на языках высокого уровня
Индивидуальное задание №2 Функции. Вариант 3.\n
{get_text_color(f'Какую задачу выполнить: ', COLOR_WARNING)}
{get_text_color(f'{_EX_1}) ', COLOR_WARNING)}Оформить функцию поиска количества элементов равных 5. В главной
программе дано 3 одномерных массива p, q, r длиной 10 элементов
каждый. Применить функцию для каждого из 3 -х заданных массивов.\n
{get_text_color(f'{_EX_2}) ', COLOR_WARNING)}Оформить функцию поиска номера последнего нулевого элемента в
массиве. В главной программе дано 3 одномерных массива a, b, c длиной
20 элементов каждый. Применить функцию для каждого из 3-х заданных
массивов. Найти сумму найденных номеров элементов.\n
{get_text_color(f'{_EX_3}) ', COLOR_WARNING)}Описать функцию, вычисляющую количество слов «Иванушка» в тексте.
В главной программе дано 3 текста S1, S2, S3. Выяснить, в каком тексте
больше слов «Иванушка», используя функцию.\n
{get_text_color(f'{_EX_4}) ', COLOR_WARNING)}Описать рекурсивную функцию C(m,n) целого типа, находящую число
сочетаний из n элементов по m, используя формулу: C(0,n) = C(n,n) = 1,
C(m,n) = C(m,n–1) + C(m–1,n–1) при 0 < m < n (m и n — целые параметры;
n > 0, 0 <= m <= n). Дано число N и пять различных значений M. Вывести
числа C(M,N) вместе с количеством рекурсивных вызовов функции C,
потребовавшихся для их нахождения.\n
{get_text_color(f'{_EX_5}) ', COLOR_WARNING)}Описать lambda-функцию с reduce(), чтобы объединить строки, добавляя
между ними пробел. В программе создайте 2 списка слов и используя
вашу функцию объедините их в предложение.\n
{get_text_color(f'{_EX_6}) ', COLOR_WARNING)}Напишите функцию, которая принимает разделитель и произвольное
количество строк, а затем возвращает объединенную строку с
использованием переданного разделителя.\n'''
        )
        select = input('Для выхода введите \'0\'\n')

        if select in _ARRAY_EX:
            globals()[f'_init_ex_{select}']()
        elif select == '0':
            break
        else:
            print(
                f'{get_text_color("Введен неверный номер задачи!", COLOR_FAIL)}'
            )

if __name__ == '__main__':
    main()