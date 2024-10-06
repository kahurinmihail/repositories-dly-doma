def merge_and_sort_lists(list1, list2):
    # Объединяем два списка
    merged_list = list1 + list2
    # Сортируем объединенный список
    sorted_list = sorted(merged_list)
    return sorted_list

# Ввод списков от пользователя
input_list1 = input("Введите элементы первого списка через запятую: ")
input_list2 = input("Введите элементы второго списка через запятую: ")

# Преобразуем ввод в списки
list1 = [int(x) for x in input_list1.split(",")] if input_list1 else []
list2 = [int(x) for x in input_list2.split(",")] if input_list2 else []

# Вызываем функцию и выводим результат
result = merge_and_sort_lists(list1, list2)
print(result)