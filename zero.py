# баг - это ошибка
# дебаг - позволяет найти ошибку, пошагово

#def duggy_functijn(x, y):
    #return x / y

#duggy_functijn(10, 2)

import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s", # формат сообщения
    filename = 'main2.log', # Указываем имя файла. Если не указать имя файла  - данные будут поступать на консоль
    filemode='w', # режим открытия файла
    encoding='UTF-8' # какая кодировка
)

def muit_str(s: str, num: int) -> str:
    try:
        if type(num) is int:
             logging.info("Тип данных верный")
             return s * num
        
        elif num.isdigit():
            logging.warning("Тип данных неверный, но строка состоит из чисел")
            return s * int(num)
    except AttributeError as e:
        logging.error(f"Тип данных неверный {e}")


muit_str("Hello", "2")
muit_str("Hello", 2)
muit_str("Hello", [])


    