import math
from threading import Thread

def calculate_distance(p1, p2):
    """Вычисляет расстояние между двумя точками."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_distances(points1, points2):
    """Вычисляет расстояния между двумя массивами точек."""
    return (calculate_distance(p1, p2) for p1, p2 in zip(points1, points2))

def filter_distances(distances, threshold):
    """Фильтрует расстояния по заданному порогу."""
    return list(filter(lambda d: d > threshold, distances))

def task3_operations(points1, points2, threshold):
    """Выполняет вычисление и фильтрацию расстояний."""
    distances_gen = calculate_distances(points1, points2)
    filtered_distances = filter_distances(distances_gen, threshold)
    
    print(f"Расстояния между точками: {list(distances_gen)}")  # Преобразуем генератор в список для отображения
    print(f"Расстояния больше порога {threshold}: {filtered_distances}")

def parse_points(input_string):
    """Парсит строку ввода в список кортежей точек."""
    return list(map(lambda point: tuple(map(int, point.split(','))), input_string.split()))

def task3_menu():
    """Меню третьего задания."""
    while True:
        points_input_1 = input("Введите точки первого массива (x,y) через пробел: ")
        points_input_2 = input("Введите точки второго массива (x,y) через пробел: ")
        
        try:
            points1 = parse_points(points_input_1)
            points2 = parse_points(points_input_2)
        except ValueError:
            print("Ошибка ввода. Убедитесь, что точки введены в формате 'x,y'.")
            continue
        
        threshold = float(input("Введите порог расстояния: "))
        
        # Создание потока для выполнения операции
        operations_thread = Thread(target=task3_operations, args=(points1, points2, threshold))
        operations_thread.start()
        operations_thread.join()

        if input("Хотите продолжить? (y/n): ") != 'y':
            break