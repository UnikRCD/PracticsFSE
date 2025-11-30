import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

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
Пройдено дистаеции: {all_distance:.1f} км
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
        

users = load_users_data()
workouts = load_workouts_data()

print(analyze_user_activity(users, workouts))
