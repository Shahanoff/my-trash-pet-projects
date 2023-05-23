import random

# начальные вероятности всех чисел
probability = {i: 1 / 37 for i in range(37)}

# список выпавших чисел
result = []

# количество итераций
n_iter = 1000

for i in range(n_iter):
    # выбираем случайное число от 0 до 36
    num = random.randint(0, 36)

    # если число еще не выпадало, добавляем его в список
    if num not in result:
        result.append(num)

    # обновляем вероятности выпадения оставшихся чисел
    for j in range(37):
        if j not in result:
            probability[j] = (1 - (len(result) - 1) / 36) * probability[j]

    # выводим выпавшее число и вероятности для данной итерации
    print(f'Итерация {i + 1}:')
    print(f'Выпало число {num}')
    for j in range(37):
        print(f'Число {j}: вероятность {probability[j]}')

    # если выпали все числа кроме одного, останавливаем цикл
    if len(result) == 36:
        print(f'Осталось число {set(range(37)) - set(result)}.')
        break
