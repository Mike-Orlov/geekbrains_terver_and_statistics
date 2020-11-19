import numpy as np
from math import factorial

"""
1. Даны значения зарплат из выборки выпускников:
100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
Посчитать (желательно без использования статистических методов наподобие std, var, mean)
среднее арифметическое, среднее квадратичное отклонение,
смещенную и несмещенную оценки дисперсий для данной выборки.
"""

salaries = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

def my_mean(salaries):
    return sum(salaries)/salaries.shape[0]

def my_std(salaries):
    deviations = np.array([salary - my_mean(salaries) for salary in salaries])
    return np.sqrt(sum(deviations**2)/deviations.shape[0])  # pylint: disable=E1136  # pylint/issues/3139

def unbiased_var(salaries):
    deviations = np.array([salary - my_mean(salaries) for salary in salaries])
    return sum(deviations**2)/(deviations.shape[0] - 1)  # pylint: disable=E1136  # pylint/issues/3139

def biased_var(salaries):
    deviations = np.array([salary - my_mean(salaries) for salary in salaries])
    return sum(deviations**2)/(deviations.shape[0])  # pylint: disable=E1136  # pylint/issues/3139

print(f'1. Mean salary: {my_mean(salaries)}')
print(f'Standard deviation: {my_std(salaries):.2f}')
print(f'Unbiased variance estimate: {unbiased_var(salaries):.2f}')
print(f'Biased variance estimate: {biased_var(salaries):.2f}')
print()

"""
2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?
"""

def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

result = (combinations(5,2)/combinations(8,2)*combinations(5,1)*combinations(7,3)/combinations(12,4) +               # Вариант, когда 2 белых в 1 корзине и 1 белый во 2-ой
    combinations(5,1)*combinations(3,1)/combinations(8,2)*combinations(5,2)*combinations(7,2)/combinations(12,4) +  # Вариант, когда 1 белый в 1 корзине и 2 белых во 2-ой
    combinations(3,2)/combinations(8,2)*combinations(5,3)*combinations(7,1)/combinations(12,4))                      # Вариант, когда 0 белых в 1 корзине и 3 белых во 2-ой

print(f'2. Probability of drawing 3 white balls: {result:.2%}')
print()

"""
3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
Найти вероятность того, что выстрел произведен:
a) первым спортсменом;
б) вторым спортсменом;
в) третьим спортсменом.
"""
# Использую формулу Байеса, т.к. ищем вероятность В (выстрела одного из спортсменов), при условии что событие А (попадание) произошло

B1, B2, B3 = 1/3, 1/3, 1/3
A1, A2, A3 = 0.9, 0.8, 0.6

print(f'3. Probability that the 1st athlete shot: {A1*B1 / (A1*B1 + A2*B2 + A3*B3):.2%}') 
print(f'Probability that the 2nd athlete shot: {A2*B2 / (A1*B1 + A2*B2 + A3*B3):.2%}') 
print(f'Probability that the 3rd athlete shot: {A3*B3 / (A1*B1 + A2*B2 + A3*B3):.2%}') 
print()

"""
4. В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же,
сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию.
Какова вероятность, что он учится:
a) на факультете A;
б) на факультете B;
в) на факультете C?
"""
# Также использую формулу Байеса

B1, B2, B3 = 1/4, 1/4, 1/2 # Соответственно вероятности для факультетов A, B, C
A1, A2, A3 = 0.8, 0.7, 0.9

print(f'4. Probability that student from A faculty: {A1*B1 / (A1*B1 + A2*B2 + A3*B3):.2%}') 
print(f'Probability that student from B faculty: {A2*B2 / (A1*B1 + A2*B2 + A3*B3):.2%}') 
print(f'Probability that student from C faculty: {A3*B3 / (A1*B1 + A2*B2 + A3*B3):.2%}') 
print()

"""
5. Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2,
для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя:
а) все детали;
б) только две детали;
в) хотя бы одна деталь;
г) от одной до двух деталей?
"""

x, y, z = 0.1, 0.2, 0.25

print(f'5. All parts: {x*y*z:.2%}') 
print(f'Only 2: {x*y*(1-z) + y*z*(1-x) + x*z*(1-y):.2%}') 
print(f'At least 1: {x*y*z + x*y*(1-z) + y*z*(1-x) + x*z*(1-y) + x*(1-y)*(1-z) + y*(1-x)*(1-z) + z*(1-x)*(1-y):.2%}') 
print(f'Only 1 or 2: {x*y*(1-z) + y*z*(1-x) + x*z*(1-y) + x*(1-y)*(1-z) + y*(1-x)*(1-z) + z*(1-x)*(1-y):.2%}') 