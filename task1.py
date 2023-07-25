# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 2, 3, 4, 2, 5, 4, 6, 7, 8, 9, 1]
new_list = []

for i in my_list:
    if my_list.count(i) >= 2 and i not in new_list:
        new_list.append(i)

print(new_list)