import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding="utf-8")


def main_function():
    select = view.choosing_an_action()
    if select == 1:
        logging.info('Выбрано чтение файла')
        format = view.format_selection()
        if format == 1:
            logging.info('Выбран формат .txt')
            data = model.reading_txt_file()
            print('Файл содержит следующие данные:\n')
            view.print_data(data)
            logging.info('Чтение выполнено!')
        if format == 2:
            logging.info('Выбран формат .csv')
            data = model.reading_csv_file()
            print('Файл содержит следующие данные:\n')
            view.print_data(data)
            logging.info('Чтение выполнено!')
    elif select == 2:
        logging.info('Выбрана запись файла')
        format = view.format_selection()
        if format == 1:
            logging.info('Выбран формат .txt')
            data = model.reading_txt_file()
            model.record_txt(data)
            logging.info('Запись выполнена!')
        if format == 2:
            logging.info('Выбран формат .csv')
            data = model.reading_csv_file()
            model.record_csv(data)
            logging.info('Запись выполнена!')