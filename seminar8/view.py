
def show_menu():
    print("Команды информационной системы: \n1 - показать всех сотрудников\n"
          "2 - добавить сотрудника\n3 - изменить данные сотрудника\n4 - удалить сотрудника\n"
          "5 - импорт сотрудников из файла\n6 - экспорт выбранных сотрудников в файл")
    try:
        select = int(input("    Выберите команду: "))
        if not select in [1, 2, 3, 4, 5, 6]:
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
    print("\nВведите Фамилию Имя Телефон и должность через пробел: ")
    data = input().split()
    return data


def change_employee():
    change = int(input("\nВыберите номер строки для перезаписи: "))
    print("Новая строка - Фамилию Имя Телефон и должность через пробел: ")
    string = input("Введите строку для записи: ").split()
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
    if len(exp) !=0:
        exp = [str(i) for i in exp]
        print(f"Выполнен экспорт сотрудников с номерами записей: {', '.join(exp)}.")
    else:
        print("Не были переданы номера строк присутствующие в базе.")
    if len(numbers) != 0:
        numbers = [str(i) for i in numbers]
        print(f"Такие номера: {', '.join(numbers)} в базе отсутствуют.")


