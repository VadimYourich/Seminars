
def show_menu():
    print("Команды информационной системы: \n1 - показать всех сотрудников\n"
          "2 - добавить сотрудника\n3 - изменить данные сотрудника\n4 - удалить сотрудника\n"
          "5 - импорт сотрудников из файла\n6 - экспорт выбранных сотрудников в файл\n"
          "7 - показать сотрудников")
    try:
        select = int(input("    Выберите команду: "))
        if not select in [1, 2, 3, 4, 5, 6, 7]:
            raise ValueError
        return select
    except Exception:
        print("\nВведена неверная команда!")
        exit()


def show_employees(spisok):
    print("\nСписок всех сотрудников :")
    for i, sotrudnik in enumerate(spisok):
        if i == 0:
            print(" ", *sotrudnik)
        else:
            print(i, *sotrudnik)


def add_employee():
    print("\nВведите Фамилию, Имя, телефон и должность через пробел: ")
    data = input().split()
    return data


def change_employee():
    change = int(input("\nВыберите номер строки для перезаписи: "))
    string = input("Введите Фамилию, Имя, телефон и должность через пробел: ").split()
    return change, string


def delete_employee():
    number = int(input("\nВведите номер строки для удаления: "))
    return number


def res_import(count):
    print(f"\nИз файла добавлено в базу записей: {count}.")


def export_employees():
    print("\nВведите номера сотрудников для экспорта через пробел: ", end='')
    numbers = [int(n) for n in input().split()]
    return numbers


def res_export(exp, numbers):
    if len(exp) != 0:
        exp = [str(i) for i in exp]
        print(f"Выполнен экспорт сотрудников с номерами записей: {', '.join(exp)}.")
    else:
        print("Не были переданы номера строк, присутствующих в файле.")
    if len(numbers) != 0:
        numbers = [str(i) for i in numbers]
        print(f"Номера: {', '.join(numbers)}, в файле отсутствуют.")


def employee():
    print("\nВведите через пробел номера сотрудников для вывода на экран: ", end='')
    numbers = [int(n) for n in input().split()]
    return numbers


def print_employee(numbers, spisok, read_num):
    if len(read_num) != 0:
        print()
        for i in spisok:
            print(*i, end='\n')
        read_num = [str(i) for i in read_num]
        print(f"\nВыполнен вывод на экран сотрудников с номерами записей: {', '.join(read_num)}.")
    else:
        print("Не были переданы номера строк, присутствующих в файле.")
    if len(numbers) != 0:
        numbers = [str(i) for i in numbers]
        print(f"Номер(а): {', '.join(numbers)}, в файле отсутствуют(ет).")