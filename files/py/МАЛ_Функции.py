from pandas import read_csv

def загрузить_данные_aopa():
    """
    Функция обеспечивает загрузку данных из файла aopa-points-export.csv
    в память компьютера. 
    """
    aopa = None
    try:
        aopa = read_csv(
            '../csv/aopa-points-export.csv',
            index_col='Индекс', sep=';')
    except:
        print("[ОШИБКА] Проверить файл ~/csv/aopa-points-export.csv")
    finally:
        return aopa