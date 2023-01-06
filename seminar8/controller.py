import view
import models
import logging

logging.basicConfig (filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG, encoding="UTF-8")


def main():
    select = view.show_menu()
    if select == 1:
        logging.info("\nВыбрана первая команда.")
        sotr = models.get_list()
        view.show_employees(sotr)
        logging.info("Показаны все сотрудники.")
    elif select == 2:
        logging.info("\nВыбрана вторая команда.")
        data = view.add_employee()
        models.add_employee_to_list(data)
        logging.warning("Добавлен новый сотрудник.")
    elif select == 3:
        logging.warning("\nВыбрана третья команда.")
        change, string = view.change_employee()
        print(change, string)
        models.update_employee(change, string)
        logging.warning(f"Данные сотрудника {change} изменены.")
    elif select == 4:
        logging.warning("\nВыбрана четвёртая команда.")
        number = view.delete_employee()
        models.delete_employee(number)
        logging.warning(f"Сотрудник номер {number} удалён.")
    elif select == 5:
        logging.info("\nВыбрана пятая команда.")
        count = models.import_exployees_file()
        logging.warning("Успешный импорт сотрудников из файла.")
        view.res_import(count)
    elif select == 6:
        logging.info("\nВыбрана шестая команда.")
        numbers = view.export_employees()
        exp = models.export_employees_file(numbers)
        logging.warning(f"Выполнен экспорт сотрудников в файл.")
        view.res_export(exp, numbers)
    else:
        print("\nНеверная команда!")
    logging.info("Программа выполнена корректно!")