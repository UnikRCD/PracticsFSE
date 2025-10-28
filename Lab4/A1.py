# -*- coding: utf-8 -*-

import random
import time

print ('Введите кол-во примеров:')
x = int(input())
all_time = 0
counter = 0
counter_que = 1

for i in range(x):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    print (f'Вопрос {counter_que}/{x}')
    print (f'{a} x {b} = ')

    while True: 
        try:
            start_time = time.time()
            otvet = int(input())
            time_spend = time.time() - start_time
            break 
        
        except ValueError: 
            print("Пожалуйста, введите целое число!")

    primer = a * b

    if otvet == primer:
        print (f'Верно! (Время: {time_spend:.1f}с)')
        counter += 1
        counter_que += 1
        all_time = all_time + time_spend
    else:
        counter_que += 1
        print (f'Неверно! Правильный ответ {primer} (Время: {time_spend:.1f}с')
        all_time = all_time + time_spend

procent = counter / x * 100
avarage_time = all_time / x

print (f'----------------------\n',
       'СТАТИСТИКА\n',
       '-----------------------\n',
       f'Общее время: {all_time:.1f}\n',
       f'Среднее время на вопрос: {avarage_time:.1f}\n',
       f'Кол-во правильных ответов: {counter}/{x}\n',
       f'Процент правильных ответов: {procent:.1f}%\n')