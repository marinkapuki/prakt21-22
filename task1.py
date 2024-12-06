import random

def input_large_number_array(prompt):
    """Ввод массива чисел вручную."""
    return list(map(int, input(prompt).split()))

def generate_large_number_array(size):
    """Генерация случайного массива чисел."""
    return [random.randint(0, 9) for _ in range(size)]

def sum_arrays(array1, array2):
    """Суммирует два массива."""
    max_length = max(len(array1), len(array2))
    array1 = array1 + [0] * (max_length - len(array1))
    array2 = array2 + [0] * (max_length - len(array2))
    return [a + b for a, b in zip(array1, array2)]

def subtract_arrays(array1, array2):
    """Вычитает второй массив из первого."""
    max_length = max(len(array1), len(array2))
    array1 = array1 + [0] * (max_length - len(array1))
    array2 = array2 + [0] * (max_length - len(array2))
    return [a - b for a, b in zip(array1, array2)]

def task1_operations(array1, array2, operation):
    """Выполняет операцию сложения или вычитания массивов."""
    if operation == '+':
        result = sum_arrays(array1, array2)
        print(f"Результат суммы: {result}")
    elif operation == '-':
        result = subtract_arrays(array1, array2)
        print(f"Результат разности: {result}")

def task1_menu():
    """Меню первого задания."""
    while True:
        print("\nЗадание 1: Сумма и разность массивов")
        print("1) Ввод массивов вручную")
        print("2) Генерация случайных массивов")
        print("3) Выполнить операцию")
        print("4) Вернуться в главное меню")

        choice = input("Выберите опцию: ")

        if choice == '1':
            array1 = input_large_number_array("Введите первый массив чисел: ")
            array2 = input_large_number_array("Введите второй массив чисел: ")
            operation = input("Введите операцию (+ или -): ")
            from threading import Thread
            operation_thread = Thread(target=task1_operations, args=(array1, array2, operation))
            operation_thread.start()
            operation_thread.join()

        elif choice == '2':
            size = int(input("Введите размер массивов: "))
            array1 = generate_large_number_array(size)
            array2 = generate_large_number_array(size)
            print(f"Сгенерированный первый массив: {array1}")
            print(f"Сгенерированный второй массив: {array2}")
            operation = input("Введите операцию (+ или -): ")
            from threading import Thread
            operation_thread = Thread(target=task1_operations, args=(array1, array2, operation))
            operation_thread.start()
            operation_thread.join()

        elif choice == '3':
            print("Сначала необходимо ввести или сгенерировать массивы.")
        
        elif choice == '4':
            break
        
        else:
            print("Неверный выбор.")