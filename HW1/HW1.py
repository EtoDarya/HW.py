def task1():
    week = ['Понедельник','Вторник', 'Среда','Четверг','Пятница','Суббота','Воскресенье']
    n = int(input('Введите число:'))
    n = n - 1
    count = 0
    if n > 7 or n < 0:
        print('Такого дня недели нет')
    for i in week:
        if count != n:
            count+=1
        else:
            print(week[count])    
    
# task1()


def task2():
    import math
    A1 = int(input('Введите первую координату первой точки:'))
    A2 = int(input('Введите вторую координату первой точки:'))
    B1 = int(input('Введите первую координату второй точки:'))
    B2 = int(input('Введите вторую координату второй точки:'))
    print(round((math.sqrt((B1-A1)**2 + (B2-A2)**2)), 2))

# task2()

def task3():
    n = int(input('Введите номер четверти:'))
    if n == 1:
        print('x > 0, y > 0')
    if n == 2:
        print('x < 0, y > 0')
    if n == 3:
        print('x < 0, y < 0')
    if n == 4:
        print('x > 0, y < 0')
    else:
        print('Такой четверти нет')

# task3()

def task4():
    n = int(input('Введите число:'))
    for i in range(1, n):
        if i % 2 == 0:
            print(i, end =', ')

# task4()