import view
import model
import logging

logging.basicConfig(filename='log.txt',
filemode='a',
format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
datefmt='%H:%M:%S',
level=logging.INFO, encoding='utf-8')

def main_function():
    try:
        select = view.greeting()
        if select == 1:
            logging.info('Выбран режим калькулятор')
            primer = view.get_math_example()
            result = model.calc(primer)
            view.view_result(result)
            logging.info(f"Получен результат '{result}'")
        elif select == 2:
            logging.info('Выбран режим конвертер')
            massa = view.get_massa()
            logging.info(f"Введено значение '{massa}'")
            value = model.converter(massa)
            view.view_result(value)
    except Exception as err:
        logging.warning(f'Введено некорректное значение "{err}"')


