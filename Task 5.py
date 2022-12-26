# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

fib = int(input('Введите число: '))
res_5 = []
for i in range(fib+1):
    if i == 0:
        res_5.append(i)
    elif i == 1:
        res_5.append(i)
        res_5.insert(0, i)
    else:
        res_5.append(res_5[len(res_5)-1]+res_5[len(res_5)-2])
        res_5.insert(0, (-1)**(i-1)*res_5[len(res_5)-1])
print(res_5)
