from pandas import read_csv
# "id","region","municipality","settlement","type","population","children",
# "latitude_dms","longitude_dms","latitude_dd","longitude_dd","oktmo","dadata","rosstat"
def Агломерация(широта = 53, долгота = 87, радиус = 100):
    агломерация = 0
    try:
        df = read_csv('../csv/data.csv', index_col="id")
    except:
        print("[ОШИБКА] Проверить файл data.csv")
    finally:
        ...
    
    return агломерация



if __name__ == "__main__":
    широта = 50
    долгота = 80
    радиус = 50

    print(Агломерация())
    print(Агломерация(широта, долгота, радиус))