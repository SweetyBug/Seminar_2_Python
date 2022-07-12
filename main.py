#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def number(n):
    if int(n) == 0:
        return int(n)
    else:
        n = n.replace('.', '')
        n = n.replace('0', '')
        return int(n)

def sum(data, c):
    if data != 0:
        c += data % 10
        data = data // 10
        sum(data, c)
    else: 
        print(c)

count = 0
numb = input('Введите число: ')
numb = number(numb)
sum(numb, count)

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
def proizvedenie(numb, mas, i):
    if len(mas) < n:
        mas.append(i * mas[len(mas)-1])
        proizvedenie(numb, mas, i+1)
    else:
        print(mas)
n = int(input())
j = 2
arr = [1]
proizvedenie(n, arr, j)