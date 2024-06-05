import streamlit as st
from geopy.distance import geodesic
from pandas import read_csv, DataFrame
from классы import *
from перечни import *

черта = lambda x: ' | ' + x if x else ''

# Возвращает геодезическое расстояние между двумя аэродромами
def Дистанция(вылет = 'UNWW', прилёт = 'UNNT'):
    """Функция возвращает геодезическое расстояние между КТА в км.
    Входные данные:
        - вылет (код ИКАО аэродрома вылета);
        - прилёт (код ИКАО аэродрома прибытия)."""
    В = КТА(вылет)
    П = КТА(прилёт)
    return int(geodesic(
        (В.широта, В.долгота),
        (П.широта, П.долгота)).km)

# Возвращает геодезическое расстояние между КТА и парой значений (широта и долгота)
def Расстояние(аэродром = 'UNWW', широта=55, долгота=87):
    """Функция возвращает геодезическое расстояние между КТА
    и географической координатой, заданной десятичными значениями
    широты и долоты в километрах."""
    а = КТА(аэродром)
    return int(geodesic(
        (а.широта, а.долгота),
        (широта, долгота)).km)

# Возвращает широту, долготу и превышения контрольной точи аэродрома
def КТА(аэродром="UNWW"):
    """Функция возвращает именованный кортеж, который содержит
    десятичные значения северной широты, восточной долготы
    и превышения КТА над уровнем Балтийского моря в метрах."""
    возврат = None
    d = None
    try:
        d = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
        возврат = К(
            d.loc[аэродром]['Широта КТА'],
            d.loc[аэродром]['Долгота КТА'],
            d.loc[аэродром]['Превышение'])
    except:
        print('[ОШИБКА] Проверить файл aopa-points-export.csv')
    finally:
        del d
        return возврат

# def Расчёт_агломерации(аэродром='UNWW', радиус=100):
#     возврат = None
#     d = read_csv('../csv/data.csv')
#     a = []
#     return возврат

# Возвращает агломерацию населения в районе аэропорта
def Агломерация(аэродром = 'UNWW', радиус = 100):   
    """Функция возвращает агломерацию населения в районе КТА
    с указанным радиусом окружности, в границах которой учитываются
    населённые пункты, жители которых суммируются в результат."""
    возврат = None
    a = None
    if радиус == 100:
        a = read_csv('../csv/Агломерация.csv', index_col='ICAO')
        возврат = a.loc[аэродром]['Агломерация']
    else:
        d = read_csv('../csv/data.csv', index_col='id')
        кта = КТА(аэродром=аэродром)
        ШВ = кта.широта + 1
        ШН = кта.широта - 1
        ДЗ = кта.долгота - 1
        ДВ = кта.долгота + 1

    del a
    return возврат

# Возвращает коэффициент авиационной подвижности для аэропорта
def АПН(аэродром = 'UNWW', КУА=2.5, КАН=4.2):
    """
    Функция возвращает коэффициент авиационной подвижности
    для определённого вида аэропорта:
        - для узлового аэропорта коэффициент по умолчанию равен 2.5;
        - для аэропорта назначения коэффициент по умолчанию равен 4.2.
    """
    возврат = None
    s = None
    s = read_csv('../csv/Сводка.csv', index_col='ICAO')
    if s.loc[аэродром]['Вид'] == "УА": возврат = КУА
    elif s.loc[аэродром]['Вид'] == "АН": возврат = КАН
    else:
        ...
    del s
    return возврат

# Возвращает название города в районе аэропорта или None
def Город(аэродром='UNWW'):
    """Функция возвращает название города в района аэродрома
    для укзанного кода ИКАО аэродрома"""
    возврат = ''
    try:
        a = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
        возврат = a.loc[аэродром]['Город']
        if isinstance(возврат, float): возврат = ''
        else: ...
        del a
    except: print('[ОШИБКА] Проверить файл aopa-points-export.csv')
    finally: ...
    return возврат

# Возвращает название аэропорта или None
def Название(аэродром='UNWW'):
    """Функция возвращает название аэродрома для указанного кода ИКАО"""
    возврат = ''
    try:
        a = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
        возврат = a.loc[аэродром]['Название']
        del a
    except:
        print('[ОШИБКА] Проверить файл aopa-points-export.csv')
    finally:
        ...
    return возврат    

# Возвращает код ИАТА аэропорта или None
def IATA(аэродром='UNWW'):
    """Функция возвращает код ИАТА для указанного кода ИКАО аэродрома
    или пустое значение, если код ИАТА для данного аэродрома не найден."""
    возврат = ''
    try:
        d = read_csv('../csv/IATA.csv', index_col='icao')
        возврат = d.loc[аэродром]['iata']
    except:
        print('[ОШИБКА] Проверить файл IATA.csv')
    finally:
        del d
        return возврат

# Возвращает полное наименование аэропорта
# def Наименование(аэродром='UNWW'):
#     """Функция возвращает составное наименование аэропорта.
#     В состав наименования входят:
#         - код ИКАО аэродрома;
#         - код ИАТА аэропорта (если найден);
#         - название города в районе аэродрома (если найден);
#         - название аэропорта (если имеется)."""
#     возврат = ''
#     возврат = аэродром + черта(IATA(аэродром)) + черта(Город(аэродром)) + черта(Название(аэродром))
#     return возврат

def Наименование(аэродром='UNWW'):
    """Функция возвращает составное наименование аэропорта.
    В состав наименования входят:
        - код ИКАО аэродрома;
        - код ИАТА аэропорта (если найден);
        - название города в районе аэродрома (если найден);
        - название аэропорта (если имеется)."""
    d = read_csv('../csv/Имена.csv', index_col='ICAO')
    возврат = d.loc[аэродром]['Имя']
    del d
    return возврат


# Возвращает перечень наименований аэропортов МАЛ
def Перечень_МАЛ():
    """Функция возвращает DataFrame таблицы Сводка.csv"""
    возврат = []
    d = read_csv('../csv/Сводка.csv', index_col='ICAO')
    for _ in d.index: возврат.append(Наименование(_))
    del d
    return возврат

# Возвращает перечень наименований аэропортов ЮВК
def Перечень_ЮВК():
    возврат = []
    d = read_csv('../csv/Сводка.csv', index_col='ICAO')
    for _ in d[d.ВК == 1].index:
        возврат.append(Наименование(_))
    del d
    return возврат

# Возвращает перечень наименований аэропортов СВК
def Перечень_СВК():
    возврат = []
    d = read_csv('../csv/Сводка.csv', index_col='ICAO')
    for _ in d[d.ВК == 2].index:
        возврат.append(Наименование(_))
    del d
    return возврат

# Возвращает перечень наименований аэропортов ЦВК
def Перечень_ЦВК():
    возврат = []
    d = read_csv('../csv/Сводка.csv', index_col='ICAO')
    for _ in d[d.ВК == 3].index:
        возврат.append(Наименование(_))
    del d
    return возврат

# Возвращает перечень наименований узловых аэропортов
def Перечень_УА():
    возврат = []
    d = read_csv('../csv/Сводка.csv', index_col='ICAO')
    for _ in d[d.Вид == "УА"].index:
        возврат.append(Наименование(_))
    del d
    return возврат

# Возвращает перечень наименований аэропортов назначения
def Перечень_АН():
    возврат = []
    d = read_csv('../csv/Сводка.csv', index_col='ICAO')
    for _ in d[d.Вид == "АН"].index:
        возврат.append(Наименование(_))
    del d
    return возврат

# Определяет, является ли аэропорт УА (True или False)
def УА(аэродром="UNWW", перечень=перечень_УА):
    возврат = False
    for _ in перечень:
        if аэродром == _[:4]: возврат = True
    return возврат

# Определяет, является ли аэропорт АН (True или False)
def АН(аэродром="UNWW", перечень=перечень_АН):
    возврат = False
    for _ in перечень:
        if аэродром == _[:4]: возврат = True
    return возврат

# Выгрузка таблицы городов в CSV
def Перечень_городов_в_csv(аэродром='UNWW', df=DataFrame(), радиус=100):
    путь = '../csv/Города/' + аэродром + '_' + str(радиус) +'_перечень_городов.csv'
    df.to_csv(путь,index=False)
    return None

# Выгрузка таблицы аэродромов в CSV
def Перечень_аэродромов_в_csv(аэродром='UNWW', df=DataFrame(), радиус=1000):
    путь = '../csv/Аэродромы/' + аэродром + '_' + str(радиус) +'_перечень_аэродромов.csv'
    df.to_csv(путь,index=False)
    return None

# Формирует таблицу городов в районе аэродрома по указанному радиусу
@st.cache_data
def Перечень_городов(аэродром='UNWW', радиус=100):
    возврат = []
    дистанция = 0
    кта = КТА(аэродром)
    ШС = кта.широта + 1
    ШЮ = кта.широта - 1
    ДЗ = кта.долгота - 1
    ДВ = кта.долгота + 1
    d = read_csv('../csv/data.csv', index_col='id')
    набор = d[(d.latitude_dd < ШС) & (d.latitude_dd > ШЮ) & (d.longitude_dd > ДЗ) & (d.longitude_dd < ДВ)]
    for _ in набор.index:
        дистанция = Расстояние(аэродром, набор.loc[_]['latitude_dd'], набор.loc[_]['longitude_dd'])
        if дистанция <= радиус:
            запись = {
                "регион": набор.loc[_]['region'],
                "район": набор.loc[_]['municipality'],
                "город": набор.loc[_]['settlement'],
                "тип": набор.loc[_]['type'],
                "население": int(набор.loc[_]['population']),
                "широта": набор.loc[_]['latitude_dd'],
                "долгота": набор.loc[_]['longitude_dd'],
                "расстояние": дистанция 
            }
            возврат.append(запись)
    return DataFrame(возврат)

# Таблица аэродромов в зоне доступности указанного аэродрома
@st.cache_data
def Перечень_аэродромов(аэродром='UNWW', радиус=1000):
    """Функция возвращает DataFrame записей, которые содержат основные
    сведения по аэродромам, расположенным в районе зоны ответствености
    аэродрома, принимаемого входным значением.
    
    Входные данные:
        - код ИКАО (лат.) основного аэродрома;
        - радиус зоны ответственности в километрах.
        
    Выходные данные;
        - DataFrame определённых записей."""
    возврат = []
    дистанция = 0
    кта = КТА(аэродром)
    ШС = кта.широта + (радиус/10)
    ШЮ = кта.широта - (радиус/10)
    ДЗ = кта.долгота - (радиус/10)
    ДВ = кта.долгота + (радиус/10)
    d = read_csv('../csv/aopa-points-export.csv',sep=';', index_col='Индекс')
    s = read_csv('../csv/Сводка.csv', index_col='ICAO')
    # набор = d[(d['Широта КТА'] < ШС) & (d['Широта КТА'] > ШЮ) & (d['Долгота КТА'] > ДЗ) & (d['Долгота КТА'] < ДВ)]
    for _ in перечень_МАЛ:
        дистанция = Расстояние(аэродром, d.loc[_[:4]]['Широта КТА'], d.loc[_[:4]]['Долгота КТА'])
        if дистанция <= радиус:
            запись = {
                "ICAO": _[:4],
                "Широта": d.loc[_[:4]]['Широта КТА'],
                "Долгота": d.loc[_[:4]]['Долгота КТА'],
                "Превышение": d.loc[_[:4]]['Превышение'],
                "Расстояние": дистанция,
                "Коридор": s.loc[_[:4]]['ВК'],
                "Вид": s.loc[_[:4]]['Вид'],
                "Кандидат": s.loc[_[:4]]['Кандидат'],
                "Пассажиропоток": s.loc[_[:4]]['Пассажиропоток'],
                "Грузопоток": s.loc[_[:4]]['Груз, тонн'],
                "Почта": s.loc[_[:4]]['Почта, тонн'],
                "Керосин": s.loc[_[:4]]['Цена ТС-1, руб'],
                "Категория": s.loc[_[:4]]['Категория']
            }
            возврат.append(запись)
    del d
    return DataFrame(возврат)

# Средняя стоимость ТС-1 через стоимость ТС-1 в UNNT
def Керосин_сегодня(аэропорт='UNWW', UNNT=100680, коэффициент=1.08):
    """Функция возвращает среднюю расчётную стоимость ТС-1 на сегодня.
    Стоимость расчитывается как цена ТС-1 в аэропорте Толмачёво в крыло,
    умноженная на средний статистический коэффициент стоимости ТС-1
    в Толмачёво по годам к средней стоимости ТС-1 по России.
    Входная цента в рублях за тонну ТС-1."""
    # возврат = int(round(UNNT*коэффициент, 0))
    try:
        d = read_csv('../csv/КТ.csv', index_col='ICAO')
        коэффициент = d.loc[аэропорт]['КТ']
        del d
    except: ...
    finally: возврат = int(round(UNNT/коэффициент, 0))
    return возврат

# Таблица населённых пунктов в районе аэропорта
@st.cache_data
def Города_аэродромов(радиус=100):
    """Функция формирует csv-файлы в каталоге ../csv/Города/
    в которые входят списки близлежащих населённых пунктов
    с координатами, жителями и расстоянием от КТА"""
    for _ in перечень_МАЛ:
        df = Перечень_городов(аэродром=_[:4], радиус=радиус)
        Перечень_городов_в_csv(аэродром=_[:4], df=df, радиус=радиус)
    return None

# Категория аэропорта (1, 2, 3 или 0)
def Категория(аэродром='UNWW'):
    """Функцция возвращает значение категории аэропорта в терминологии
    проекта МАЛ:
        - 1 (аэропорт может принимать все расчётные типы ВС);
        - 2 (аэропорт не может принимать Ил-114-300);
        - 3 (аэропорт может принимать только ЛМС-901);
        - 0 (аэропорт не может принимать расчётные типы ВС проекта МАЛ)"""
    s = None
    категория = 0
    try:
        s = read_csv('../csv/Сводка.csv', index_col='ICAO')
        категория = s.loc[аэродром]['Категория']
    except:
        print("[ОШИБКА] Проверить файл Сводка.csv")
    finally:
        del s
        return категория

# Вид аэропорта (УА или АН)
def Вид(аэродром='UNWW'):
    """Функция возвращает вид ажропорта: АН или УА"""
    s = None
    вид = 0
    try:
        s = read_csv('../csv/Сводка.csv', index_col='ICAO')
        вид = s.loc[аэродром]['Вид']
    except:
        print("[ОШИБКА] Проверить файл Сводка.csv")
    finally:
        del s
        return вид

# Фактический пассажиропоток аэропорта
def ФПП(аэродром='UNWW'):
    """Функция возвращает фактический пассажиропоток, пасс"""
    s = None
    пассажиропоток = 0
    try:
        s = read_csv('../csv/Сводка.csv', index_col='ICAO')
        пассажиропоток = s.loc[аэродром]['Пассажиропоток']
    except:
        print("[ОШИБКА] Проверить файл Сводка.csv")
    finally:
        del s
        return пассажиропоток

# Расчётный годовой пассажиропоток аэропорта
def РПП(аэродром='UNWW'):
    """Функция возвращает расчётный годовой пассажиропоток, пасс"""
    s = None
    пассажиропоток = 0
    try:
        s = read_csv('../csv/Агломерация.csv', index_col='ICAO')
        пассажиропоток = s.loc[аэродром]['Агломерация'] * АПН(аэродром)
    except:
        print("[ОШИБКА] Проверить файл Сводка.csv")
    finally:
        del s
        return int(пассажиропоток)

# Определяет тип ВС по категории аэродрома и суточному пассажиропотоку
def Расчётный_тип_ВС(рпп=120, категория=1):
    """Функция возвращает расчётный тип воздушного судна
    в зависимости от среднесуточного пассажиропотока и категории аэропорта"""
    возврат = ""
    if (рпп > 130) and (категория == 1): возврат = "Ил-114-300"
    elif (рпп > 130) and (категория == 2): возврат = "ТВРС-44"
    elif (рпп < 130): возврат = "ЛМС-901"
    else: ...
    return возврат

# Крейскрская скорость ВС в км/ч
def Vкр(тип="Ил-114-300"):
    """Функция возвращает крейсерскую скорость указанного типа ВС в км/ч"""
    df = DataFrame(перечень_самолёты, columns=["тип", "Крейсерская скорость, км/ч"])
    df.set_index("тип", inplace=True)
    возврат = int(df.loc[тип]["Крейсерская скорость, км/ч"])
    del df
    return возврат

# Количество кресел пассажирского салона
def Количество_кресел(тип="Ил-114-300"):
    """Функция возвращает количество кресел пассажирского салона указанного типа ВС"""
    df = DataFrame(перечень_самолёты, columns=["тип", "Пассажиров, чел"])
    df.set_index("тип", inplace=True)
    возврат = int(df.loc[тип]["Пассажиров, чел"])
    del df
    return возврат

# Минимальное количество ежедневных парных рейсов
def Парных(суточный_пассажиропоток=139, пассажиров_на_рейсе=31):
    возврат=1
    if суточный_пассажиропоток/пассажиров_на_рейсе > 2:
        возврат = 2
    else: ...
    return возврат

# Количество пассажирских кресел в салоне указанного типа ВС
def Пвс(тип="Ил-114-300"):
    """Функция возвращает количество кресел пассажирского салона"""
    df = DataFrame(перечень_самолёты, columns=["тип", "Пассажиров, чел"])
    df.set_index("тип", inplace=True)
    возврат = int(df.loc[тип]["Пассажиров, чел"])
    del df
    return возврат

# Часовой расход ТС-1 для выбранного типа ВС в кг/лч
def Рлч(тип="Ил-114-300"):
    """Функция возвращает часовой расход ТС-1 для указанного типа ВС в кг/лч"""
    df = DataFrame(перечень_самолёты, columns=["тип", "Расход ТС-1, кг/лётный час"])
    df.set_index("тип", inplace=True)
    возврат = int(df.loc[тип]["Расход ТС-1, кг/лётный час"])
    del df
    return возврат

# Техническая скорость по маршруту
def Vт(тип="Ил-114-300", расстояние=300):
    """Функция возвращает техническую скорость указанного типа ВС в км/ч
    для указанного расстояния для беспосадочного маршрута."""
    возврат = None
    крейсерская_скорость = Vкр(тип=тип)
    if (тип == "Ил-114-300") or (тип == "ТВРС-44"): дельта_t = 0.22
    elif тип == "ЛМС-901": дельта_t = 0.165
    else: дельта_t = 1.65
    возврат = int((расстояние*крейсерская_скорость)/(расстояние + крейсерская_скорость*дельта_t))
    return возврат

# Определяет расчётное время полёта самолёта на указанное расстояние
def tр(тип="Ил-114-300", расстояние=100):
    """Функция возвращает десятичное значение времени полёта"""
    возврат = None
    возврат = расстояние/Vт(тип=тип, расстояние=расстояние)
    return возврат

# Переводит десятичное значение времени полёта в текстовое в формате Ч:ММ
def ЧММ(время=1.97):
    """Функция возвращает текстовое представление времени в формате Ч:ММ"""
    часы = int(время)
    минуты = (время*60)%60
    return "%d:%02d"%(часы, минуты)

# По текстовому значению расчётного времени полёта определяет время полёта по расписанию 
def tрасп(время="0:21"):
    """Функция возвращает расчётное время в регулярном расписании.
    Алгоритм расчёта к значению от 0 до 9 добавляет от 20 до 11 единиц.
    В случе, если значение превышает 60, тогда к часу добавляется 1,
    минуты начинаются с остатка значения."""
    возврат = ""
    час = int(время[0])
    дес = int(время[2])*10
    мин = int(время[3])
    дельта = 20 - мин
    минуты = дес+мин+дельта
    if минуты > 60:
        час += 1
        мин = минуты - 60
    else:
        мин = минуты
    if мин < 10:
         мин = "0" + str(мин)
    else:
        мин = str(мин)
    возврат = str(час) + ":" + str(мин)
    return возврат

# Расход ТС-1 для указанного типа ВС в килограммах на лётный час
def Рлч(тип="Ил-114-300"):
    """Функция возвращает расход ТС-1 на лётный час в килограммах
    на час полёта, кг/л.час"""
    df = DataFrame(перечень_самолёты, columns=["тип", "Расход ТС-1, кг/лётный час"])
    df.set_index("тип", inplace=True)
    возврат = int(df.loc[тип]["Расход ТС-1, кг/лётный час"])
    del df
    return возврат

# Стоимость ТС-1 в аэропорте или средняя стоимость по России
def Заправка(аэродром='UNWW'):
    """Функция возвращает цену ТС-1 в тыс. руб/тн"""
    s = None
    цена = 0
    try:
        s = read_csv('../csv/Сводка.csv', index_col='ICAO')
        цена = s.loc[аэродром]["Цена ТС-1, руб"]
    except:
        цена = Керосин_сегодня()
        print("[ОШИБКА] Проверить файл Сводка.csv")
    finally:
        del s
        return цена

# Таблица аэропортов в зоне доступности аэропорта
def Таблица_аэродромов(аэродром="UNWW", радиус=1000):
    имя_файла = '../csv/Аэродромы/' +аэродром + '_' + str(радиус) + '_перечень_аэродромов.csv'
    df = read_csv(имя_файла, index_col='ICAO')
    df = df[df.Расстояние > 0]
    return df

# Базовый узловой аэропорт для аэропорта назначения
def Базовый_УА(аэродром="UERA"):
    """Функция возврашает наименование базового узлового аэропорта
    для входящего значения кода ИКАО аэропорта назначения"""
    возврат = ""
    try:
        d = read_csv('../csv/АНУА.csv', index_col='АН')
        возврат = Наименование(d.loc[аэродром]['УА'])
    except:
        print('[ОШИБКА] Возможно не является аэропортом назначения')
    finally:
        del d
        return возврат

# Расстояние до ближайшего узлового аэропорта
def Базовый_УА_км(аэродром="UERA"):
    """Функция возврашает расстояние до базового узлового аэропорта
    для входящего значения кода ИКАО аэропорта назначения в километрах"""
    возврат = ""
    try:
        d = read_csv('../csv/АНУА.csv', index_col='АН')
        возврат = d.loc[аэродром]['дистанция']
    except:
        print('[ОШИБКА] Возможно не является аэропортом назначения')
    finally:
        del d
        return возврат

# @st.cache_data # Функция рабочая. Используется разово
# def Аэродромы_аэродромов(радиус=1000):
#     """Функция формирует csv-файлы в каталоге ../csv/Аэродромы
#     в которые входят списки близлежащих аэропортов в зоне ответственности
#     аэродрома с координатами и расстоянием от КТА"""
#     for _ in перечень_МАЛ:
#         df = Перечень_аэродромов(аэродром=_[:4], радиус=радиус)
#         Перечень_аэродромов_в_csv(аэродром=_[:4], df=df, радиус=радиус)
#     return None

# def Сводка_АНУА(АН="UERA", УА="UEEE"): # Функция требует доработки!
#     """Функция возвращает набор данных в виде словаря:
#         - АН (код ИКАО аэропорта назначения);
#         - УА (код ИКАО узлового аэропорта);
#         - расстояние (код ИКАО аэропорта назначения);"""
#     расстояние = Дистанция(АН, УА)
#     рпп = РПП(АН)
#     Vт = None
#     tп = None
#     tр = None
#     if (Категория(АН) == 1) and (пассажиропоток/365 > 130):
#         тип = "Ил-114-300"
#     elif (Категория(АН) == 2) and (пассажиропоток/365 > 130):
#         тип = "ТВРС-44"
#     else:
#         тип = "ЛМС-901"
#     return {
#         "АН": АН,
#         "УА": УА,
#         "расстояние": расстояние,
#         "тип": тип,
#         "Vт": Vт,
#         "tп": tп,
#         "tр": tр
#     }

def Расчёт_себестоимости_рейса(вылет='UNWW', прилёт='UNNT'):
    """Функция возвращает набор показателей регулярного рейса для
    использования при подготовке расписания полётов."""
    возврат=None
    категория_маршрута = Категория_маршрута(вылет=вылет, прилёт=прилёт)
    расстояние = Дистанция(вылет=вылет, прилёт=прилёт)
    среднесуточный_пассажиропоток = int(round(РПП(аэродром=вылет)/365, 0))
    тип_самолёта = Расчётный_тип_ВС(рпп=среднесуточный_пассажиропоток, категория=категория_маршрута)
    # крейсерская_скорость = Vкр(тип=тип_самолёта)
    # техническая_скорость = Vт(тип=тип_самолёта)
    продолжительность_рейса = tр(тип=тип_самолёта, расстояние=расстояние)
    продолжительность_рейса_чмм = ЧММ(время=продолжительность_рейса)
    # продолжительность_рейса_расписание = tрасп(время=продолжительность_рейса_чмм)
    расход_на_лётный_час = Рлч(тип=тип_самолёта)
    топливо_на_полёт = расход_на_лётный_час*продолжительность_рейса
    стоимость_топлива = Керосин_сегодня()
    # пассажирских_кресел = Пвс(тип=тип_самолёта)
    себестоимость_рейса = int(round(топливо_на_полёт*стоимость_топлива*4, 0))
    возврат = себестоимость_рейса
    return возврат

def Категория_маршрута(вылет='UNWW', прилёт='UNNT'):
    """Функция определяет категорию маршрута в зависимости от категории
    аэропортов вылета и прибытия:
        - 1 (возможна эксплуатация всех типов воздушных судов);
        - 2 (возможна эксплуатация только ТВРС-44 и ЛМС-901);
        - 3 (возможна эксплуатация только ЛМС-901);
        - 0 (нет возможности эксплуатации самолётов проекта МАЛ)."""
    возврат = 0
    if (Категория(вылет) == 1) and (Категория(прилёт) == 1):
        возврат = 1
    elif (0 < Категория(вылет) <= 2) and (Категория(прилёт) == 2):
        возврат = 2
    elif (Категория(вылет) == 2) and (0 < Категория(прилёт) <= 2):
        возврат = 2
    elif (0 < Категория(вылет) <= 3) and (Категория(прилёт) == 3):
        возврат = 3
    elif (Категория(вылет) == 3) and (0 < Категория(прилёт) <= 3):
        возврат = 3
    else: ...
    return возврат

def Расчётный_суточный_пассажиропоток(вылет='UNWW', прилёт='UNNT', магистральные_пассажиропотоки=200):
    """Функиця возвращает расчётне значение пассажиропотока из аэропорта
    вылета в аэропорт прибытия. Значение определяется:
        - для аэропортов назначения умножением количества жителей
          в районе аэропорта вылета на коэффициент авиационной
          подвижности населения и делением полученного значения на 365;
        - для узловых аэропортов: умножением количества жителей
          в районе аэропорта вылета на коэффициент авиационной
          подвижности населения, делением на 365, делением
          на количество УА"""
    расчётный_пассажиропоток = РПП(аэродром=вылет)
    if АН(аэродром=вылет):
        расчётный_пассажиропоток_суточный = int(round(расчётный_пассажиропоток/365,0))
    elif УА(аэродром=вылет):
        расчётный_пассажиропоток_суточный = int(round(расчётный_пассажиропоток/365,0))
    return расчётный_пассажиропоток_суточный

def Количество_УА(аэродром='UNWW', радиус=1000):
    """Функция определяет количество узловых аэропортов в зоне
    доступности аэродрома"""
    df = Таблица_аэродромов(аэродром=аэродром, радиус=радиус)
    количество_УА = len(df[df.Вид == "УА"])
    return количество_УА

def Коды_УА_зоны(аэродром='UNWW', радиус=1000):
    """Функция возвращает перечень кодов узловых аэропортов в зоне
    доступности аэродрома"""
    df = Таблица_аэродромов(аэродром=аэродром, радиус=радиус)
    возврат = []
    for _ in df.index:
        if df.loc[_]['Вид'] == "УА": возврат.append(_)
        else: ...
    return возврат

def Распределённый_пассажиропоток(аэродром='UNWW', радиус=1000):
    """Функция возвращает значение распределённого суточного
    пассажиропотока узлового аэропорта."""
    количество_УА = Количество_УА(аэродром=аэродром, радиус=радиус)
    перечень = Коды_УА_зоны(аэродром=аэродром, радиус=радиус)
    пассажиропоток = РПП(аэродром=аэродром)
    пассажиропоток_суточный = int(round((пассажиропоток/365), 0))
    сумма_входящих_пассажиропотоков = 0
    for _ in перечень:
        if Количество_УА(аэродром=_):
            входящий_суточный_пассажиропоток = (РПП(аэродром=_)/Количество_УА(аэродром=_))/365
        else:
            входящий_суточный_пассажиропоток = РПП(аэродром=_)/365
        сумма_входящих_пассажиропотоков += входящий_суточный_пассажиропоток
    if количество_УА:
        распределённый_пассажиропоток = пассажиропоток_суточный/количество_УА
    else:
        распределённый_пассажиропоток = пассажиропоток_суточный
    возврат = int(round(сумма_входящих_пассажиропотоков + распределённый_пассажиропоток, 0))
    return возврат

def Баланс_рейса(вылет="UNWW", прилёт="UNNT", загрузка=0.7, тариф=3000):
    себестоимость = Расчёт_себестоимости_рейса(вылет=вылет, прилёт=прилёт)
    категория_маршрута = Категория_маршрута(вылет=вылет, прилёт=прилёт)
    среднесуточный_пассажиропоток = int(round(РПП(аэродром=вылет)/365, 0))
    тип_самолёта = Расчётный_тип_ВС(рпп=среднесуточный_пассажиропоток, категория=категория_маршрута)
    кресел = Количество_кресел(тип=тип_самолёта)
    проданных_билетов = int(round(кресел*загрузка, 0))
    валовый_доход = проданных_билетов * тариф
    return себестоимость - валовый_доход


# st.cache_data
# def наименования():
#     s = read_csv("../csv/Сводка.csv", index_col='ICAO')
#     возврат = [Наименование(_) for _ in s.index]
#     return возврат

def Изменить_флаг(строка='UNWW'):
    csv='../csv/Сводка.csv'
    столбец='Учитывать'
    d = read_csv(csv, index_col='ICAO')
    d.to_csv(csv[:len(csv)-4]+'_архив.csv', index='ICAO')
    d.loc[строка, столбец] = not d.loc[строка, столбец]
    d.to_csv(csv, index='ICAO')
    del d
    return None



def Получить_таблицу():
    d = read_csv('../csv/FTD.csv', index_col='FT')
    d[(d.D <= 1000) & (d.D > 0)]
    маршруты = []
    s = read_csv('../csv/Сводка.csv', index_col='ICAO')

    for _ in s.index:
        if s.loc[_]['Учитывать']:
            for __ in s.index:
                if s.loc[__]['Учитывать']:
                    try:
                        вылет = _
                        прилёт = __
                        дистанция = s.loc[_ + __]['D']
                        маршруты.append(
                            dict(
                                вылет=вылет, 
                                прилёт=прилёт,
                                дистанция=дистанция))
                    except: ...
                    finally: ...
    return DataFrame(маршруты)