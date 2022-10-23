# Знакомство с языком Python (семинары)
# Урок 3. Данные, функции и модули в Python
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# n = int(input("input the number: "))
# import random 
# my_list = [random.randint(0, 2*n) for i in range(n)]
# print(my_list) 

# sum = 0
# for i in range(1,n,2):
#     sum += my_list[i]
    
# print(f'sum of the uneven elements is : {sum}') 


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# n = int(input('input the random nuber: '))
# import random
# nums = [random.randint(1, n) for i in range(1, n+1)] 
# print(nums)
# antinums=nums[::-1]
# print(antinums)

# res=[]
# for i in range(n):
#     if i>=n//2:
#         break
#     res.append(nums[i]*antinums[i])
# print(res)



# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# new_list = []
# for i in my_list:
#     num=round(i%int(i),5)
#     new_list.append(num)

# new_list.remove(0)
# print(max(new_list)-min(new_list))



# 4. Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def find_digit(num):
#     num = int(input('input the decimal number: '))
#     temp = num
#     res=[]
#     while temp/2>0:
#         res.append(temp%2)
#         temp=temp//2
#     antires=list(reversed(res))

#     result = ''
#     for i in antires:
#         result += str(i)
#     print(result)
#     return find_digit

# find_digit(0)



# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)



# def fib(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         a, b = b, a + b
#     return a

# def neg_fib(n):
#     a = 0
#     b = 1
#     for i in range(-n):
#         a, b = b,a - b
#     return a

# num = int(input('input the coefficient: '))
# fibb_list = []
# for i in range(-num,num+1):
#     if i<0:
#         fibb_list.append(neg_fib(i)) 
#     if i>=0:
#         fibb_list.append(fib(i)) 
# print(fibb_list) 
