import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from collections import Counter

def load_users_data():
    try:
        users_tree = ET.parse('users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
                'user_id': int(user_elem.find('user_id').text),
                'name': user_elem.find('name').text,
                'age': int(user_elem.find('age').text),
                'weight': int(user_elem.find('weight').text),
                'fitness_level': user_elem.find('fitness_level').text,
                'workouts': []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")
        return []

def load_workouts_data():
    try:
        workouts_tree = ET.parse('workouts.xml')
        workouts = []
        for workout_elem in workouts_tree.getroot().findall('workout'):
            workout = {
                'workout_id': int(workout_elem.find('workout_id').text),
                'user_id': int(workout_elem.find('user_id').text),
                'date': workout_elem.find('date').text,
                'type': workout_elem.find('type').text,
                'duration': int(workout_elem.find('duration').text),
                'distance': float(workout_elem.find('distance').text),
                'calories': int(workout_elem.find('calories').text),
                'avg_heart_rate': int(workout_elem.find('avg_heart_rate').text),
                'intensity': workout_elem.find('intensity').text,
            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Файл не найден")
        return []

users = load_users_data()
workouts = load_workouts_data()
    
def get_stats(users, workouts):
    all_workouts = len(workouts)
    all_users = len(users)
    all_calories = sum(workout['calories'] for workout in workouts)
    all_time = float(sum(workout['duration'] for workout in workouts) / 60)
    all_distance = float(sum(workout['distance'] for workout in workouts))
    text = f'''ОБЩАЯ СТАТИСТИКА
=================================
Всего тренировок: {all_workouts}
Всего пользователей: {all_users}
Сожжено калорий: {all_calories}
Общее время: {all_time:.1f} часов
Пройдено дистанции: {all_distance:.1f} км
'''
    return text

def analyze_user_activity(users, workouts):
    
    user_stats = []
      
    for user in users:
        user_workouts = [workout for workout in workouts if workout['user_id'] == user['user_id']]
        
        all_workouts = len(user_workouts)
        all_calories = sum(workout['calories'] for workout in user_workouts)
        all_duration = float(sum(workout['duration'] for workout in user_workouts)/60)

        stats = ({
            'user_id': user['user_id'],
            'name': user['name'],
            'all_workouts': all_workouts,
            'all_calories': all_calories,
            'all_time': all_duration,
        })
        
        user_stats.append(stats)
        
        top_users = sorted(user_stats, key=lambda x: x['all_workouts'], reverse=True)[:3]
        
    print("\nТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ")
    print("=" * 50)
    for i, user in enumerate(top_users, 1):
        print(f"{i}. {user['name']}")
        print(f"Тренировок: {user['all_workouts']}")
        print(f"Калорий: {user['all_calories']}")
        print(f"Время: {user['all_time']:.2f} часов\n")

def analyze_workout_types(workouts):
    stats = {}
    all_workouts = len(workouts)
    
    for workout in workouts:
        workout_type = workout['type']
        duration = workout['duration']
        calories = workout['calories']
        
        if workout_type not in stats:
            stats[workout_type] = {
                'count': 0,
                'total_duration': 0,
                'total_calories': 0
            }
        stats[workout_type]['count'] += 1
        stats[workout_type]['total_duration'] += duration
        stats[workout_type]['total_calories'] += calories
    
    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for workout_type, data in stats.items():
        count = data['count']
        percentage = (count / all_workouts) * 100
        
        avg_duration = data['total_duration'] / count
        avg_calories = data['total_calories'] / count
        
        print(f"{workout_type}: {count} тренировок ({percentage:.1f}%)")
        print(f"Средняя длительность: {avg_duration:.0f} мин")
        print(f"Средние калории: {avg_calories:.0f} ккал\n")

def find_user_workouts(users, user_name):
    target_user = None
    
    for user in users:
        if user.get('name') == user_name:
            target_user = user
            break

    user_workouts = []
    for workout in workouts:
        if workout.get('user_id') == target_user.get('user_id'):
            user_workouts.append(workout)
            
    return user_workouts

def analyze_user(users, workouts, user_workouts):
    target_user = None 
    
    for user in users:
        if user.get('name') == user_name:
            target_user = user
            user_age = target_user['age']
            user_weight = target_user['weight']
            user_fitness_level = target_user['fitness_level']
    
    all_calories = 0
    all_time = 0
    all_distance = 0
    all_calories = 0
    
    type_counts = Counter(workout['type'] for workout in user_workouts)
    for types in type_counts:
        if type_counts:
            favorite_workout = type_counts.most_common(1)[0][0]
        else:
            favorite_workout = "Нет данных"
    
    for w in user_workouts:
        all_calories += w['calories']
        all_time += w['duration'] / 60
        all_distance += w['distance']
        all_calories += w['calories']
    all_calories = all_calories / 2
    avg_calories = all_calories / len(user_workouts)
            
    text = f'''ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user_name}
{'='*50}
Возраст: {user_age}, Вес: {user_weight}
Уровень: {user_fitness_level}
Сожжено калорий: {all_calories}
Общее время: {all_time:.1f} часов
Пройдено дистанции: {all_distance:.1f} км
Средние калории за тренировку: {avg_calories:.0f}
Любимый тип тренировки: {favorite_workout}
'''
    return text

user_name = "Борис"
user_workouts = find_user_workouts(users, user_name)
print(analyze_user(users, workouts, user_workouts))
