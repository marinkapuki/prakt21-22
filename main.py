import task1
import task2
import task3

def main_menu():
    """Главное меню приложения."""
    while True:
        print("\nГлавное меню:")
        print("1) Задание 1")
        print("2) Задание 2")
        print("3) Задание 3")
        print("4) Завершить работу программы")

        choice = input("Выберите опцию: ")

        if choice == '1':
            task1.task1_menu()
        elif choice == '2':
            task2.task2_menu()
        elif choice == '3':
            task3.task3_menu()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main_menu()