import json
import numpy
from numpy import genfromtxt

user_id = int(input("Введите id пользователя "))

#Для расчета оценок использовать подход user-based коллаборативной фильтрации, метод kNN
k = 4

#Читаем файл и записываем в массив
data = genfromtxt('data.csv', delimiter=',')
#print(data[5][1])

#Словарь оценок схожести
sim = {}
for u in range(41):
    if u==user_id or u==0:
        continue
    divisible, divisor1, divisor2 = 0, 0, 0
    for m in range(31):
        if data[u][m]==-1 or data[user_id][m]==-1 or m==0:
            continue
        divisible += data[u][m]*data[user_id][m]
        divisor1 += data[u][m] ** 2
        divisor2 += data[user_id][m] ** 2
    sim[u] = round(divisible / ((divisor1 ** 0.5) * (divisor2 ** 0.5)), 3)

sorted_sim = sorted(sim.items(), key=lambda kv: kv[1], reverse=True)
#print(sorted_sim[0][0])

#Средняя оценка пользователей
avg_grade = {}
for u in range(41):
    if u==0:
        continue
    divisible, count = 0, 0
    for m in range(31):
        if data[u][m]==-1 or m==0:
            continue
        divisible += data[u][m]
        count += 1
    avg_grade[u] = round(divisible / count, 3)
#print(avg_grade)

#Словарь расчётных оценок пользователя для фильма
final_grade = {}
for m in range(31):
    if m==0 or data[user_id][m]!=-1:
        continue
    divisible, sum_sim = 0, 0
    for i in range(4):
        divisible += sorted_sim[i][1]*(data[sorted_sim[i][0]][m] - avg_grade[sorted_sim[i][0]])
        sum_sim += abs(sorted_sim[i][1])
    final_grade[m] = round(avg_grade[user_id] + (divisible / sum_sim),3)
#print(final_grade)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(final_grade, f, ensure_ascii=False, indent=4)
