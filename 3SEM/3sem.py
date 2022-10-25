# Дарья Лютова: 19. Задайте список. Напишите программу, 
# которая определит, присутствует ли в заданном списке строк некое число.

# num = input('input the number')
# my_list = ['123', '4' , 'ghbdtn']
# flag= False 
# for i in my_list:  
#     if i==num: 
#         flag= True
# if flag==True: print(f'{num} is in the list') 
# else:print(f'{num} is not  in the list')



# 20.  Вывести список, содержащий средние арифметические значения чисел каждого вложенного кортежа в заданном кортеже кортежей numbers.


# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# my_list=[]
# for i in numbers:
#     my_list.append(sum(i)/len(i))
#     print(i)
# print(my_list)


#ущу одно решение
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

# def sum_tup(tup):
#     my_list = []
#     for row in tup:
#         my_list.append(sum(row)/len(row))
#     return my_list

# print(sum_tup(numbers))





# 21. Напишите программу, которая определит позицию второго 
# вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# num= str(input('input the num'))
# if num in my_list:
#     a=my_list.index(num)
#     for i in range(a+1,len(my_list)):
#         if my_list[i]== num:
#             print(i)
#             break
#         else: 
#             print(-1)
# else: print(-2)


#еще одно

# str1 = "qwe"
# str2 = "qwe", "asd", "zxc", "qwe", "ertqwe"

# def get_sec_entry(str1, str2):
#     start = str2.find(str1)
#     return str2.find(str1, start+1)

# print(get_sec_entry(string_1, string_2))

program = True

dictionary = {
1: {'name': 'Молоко', 'date': '12.04'},
2: {'name': 'Yoghurt', 'date': '5.07'},
3: {'name': 'meat', 'date': '3.07'},
4: {'name': 'eggs', 'date': '25..8'},
}

while program:
    print('1.View\n2. Add\n3. Remove\n4. Exit\n')
    choice = input('input parameter\n')

    if choice == '4':
        program = False
    
    if choice == '1':
        id = int(input('Input id: '))
        print(f'\n{dictionary[id]}\n')

    if choice =='2':
        id = int(input('\nInput id: '))
        name = input('\nInput name: ')
        date = input('\nInput date: ')
        dictionary[id]= {'name':name, 'date': date}
    
    if choice == '3':
        id = int(input('Input id:'))
        del dictionary[id]



