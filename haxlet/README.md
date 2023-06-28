
<b>Два года рождения (<a href="haxlet/get_age_difference.py">get_age_difference.py</a></b>)
Условие: 
Напишите функцию get_age_difference(), которая принимает два года рождения и возвращает строку 
с разницей в возрасте в виде The age difference is 11.

Пример работы функции:
actual = get_age_difference(2001, 2018)
print(actual)  # => The age difference is 17
---

<b>Cодержит ли строка заглавные буквы (<a href="haxlet/has_upper_case.py">has_upper_case.py</a></b>)

Условие: Реализуйте функцию has_upper_case(), которая определяет, содержит ли строка заглавные буквы. 
Функция должна вернуть булево значение:

has_upper_case('')  # False
has_upper_case('python')  # False
has_upper_case('pyThon')  # True

Подсказка
Воспользуйтесь методом из стандартной библиотеки, который приводит строку к нижнему регистру. 
Обратите внимание, чем отличается такая строка от исходной.
---

<b>Является ли год високосным. (<a href="haxlet/is_leap_year.py">is_leap_year.py</a></b>)

Условие: Реализуйте функцию is_leap_year(), которая определяет, является ли год високосным. 
Год будет високосным, если он делится без остатка на 400, или он одновременно делится без остатка
 на 4 и не делится на 100:

is_leap_year(2018)  # False
is_leap_year(2017)  # False
is_leap_year(2016)  # True
---

<b>Повторить символ в слове (<a href="haxlet/letter_multiply.py">letter_multiply.py</a></b>)

Условие: Реализуйте функцию letter_multiply(). Она должна принимать три параметра:
    Строку
    Символ
    Число, которое обозначает, сколько раз нужно повторить символ в слове
text = 'python'
print(letter_multiply(text, 'p', 2)) # => ppython
print(letter_multiply(text, 'y', 3)) # => pyyython
print(letter_multiply(text, 'n', 4)) # => pythonnnn
Укажите аннотации типов при объявлении функции.
Подсказка
Для замены символов в строке воспользуйтесь методом replace()
---
