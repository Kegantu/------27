n = int(input("Введіть кількість елементів масиву: "))
array = list(map(float, input("Введіть елементи масиву через пробіл: ").split()))

def findClosestPair(a):
    min_diff = abs(a[1] - a[0])
    idx = 0

    for i in range(1, len(a) - 1):
        diff = abs(a[i + 1] - a[i])
        if diff < min_diff:
            min_diff = diff
            idx = i

    return a[idx], a[idx + 1], min_diff

if len(array) != n:
    print("Помилка: кількість введених елементів не дорівнює n.")
elif n < 2:
    print("Потрібно щонайменше 2 елементи.")
else:
    x1, x2, diff = findClosestPair(array)

    print("Найближча пара:", x1, "і", x2)
    print("Мінімальна різниця |xi+1 - xi| =", diff)