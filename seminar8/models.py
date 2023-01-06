import csv


def get_list():
    with open('file.csv', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        return list(reader)


def add_employee_to_list(employee):
    with open('file.csv', 'a', encoding="utf-8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(employee)


def update_employee(number, string):
    try:
        with open('file.csv', 'r', encoding="utf-8", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader)
            data[number] = string
        with open('file.csv', 'w', encoding="utf-8", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        print("Вы вышли за границы списка.")
        exit()
    except Exception:
        print("Выявлены другие ошибки!")
        exit()


def delete_employee(number):
    try:
        with open('file.csv', 'r', encoding="utf-8", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader)
            del data[number]
        with open('file.csv', 'w', encoding="utf-8", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        print("Вы вышли за границы списка.")
        exit()
    except Exception:
        print("Выявлены другие ошибки!")
        exit()


def import_exployees_file():
    with open('import.csv', 'r', encoding="utf-8", newline='') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=';')
        data1 = list(reader1)
        data1.pop(0)
        count = 0
    with open('file.csv', 'r', encoding="utf-8", newline='') as csvfile:
        reader2 = csv.reader(csvfile, delimiter=';')
        data2 = list(reader2)
    with open('file.csv', 'a', encoding="utf-8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for s in data1:
            if s not in data2:
                writer.writerow(s)
                count += 1
    return str(count)


def export_employees_file(numbers):
    exp = []
    ex = []
    with open('file.csv', 'r', encoding="utf-8", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        for i, sotrudnik in enumerate(data):
            if i in numbers:
                exp.append(sotrudnik)
                ex.append(i)
                numbers.remove(i)
    with open('export.csv', 'w', encoding="utf-8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(["Имя", "Фамилия", "Телефон", "Должность"])
        for i in exp:
            writer.writerow(i)
    return ex


def read_employee(numbers):
    spisok = []
    read_num = []
    with open('file.csv', 'r', encoding="utf-8", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        for i, sotrudnik in enumerate(data):
            if i in numbers:
                spisok.append(sotrudnik)
                read_num.append(i)
                numbers.remove(i)
    return numbers, spisok, read_num

