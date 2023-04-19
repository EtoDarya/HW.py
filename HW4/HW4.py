def task1():
    number = int(input('Введите число:'))
    mnozhetely =[]
    for i in range(2, number):
        while number % i == 0:
                mnozhetely.append(i)
                number = number / i
    print(mnozhetely)

#task1()

def task2():
    assortiment = {"Сливочное", "Бурёнка", "Вафелька", "Сладкоежка"}
    sklad = {"Сливочное", "Вафелька", "Сладкоежка"}
    print(f'На складе отсутствует: {assortiment.difference(sklad)}')

#task2()

def task3():
    number = int(input('Введите число знаков после запятой:'))
    des = str(141592653589793238462643383279502884197169399375105820974944)
    py = des[0:number]
    
    print(f"3.{py}")

task3()