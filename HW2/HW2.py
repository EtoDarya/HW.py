def task1():
    n = int(input('Введите число:'))
    f = 1
    for i in range(1,n+1):
        f = f * i
        print(f, end = ', ')

# task1()

def task2():
    for x in range(0, 2):
        for y in range(0,2):
            for z in range(0,2):
                print (f'{x} {y} {z} = {int(not(x==1 and y==1) or z == 1)}')

# task2()

def task3():
    string_1 = input('Введите первую строку: ')
    string_2 = input('Введите вторую строку: ')
    length_string_1 = len(string_1)
    length_string_2 = len(string_2)
    count = 0
    for j in range(length_string_1):
        for i in range(length_string_2):
            if string_2[i] == string_1[j]:
                count +=1
        print(f'{string_1[j]} = {count}')
        count = 0

# task3()

def task4():
    n = int(input('Введите число:'))
    n = abs(n)
    numbers = []
    numbers_new = []
    j = len(numbers)
    for i in range(-n, n + 1):
        numbers.append(i)
    for j in range(-2, len(numbers)-2):
        numbers_new.append(numbers[j])
    print(numbers)
    print(numbers_new)

# task4()

            