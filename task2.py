# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
from pprint import pprint
from collections import Counter

my_text = list(input('Введите текст:').lower())
i = 0
# Я понимаю что можно было проще удалить точки и запятые, но мне так не хотелось сейчас в этом копаться :-)
# А еще если во вводимом тексте есть символ переноса строки, то будет обработан только текст до него.
x = my_text.count('.')
for i in range(x):
    my_text.remove('.')
y = my_text.count(',')
for i in range(y):
    my_text.remove(',')
my_text = ''.join(my_text)

# Может Вы подскажете: почему если в сплите между ковычками убираю пробел то выходит ошибка: ValueError: empty separator?
my_list = my_text.split(' ')
x = my_list.count('')
for i in range(x):
    my_list.remove('')
my_counter = Counter(my_list)
my_dict = {}
for i in my_counter.items():
    my_dict[i[0]] = i[1]
new_list = []
count = 1
for i in range(10):
    max = 0
    if count > 10:
        break
    for j in my_dict.items():
        if j[1] > max:
            max = j[1]
    for j in my_dict.items():
        if j[1] == max:
            new_list.append(j)
            count += 1
    for j in new_list:
        if j[0] in my_dict.keys():
            my_dict.pop(j[0])

for i in range(len(new_list)):
    print(f'{i + 1}. "{new_list[i][0]}" встречается {new_list[i][1]} раз')
