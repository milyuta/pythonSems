# Знакомство с языком Python (семинары)
# Урок 2. Знакомство с Python. Продолжение
# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# num = input('input the number: ')
# sum = 0
# if float(num)<0:
#     num = float(num)*(-1)
# for i in str(num):
#     if i!= '.':
#         sum +=int(i)
# print(sum)


# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input("input the number: "))
# my_list = []
# i=1
# m=1
# while i<=N:
#     m=m*i
#     my_list.append(m)
#     i+=1
# print(my_list)   


# 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

# N = int(input("input the number: "))
# my_list = []
# i=1
# sum=0
# while i<=N:
#     m=round((1+1/i)**i,2)
#     sum=sum+m
#     my_list.append(m)
#     i+=1
# print(f'For N= {N}:{my_list}')
# print(f'{sum}')



# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на введенных пользователем позициях.

# import random   #создает лист, из n элементов, заполненный от -n до n
# n = int(input('Input the number: '))
# my_list = [random.randint(-n, n) for i in range(n)]
# print(my_list)

# i= int(input('input the count of your elements: ')) #создает лист с номерами индексов позиций из my_list, которые будем перемножать
# new_list = []
# for j in range(1,i+1):
#     new_list.append(int(input('Input the position: ')))
# print(new_list)

# comp=1
# for k in new_list:
#     comp = comp*my_list[k]
# print(comp)




# 18. *Реализуйте алгоритм перемешивания списка.

# import random
# n = int(input('Input the number: '))
# my_list = [random.randint(-n, n) for i in range(n)]
# print(my_list)
# random.shuffle(my_list)
# print(my_list)