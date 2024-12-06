from functools import lru_cache

@lru_cache(maxsize=None)
def count_subarrays_with_sum(array_tuple, target_sum):
    """Подсчитывает количество подмассивов с заданной суммой."""
    count = 0
    n = len(array_tuple)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += array_tuple[j]
            if current_sum == target_sum:
                count += 1
                
    return count

def task2_operations(array, target_sum):
    """Выполняет подсчет подмассивов с заданной суммой."""
    result = count_subarrays_with_sum(tuple(array), target_sum)
    print(f"Количество подмассивов с суммой {target_sum}: {result}")

def task2_menu():
    """Меню второго задания."""
    while True:
        array_input = input("Введите массив чисел через пробел: ")
        
        try:
            # Преобразование ввода в список целых чисел
            array = list(map(int, array_input.split()))
        except ValueError:
            print("Ошибка ввода. Убедитесь, что введены только числа.")
            continue
            
        target_sum = int(input("Введите целевую сумму: "))
        
        # Создание потока для выполнения операции
        from threading import Thread
        operations_thread = Thread(target=task2_operations, args=(array, target_sum))
        operations_thread.start()
        operations_thread.join()

        if input("Хотите продолжить? (y/n): ") != 'y':
            break