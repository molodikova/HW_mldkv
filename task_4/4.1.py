from itertools import count
from functools import reduce
import math


# Квадраты всех четных чисел (используя map и filter)
def squared(x): return x ** 2


def even(x): return x % 2 == 0


some_list = list(range(1, 11))
result = list(map(squared, filter(even, some_list)))
print(result)

# Дана входная строка и массив чисел, необходимо вернуть строку
# с теми буквами, которые стоят на указанных местах (два
# варианта, используя и не используя list comprehensions)
string = "Hello everybody!"
ind_list = list(range(1, 14, 3))
res_non_list = []
for i in ind_list:
    res_non_list.append(string[i])

print("list comprehensions: ", ''.join([string[i] for i in ind_list]), "\nnon-list comprehensions: ",
      ''.join(res_non_list))

# Дан текст (предложения разделены только точками), в котором
# буквы могут находиться в разных регистрах. Необходимо вернуть
# текст, в котором все буквы в нижнем регистре, а первые буквы
# каждого предложения – в верхнем. Пользоваться можно
# встроенными функциями строки (кроме capitalize J), всеми
# изученными в этой теме функциями и модулем itertools.
text = "темНО.мнE не Спится.ОченЬ хоЧется еСТЬ.нО Я ДеРжуСь."
_text = text.lower()
res_text = [_text[0].upper()]
for i in count(1, 1):
    if i > len(text) - 1:
        break
    else:
        if _text[i - 1] == ".":
            res_text.append(_text[i].upper())
        else:
            res_text.append(_text[i])
print(''.join(res_text))

# functools.reduce
num_list = [1, 7, 3, 2, 2, 9, 0]
print("Максимальный элемент: ", reduce(lambda x, y: x if x > y else y, num_list))


# Задание:
# ◦ создайте функцию pipeline_each, в которую вы будете подавать
# итерируемый объект и список функций, которые последовательно
# надо к нему применить.
# Ответ – объект после применения функций в указанном порядке.
def pipeline_each(iterable, func):
    for f in func:
        for ind, obj in enumerate(iterable):
            iterable[ind] = f(obj)
    return iterable


iter_ob = ['  иванов вадим ', '  еремеев услан']
print(pipeline_each(iter_ob, [str.strip, str.title]))


# Написать генератор, возвращающий по очереди все слова,
# входящие в предложение.
def generator(words):
    for word in words:
        yield word


some_words = 'А судьи кто?'
gen = generator(some_words.split())
for i in gen:
    print(i)


# Написать генератор псевдо случайных чисел
# ◦ Генератор внутри задается какой-нибудь формулой, которая выдает
# «случайный» результат
# ◦ На вход генератору приходит seed – начальное значение, при
# одинаковых начальных значениях два генератора будут выдавать
# одинаковые следующие значения
def random(seed):
    f = lambda x: math.trunc((x * math.tau) * math.pi * math.e % 100000)
    while True:
        seed = f(seed)
        yield seed


ran = random(48)
for i in range(3):
    print(next(ran))


# Написать корутину, которая реализует бесконечную
# арифметическую прогрессию с возможностью перезапуска с
# любого места (3, 4, 5, 6, send(30), 31, 32, 33, …)
def arith_progression():
    x = 0
    while True:
        val = (yield x)
        if val is not None:
            x = val
        else:
            x += 1


pro = arith_progression()
for i in range(3):
    print(next(pro))
pro.send(23)
print(next(pro))
