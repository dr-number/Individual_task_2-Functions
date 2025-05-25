## Ларионов гр. 410з. Программирование на языках высокого уровня
## Индивидуальное задание №2 Функции. Вариант 3.
1. Оформить функцию поиска количества элементов равных 5. В главной
программе дано 3 одномерных массива p, q, r длиной 10 элементов
каждый. Применить функцию для каждого из 3 -х заданных массивов.
<figure>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_2-Functions/blob/main/for_read_me/1-count_five.png">
   </p>
</figure>

2. Оформить функцию поиска номера последнего нулевого элемента в
массиве. В главной программе дано 3 одномерных массива a, b, c длиной
20 элементов каждый. Применить функцию для каждого из 3-х заданных
массивов. Найти сумму найденных номеров элементов.
<figure>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_2-Functions/blob/main/for_read_me/2-summ_indexes_last_zero.png">
   </p>
</figure>

3. Описать функцию, вычисляющую количество слов «Иванушка» в тексте.
В главной программе дано 3 текста S1, S2, S3. Выяснить, в каком тексте
больше слов «Иванушка», используя функцию.
<figure>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_2-Functions/blob/main/for_read_me/3-count-ivanushka.png">
   </p>
</figure>

4. Описать рекурсивную функцию C(m,n) целого типа, находящую число
сочетаний из n элементов по m, используя формулу: C(0,n) = C(n,n) = 1,
C(m,n) = C(m,n–1) + C(m–1,n–1) при 0 < m < n (m и n — целые параметры;
n > 0, 0 <= m <= n). Дано число N и пять различных значений M. Вывести
числа C(M,N) вместе с количеством рекурсивных вызовов функции C,
потребовавшихся для их нахождения.
<figure>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_2-Functions/blob/main/for_read_me/4-combinations.png">
   </p>
</figure>
<figure>
   <p align="center">Проверка на ошибки допущенные при вводе данных</p>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_2-Functions/blob/main/for_read_me/4-error-error-imput.png">
   </p>
</figure>

5. Описать lambda-функцию с reduce(), чтобы объединить строки, добавляя
между ними пробел. В программе создайте 2 списка слов и используя
вашу функцию объедините их в предложение.
<figure>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_2-Functions/blob/main/for_read_me/5-join_words.png">
   </p>
</figure>

6. Напишите функцию, которая принимает разделитель и произвольное
количество строк, а затем возвращает объединенную строку с
использованием переданного разделителя.
<figure>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_2-Functions/blob/main/for_read_me/6-join_strings.png">
   </p>
</figure>
<figure>
   <p align="center">Проверка на ошибки допущенные при вводе данных</p>
   <p align="center">
      <img src="https://github.com/dr-number/Individual_task_2-Functions/blob/main/for_read_me/6-error-input.png">
   </p>
</figure>

# Create venv:
    python3 -m venv venv

# Activate venv:
## In Windows:
    venv\Scripts\activate
     
## In macOS or Linux:
    source venv/bin/activate

# install library
    pip install -r requirements.txt

# start 
## In macOS or Linux:
    ./venv/bin/python "main.py"

## In Windows:
    .\myenv\Scripts\python main.py