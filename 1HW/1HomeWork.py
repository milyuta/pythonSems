# Урок 1. Знакомство с Python
# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

day = int(input('day='))
if 1<=day<=5: print('нет, это будни')
elif 6<=day<=7: print('да, это выходной')
else: print ('введите правильные данные')


# 7. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#V - или
#л - и 





# 8. Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

# x = int(input('input the x-coordinate:'))
# y = int(input('input the y-coordinate:'))
# if x==0 or y==0: print('input right data')
# elif x>0 and y>0: print('it is the 1 quater')
# elif x>0 and y<0: print('it is the 2 quater')
# elif x<0 and y<0: print('it is the 3 quater')
# elif x<0 and y>0: print('it is the 4 quater')


# 9. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


# quat=int(input('input the number of the quater'))
# if quat==1: print('the diapasone of x-/y-coordinate is from 0 to infiniti')
# elif quat==2: print('the diapasone of x-coordinate is from 0 to infiniti and y-coordinate is from  minus infiniti to 0 ')
# elif quat==3: print('the diapasone of x-coordinate is from  minus infiniti to 0 and y-coordinate is from  minus infiniti to 0 ')
# elif quat==4: print('the diapasone of x-coordinate is from  minus infiniti to 0 and y-coordinate is from  from 0 to infiniti ')
# else: print('number of quarter cant be bigger than 4, try one more time')

# 10. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# x1 = float(input('input the x-coordinate of the 1 point:'))
# y1 = float(input('input the y-coordinate of the 1 point:'))
# x2 = float(input('input the x-coordinate of the 2 point:'))
# y2 = float(input('input the y-coordinate of the 2 point:'))
# length=((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))**0.5
# print('the distance between these points is:', length)