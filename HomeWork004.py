# # Вычислить число c заданной точностью d

import random

d = float(input('Задайте точность вычисления в виде дроби (0.01 или 0.1 или 0.0001 и т.д.) d = '))
count = 0
while d < 1:
    d *= 10
    count += 1
num1 = random.uniform(0, 100)
num2 = random.uniform(0, 100)
print(f'{num1} / {num2} = {round(num1 / num2, count)}')



                    # Решение однокурсника, тут находится для самостоятельного разбора

                    # from decimal import Decimal

                    # def rounding_accuracy(num, d):
                    #     number_in = Decimal(num)
                    #     print(number_in.quantize(Decimal(d)))

                    # number = float(input("Enter a real number: "))
                    # d = input("Enter the required accuracy '0.0001': ")
                    # rounding_accuracy(number, d)






# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))
if n > 0:
    multipliers = []
    while n > 1:
        for i in range(2, n + 1):
            count = True
            for j in range(2, i):
                if i % j == 0:
                    count = False
                    break
            if count:
                while n % i == 0:
                    multipliers.append(i)
                    n /= i
    print(multipliers)
else:
    print('Введено не натуральное число')



# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

n = int(input('Введите количество членов: '))
lst = []
for i in range(0, n):
    lst.append(random.randint(0, 20))
print(lst)
i = 0
while i < len(lst) - 1:
    count = len(lst)
    j = i + 1
    while j < len(lst):
        if lst[j] == lst[i]:
            lst.pop(j)
            j -= 1
        j += 1
    if count > len(lst):
        lst.pop(i)
        i -= 1
    i +=1
print(lst)



# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

def createEquation(value):
    lst = []
    equation = ' = 0'
    for i in range(0, value + 1):
        lst.append(random.randint(0, 100))
        if lst[i] != 0:
            if i == 0:
                equation = str(lst[i]) + equation
            elif i == 1:
                equation = str(lst[i]) + ' * x + ' + equation
            else:
                equation = str(lst[i]) + ' * x^' + str(i) + ' + ' + equation
    return equation

def writeFile(string, fileName):
    f = open(fileName, 'w')
    f.write(string)
    f.close()

k = int(input('Введите максимальную степень многочлена: '))
writeFile(createEquation(k), 'file1.txt')
writeFile(createEquation(k), 'file2.txt')



# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# Считываем уравнение из файла
def readFile(file):
    f = open(file, 'r')
    string = f.read()
    f.close()
    return string

# Записываем словарь, в котором ключ является степенью переменной Х, а значение ключа - множителем этой переменной
def readMultyplyers(string):
    lst = string.split()
# Записываем список множителей
    num_list = []
    for word in lst:
        if word.isnumeric():
            num_list.append(int(word))
# Записываем список степеней
    keys_list = []
    for i in range(0, len(string)):
        if string[i] == 'x' and string[i + 1] == '^':
            keys_list.append(int(string[i + 2]))
        elif string[i] == 'x' and string[i + 1] == ' ':
            keys_list.append(1)
    keys_list.append(0)
# Записываем словарь {степень: множитель}
    mu = {}
    for i in range(0, len(keys_list)):
        mu[keys_list[i]] = num_list[i]
# Проверка на отсутствие множителей, при отсутствии происходит добавление пары {степень: 0}
    for i in range(0, len(mu)):
        if mu.get(i) == None:
            mu[i] = 0

    return mu

# Сложение многочленов и вывод выражения на экран
def sumEquation(dict1, dict2):
    mult = {}
    for i in range(len(dict1)):
        mult[i] = dict1[i] + dict2[i]
    equation = ' = 0'
    for i in range(len(mult)):
        if mult[i] != 0:
            if i == 0:
                equation = str(mult[i]) + equation
            elif i == 1:
                equation = str(mult[i]) + ' * x + ' + equation
            else:
                equation = str(mult[i]) + ' * x^' + str(i) + ' + ' + equation
    print('Итоги сложения')
    print(equation)

print (readFile('file1.txt'))
print (readFile('file2.txt'))
sumEquation(readMultyplyers(readFile('file1.txt')), readMultyplyers(readFile('file2.txt')))
