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

TEXT_TASK_1 = f'''Оформить функцию поиска количества элементов равных 5. В главной
программе дано 3 одномерных массива p, q, r длиной 10 элементов
каждый. Применить функцию для каждого из 3 -х заданных массивов.\n
'''

TEXT_TASK_2 = f'''Оформить функцию поиска номера последнего нулевого элемента в
массиве. В главной программе дано 3 одномерных массива a, b, c длиной
20 элементов каждый. Применить функцию для каждого из 3-х заданных
массивов. Найти сумму найденных номеров элементов.\n
'''

TEXT_TASK_3 = f'''Описать функцию, вычисляющую количество слов «Иванушка» в тексте.
В главной программе дано 3 текста S1, S2, S3. Выяснить, в каком тексте
больше слов «Иванушка», используя функцию.\n
'''

TEXT_TASK_4 = f'''Описать рекурсивную функцию C(m,n) целого типа, находящую число
сочетаний из n элементов по m, используя формулу: C(0,n) = C(n,n) = 1,
C(m,n) = C(m,n–1) + C(m–1,n–1) при 0 < m < n (m и n — целые параметры;
n > 0, 0 <= m <= n). Дано число N и пять различных значений M. Вывести
числа C(M,N) вместе с количеством рекурсивных вызовов функции C,
потребовавшихся для их нахождения.\n
'''

TEXT_TASK_5 = f'''Описать lambda-функцию с reduce(), чтобы объединить строки, добавляя
между ними пробел. В программе создайте 2 списка слов и используя
вашу функцию объедините их в предложение.\n
'''

TEXT_TASK_6 = f'''Напишите функцию, которая принимает разделитель и произвольное
количество строк, а затем возвращает объединенную строку с
использованием переданного разделителя.\n
'''

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

def input_string(text: str) -> str:
    while True:
        _string = input(f'{get_text_color(text, COLOR_WARNING)} ')
        if _string == '':
            print(get_text_color("Текст не должен быть пустым!", COLOR_FAIL))
        else:
            return _string


def _init_ex_1():
    print(get_text_color(TEXT_TASK_1, COLOR_WARNING))
    p = [randint(0, 10) for _ in range(10)]
    q = [randint(0, 10) for _ in range(10)]
    r = [randint(0, 10) for _ in range(10)]
    
    print(f"Массив {get_text_color(f'p: {p}', COLOR_WARNING)}")
    print(f"Количество 5: {get_text_color(count_fives(p), COLOR_GREEN)}\n")
    print(f"Массив {get_text_color(f'q: {q}', COLOR_WARNING)}")
    print(f"Количество 5: {get_text_color(count_fives(q), COLOR_GREEN)}\n")
    print(f"Массив {get_text_color(f'r: {r}', COLOR_WARNING)}")
    print(f"Количество 5: {get_text_color(count_fives(r), COLOR_GREEN)}")

def count_fives(arr: list) -> int:
    return arr.count(5)

def _init_ex_2():
    print(get_text_color(TEXT_TASK_2, COLOR_WARNING))
    a = [randint(0, 5) for _ in range(20)]
    b = [randint(0, 5) for _ in range(20)]
    c = [randint(0, 5) for _ in range(20)]
    
    print(f"Массив {get_text_color(f'a: {a}', COLOR_WARNING)}")
    a_last_zero = last_zero_index(a)
    print(f"Индекс последнего нуля: {get_text_color(a_last_zero, COLOR_GREEN)}")
    
    print(f"Массив {get_text_color(f'b: {b}', COLOR_WARNING)}")
    b_last_zero = last_zero_index(b)
    print(f"Индекс последнего нуля: {get_text_color(b_last_zero, COLOR_GREEN)}")
    
    print(f"Массив {get_text_color(f'c: {c}', COLOR_WARNING)}")
    c_last_zero = last_zero_index(c)
    print(f"Индекс последнего нуля: {get_text_color(c_last_zero, COLOR_GREEN)}")
    
    total = sum([x if x is not None else 0 for x in [a_last_zero, b_last_zero, c_last_zero]])
    print(f"\nСумма индексов: {get_text_color(total, COLOR_GREEN)}")

def last_zero_index(arr: list) -> Union[int, None]:
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            return i
    return None

def _init_ex_3():
    print(get_text_color(TEXT_TASK_3, COLOR_WARNING))
    s1 = "Иванушка пошел за водой. Иванушка встретил медведя."
    s2 = "Иванушка и Иванушка играли вместе."
    s3 = "Здесь нет нужного слова."
    
    print(f"Текст 1: {get_text_color(s1, COLOR_WARNING)}")
    count1 = count_ivanushka(s1)
    print(f"Количество 'Иванушка': {get_text_color(count1, COLOR_GREEN)}\n")
    
    print(f"Текст 2: {get_text_color(s2, COLOR_WARNING)}")
    count2 = count_ivanushka(s2)
    print(f"Количество 'Иванушка': {get_text_color(count2, COLOR_GREEN)}\n")
    
    print(f"Текст 3: {get_text_color(s3, COLOR_WARNING)}")
    count3 = count_ivanushka(s3)
    print(f"Количество 'Иванушка': {get_text_color(count3, COLOR_GREEN)}\n")
    
    max_count = max(count1, count2, count3)
    if max_count == 0:
        print(get_text_color("Ни в одном тексте нет слова 'Иванушка'", COLOR_FAIL))
    else:
        texts = []
        if count1 == max_count:
            texts.append("1")
        if count2 == max_count:
            texts.append("2")
        if count3 == max_count:
            texts.append("3")
        print(f"Наибольшее количество 'Иванушка' в тексте(ах): {get_text_color(', '.join(texts), COLOR_WARNING)}")

def count_ivanushka(text: str) -> int:
    return len(re.findall(r'\bИванушка\b', text))

def _init_ex_4():
    print(get_text_color(TEXT_TASK_4, COLOR_WARNING))
    n = int(input_number("Введите N: ", min=1, max=20))
    m_values = []
    for i in range(5):
        m = int(input_number(f"Введите M{i+1} (0 <= M <= {n}): ", min=0, max=n))
        m_values.append(m)
    
    for m in m_values:
        counter = RecursionCounter()
        result = counter.combinations(m, n)
        print(f"C({m},{n}) = {result}, рекурсивных вызовов: {counter.count}")

class RecursionCounter:
    def __init__(self):
        self.count = 0
    
    def combinations(self, m: int, n: int) -> int:
        self.count += 1
        
        if m == 0 or m == n:
            return 1
        if 0 < m < n:
            return self.combinations(m, n-1) + self.combinations(m-1, n-1)
        return 0

def _init_ex_5():
    print(get_text_color(TEXT_TASK_5, COLOR_WARNING))
    words1 = ["Hello", "world", "from", "Python"]
    words2 = ["This", "is", "a", "test", "group", "410z"]
    
    join_words = lambda words: reduce(lambda x, y: f"{x} {y}", words)

    print(f"Список 1: {get_text_color(words1, COLOR_WARNING)}")
    print(f"Результат: '{get_text_color(join_words(words1), COLOR_GREEN)}'\n")
    print(f"Список 2: {get_text_color(words2, COLOR_WARNING)}")
    print(f"Результат: '{get_text_color(join_words(words2), COLOR_GREEN)}'")

def _init_ex_6():
    print(get_text_color(TEXT_TASK_6, COLOR_WARNING))
    separator = input_string("Введите разделитель: ")
    strings = []
    while True:
        s = input("Введите строку (пустая строка для завершения): ")
        if not s:
            if len(strings) >= 2:
                break
            else:
                print(get_text_color("Введите минимум две строки!", COLOR_FAIL))
                continue
            
        strings.append(s)
    
    print(f"Результат: {get_text_color(join_strings(separator, strings), COLOR_GREEN)}")

def join_strings(separator: str, strings: list) -> str:
    return separator.join(strings)

def main():
    while True:
        print(
            '\nЛарионов гр. 410з. Программирование на языках высокого уровня\n'
            'Индивидуальное задание №2 Функции. Вариант 3.\n'
        )
        print(f"{get_text_color(f'Какую задачу выполнить: ', COLOR_WARNING)}\n"
            f"{get_text_color(f'{_EX_1}) ', COLOR_WARNING)}{TEXT_TASK_1}"
            f"{get_text_color(f'{_EX_2}) ', COLOR_WARNING)}{TEXT_TASK_2}"
            f"{get_text_color(f'{_EX_3}) ', COLOR_WARNING)}{TEXT_TASK_3}"
            f"{get_text_color(f'{_EX_4}) ', COLOR_WARNING)}{TEXT_TASK_4}"
            f"{get_text_color(f'{_EX_5}) ', COLOR_WARNING)}{TEXT_TASK_5}"
            f"{get_text_color(f'{_EX_6}) ', COLOR_WARNING)}{TEXT_TASK_6}"
        )
        select = str(int(input_number('Для выхода введите \'0\'\n', min=0, max=6)))
        if select == '0':
            break
        else:
            globals()[f'_init_ex_{select}']()

        input('Для продолжения нажмите любую клавишу...')

if __name__ == '__main__':
    main()
