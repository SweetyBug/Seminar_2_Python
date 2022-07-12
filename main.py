#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def number(n):
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


