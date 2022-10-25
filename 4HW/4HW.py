# Знакомство с языком Python (семинары)
# Урок 4. Данные, функции и модули в Python. Продолжение
###### 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, 
# что при хранении данных используется принцип: одна строка — один пользователь. 
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt. 
# Фрагмент файла с данными о пользователях (users.txt):
# Иванов Иван Иванович
# Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt):
# скалолазание, охота
# горные лыжи

# file_1 = open('users.txt', 'r', encoding='utf8')
# users = file_1.readlines()
# users = [line.rstrip() for line in users]

# file_1.close()

# file_2 = open('hobby.txt', 'r', encoding='utf8')
# hobbies = file_2.readlines()
# hobbies = [line.rstrip() for line in hobbies]

# file_2.close()

# users_hobby=dict(zip(users, hobbies))
# print(users_hobby)

# with open('users_hobby.txt', 'w', encoding='utf8') as out:
#     for key, value in users_hobby.items():
#         out.writelines(f'{key}: {value}\n')
           

######## 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# N = int(input("input the number: "))

# simp_list=[]
# res_list = []

# for i in range(2, N):
#     for j in simp_list:
#         if i % j == 0:
#             break
#     else:
#         simp_list.append(i)

# for i in simp_list:
#     if N%i==0:
#         res_list.append(i)

# print(res_list)



# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# import random
# n = int(input('Input the number: '))
# my_list = [random.randint(0, n) for i in range(n)]
# print(my_list)

# new_list = []
# [new_list.append(i) for i in my_list if i not in new_list]
# print(f"Your list is: {new_list}")


#### 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

# k = int(input('input the degree: '))
# import random
# n=100
# a = random.randint(0, n)
# b = random.randint(0, n)
# c = random.randint(0, n)
# print(f'{a}*x**{k} + {b}*x + {c}=0')
# my_list = [f'{a}*x**{k} + {b}*x + {c}=0']

# with open('polinomial.txt', 'w') as out:
#     out.writelines(' '.join(my_list))




##### 34. *Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0

# import re

# file_1 = open('1polinomial.txt', 'r', encoding='utf8')
# polinomial1 = file_1.read()

# p1_1,p1_2,p1_3,p1_4,p1_5,p1_6,p1_7,p1_8,p1_9,p1_10,p1_11=re.split('[+*x=0,]', polinomial1)
# file_1.close()

# file_2 = open('2polinomial.txt', 'r', encoding='utf8')
# polinomial2 = file_2.read()
# p2_1,p2_2,p2_3,p2_4,p2_5,p2_6,p2_7,p2_8,p2_9,p2_10,p2_11=re.split('[+*x=0,]', polinomial2)
# file_2.close()

# res_polinomial=(f'{int(p1_1)+int(p2_1)}*x**2+{int(p1_6)+int(p2_6)}*x+{int(p1_9)+int(p2_9)}=0')

# with open('res_polinomial.txt', 'w', encoding='utf8') as out:
#     out.writelines(' '.join(res_polinomial))

