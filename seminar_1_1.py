# Возвести число в квадрат
# a = int(input())
# print(a**2)

# Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.
# a = int(input('A: '))
# b = int(input('B: '))

# if a**2 == b or b**2 == a:
#     print('Является')
# else:
#     print('Не является')


# Написать программу, которая на вход принимает
# 5 чисел и находит максимальное


# a = input().split()
# print(a)
# max = int(a[0])
# for i in range(len(a)):
#     if int(a[i]) > max:
#         max = int(a[i])
# print(max)


# for i in range(6,0,-1): # можно в обратную сторону ходить по листу
#     print(i)

# a = list(map(float, input().split())) # то же самое через функцию max
# print(max(a))

# Напишите программу, которая будет на вход принимать число
#  N и выводить числа от -N до N
a = []
b = ''
n = int(input())
for i in range(-n,n+1):
    a.append(i) # добавляет в конец списка а 
    print(f'{i} ',end = ' ') # end= '' будет выводить в список чере ''
    b += f'{i} '
print()
print(a)
print(b)