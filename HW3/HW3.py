def task1():
    number = int(input('Введите число:'))
    count = 0
    fibanacchi = [1, 1]
    for i in range(number-2):
        count = fibanacchi[i] + fibanacchi[i+1]
        fibanacchi.append(count)
    print(fibanacchi)

#task1()

def task2():
    fruits = {'абрикос', 'яблоко', 'мандарин', 'апельсин', 'айва', 'авокадо', 'манго', 'персик', 'груша', 'банан', 'инжир', 'лимон', 'слива', 'гранат', 'маракуйя', 'грейпфрут', 'киви', 'дыня', 'папайя', 'физалис', 'личи'}
    letter = input('Введите букву: ')
    letter_fruits = []
    for i in fruits:
        if i[0] == letter:
            letter_fruits.append(i)
    print(f'Выборка фруктов на букву "{letter}": {letter_fruits}')

#task2()

def task3():
    print (f"Здравствуй! Я бот для общения. Можешь поболтать со мной.\nЕсли хочешь узнать, на какие вопросы я умею отвечать, напиши 'на что ты умеешь отвечать'.\nЕсли хочешь чему-то меня научить, напиши 'хочу научить тебя'.")
    phrases = {"привет": "Здравствуй, пользователь!",
               "как тебя зовут": "Меня зовут Бот",
               "какой твой любимый цвет": "Я обожаю зеленый!",
               "какие фильмы ты любишь": "Фильмы ужасова просто блеск!",
               "сегодня такая плохая погода": "Да, мне тоже не нравится...",
               "какие у тебя хобби": "Я люблю читать и рыбачить."}
    flag = True
    while flag:
        key = input('Что Вы хотите сказать?: ')
        if key.lower() in phrases:
            print(phrases[key])
        elif key.lower() == "пока":
            print('До встречи!')
            flag = False 
        elif key.lower() == "на что ты умеешь отвечать":
            for key in phrases.keys():
                print(key)
        elif key.lower() == "хочу научить тебя":
            key = input('На что я буду отвечать?: ')
            phrases[key] = input('Что я буду на это отвечать?: ')
        elif key.lower() not in phrases:
            print('Я не знаю, что на это ответить :(')

        
task3()