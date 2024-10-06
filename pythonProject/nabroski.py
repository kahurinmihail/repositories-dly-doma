#print ("Hello mazafaka2 ",5,7,9,".", sep="|")
# комментарий
#print ("текст после комментария")
#print ('Result :',5+5)

#input ("ВВЕДИ СВОЙ ВОЗРАСТ Ссынок: ")

#NUM1 = int(input ("Напиши любой символ : "))
#print (NUM1)
#print (NUM1*2)
#print (NUM1*3)
#print (NUM1*4)
#print (NUM1*5)
#sun = int(input("введи число: "))
#for fak in sun:
#    print (fak)
#n = 0
#while n < sun:
#    n += 1
#    print(n)
#sun = [1,2,3,4,5]
#sun.append (2)
#sun.sort()
#print (sun)
# 3. Пользователь подаёт на ввод список из чисел, необходимо вывести список, состоящий только из чётных чисел (append)

#задание 3
#num = input("Введите список числа через пробел : ").split() # Пишем список чисел
#spisok_chetnih_chisel= []#Создаем пустой список для хранения четных чисел
#for number in num: # Проходим по каждому элементу списка введенных чисел
#    number = int(number) # Преобразуем элемент в число
#    if number % 2 == 0: # Проверяем, является ли число четным
#        spisok_chetnih_chisel.append(number) # Если число четное, добавляем его в список четных чисел
#print("Список четных чисел:", spisok_chetnih_chisel) # Выводим список четных чисел

#word = input("Введите слово: ")

# Переводим слово в нижний регистр, чтобы учитывать различия в регистре букв
#word = word.lower()

# Проверяем, является ли слово палиндромом

#a = [1,34,52,18,19,20]
#print(len(a))
#for i in range (0, 6):
#    a[i]+=10
#    print(a[i])

# Создание документа
#var= input('Напиши что нибудь')
#fw = open ('documents/file.txt', 'a')
#fw.write('Hello mazafaka\n')
#fw.write(var)
#fw.close()
# a - запись новых данных в файл
# w - запись новых данных в файл но с удалением старых
# R - read - чтение файла


def merge_and_sort_list (list1, list2):
    merge = list1 +list2
    sorteds = sorted(merge)
    return sorteds

input_list1 = input ("Введи числа 1 списка через запятую")
input_list2 = input ("Введи числа 2 списка через запятую")

list1 = [int(x) for x in input_list1.split(",")] if input_list1 else []
list2 = [int(x) for x in input_list2.split(",")] if input_list2 else []

result = merge_and_sort_list(list1, list2)
print(result)