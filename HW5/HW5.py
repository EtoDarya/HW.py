import random

def task1():
  num = [random.randint(1, 10) for i in range(15)]
  result = list(filter(lambda x: x >5 , num))
  print(num)
  print(result)

#task1()

def task2():
    nums = [random.randint(1, 10) for i in range(10)]
    print(nums)
    rand_index = random.randint(0, len(nums)-1)
    #print(rand_index, nums[rand_index])
    spisok = [nums[rand_index]]
    for i in range(rand_index, len(nums)):
        if nums[rand_index] < nums[i]:
            nums[rand_index] = nums[i]
            spisok.append(nums[i])
    print(spisok)

#task2()

def task3():
   num = [random.randint(1, 10) for i in range(5)]
   print(num)
   count = 0
   for x in num:
        if num.count(x) > 1:
            count +=1
   result = set(num)
   print(f'Список уникальных элементов: {result}')
   print(f'Количество совпадающих элементов {count}')

task3()