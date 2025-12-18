n = int(input("Введіть кількість елементів масиву: "))
array = list(map(float, input("Введіть елементи масиву через пробіл: ").split()))

if len(array) != n:
    print("Помилка: кількість введених елементів не дорівнює n.")
elif n < 2:
    print("Потрібно щонайменше 2 елементи.")
else:
    minDiff = abs(array[1] - array[0])
    idx = 0

    for i in range(1, n - 1):
        diff = abs(array[i + 1] - array[i])
        if diff < minDiff:
            minDiff = diff
            idx = i

    print("Найближча пара:", array[idx], "і", array[idx + 1])
    print("Мінімальна різниця |xi+1 - xi| =", minDiff)