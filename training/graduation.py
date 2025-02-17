import math

order_belt = {'White': 0, 'Blue': 1, 'Purple': 2, 'Brown': 3, 'Black': 4 }

def calculate_lessons_to_upgrade(n):
    d = 1.47
    k = 30 / math.log(d)

    lessons = k * math.log(n + d)
    
    return round(lessons)
