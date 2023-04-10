from pandas import read_csv
from collections import namedtuple

КТА = namedtuple('КТА', 'широта долгота превышение')

ВПП = namedtuple('ВПП', 'длина ширина тип курс освещение')

# Беспосадочный маршрут
БПМ = namedtuple('Маршрут', 'откуда куда дистанция')

class Я:
	def __init__(я, *СЧ, **РЧ):
		я.__СЧ = СЧ
		я.__РЧ = РЧ
	
	@property
	def СЧ(я): return я.__СЧ

		
	@property
	def РЧ(я): return я.__РЧ

class А(Я):
	'''
	Класс АЭРОДРОМ
	При создании экземпляра класса требуется
	обязательный ввод значения кода ИКАО аэродрома
	Пример: NOZ = А('UNWW')
	'''
	@property
	def ICAO(я):
		try: возврат = я.СЧ[0].upper()
		except:
			print('ОШИБКА! Нет информации о коде ИКАО')
			возврат = None
		return возврат
	
	@property
	def IATA(я):
		'''
		Свойство возвращает код ИАТА аэропорта или None, когда для указанного кода ИКАО 
		аэродрома не найден соответствующий код ИАТА 
		аэропорта. 
		Тип: 			str
		'''
		try:
			f = read_csv('../csv/IATA.csv', index_col='icao')
			возврат = f.loc[я.ICAO]['iata']
		except: 
			print('ОШИБКА! Не найдено соответствие кодов ИКАО и ИАТА')
			возврат = None
		finally: return возврат
	
	@property
	def КТА(я):
		'''
		Свойство возвращает координаты и высоту КТА аэродрома
		Тип: 			namedtuple('КТА' 'широта долгота превышение')
		'''
		try:
			f = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
			возврат = КТА(
				f.loc[я.ICAO]['Широта КТА'],
				f.loc[я.ICAO]['Долгота КТА'],
				f.loc[я.ICAO]['Превышение'])
		except: 
			print('ОШИБКА! Не найден код ИКАО в перечне аэродромов АОПА')
			возврат = None
		finally: return возврат
	
	@property
	def ВПП(я):
		'''
		Свойство возвращает характеристики основной взлётно-посадочной полосы аэродрома
		Тип: 			namedtuple('ВПП', 'длина ширина тип курс освещение')
		'''
		try:
			f = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
			возврат = ВПП(
				f.loc[я.ICAO]['Длина основной ВПП'],
				f.loc[я.ICAO]['Ширина основной ВПП'],
				f.loc[я.ICAO]['Покрытие основной ВПП'],
				f.loc[я.ICAO]['Магнитный курс основной ВПП'],
				f.loc[я.ICAO]['Освещение основной ВПП'])
		except: 
			print('ОШИБКА! Не найден код ИКАО в перечне аэродромов АОПА')
			возврат = None
		finally: return возврат
	
	@property
	def Примечание(я):
		'''
		Свойство возвращает дополнительную информацию по аэродрому
		Тип: 			str
		'''
		try:
			f = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
			возврат = f.loc[я.ICAO]['Примечание']
		except: 
			print('ОШИБКА! Не найден код ИКАО в перечне аэродромов АОПА')
			возврат = None
		finally: return возврат
	
	@property
	def Электропочта(я):
		'''
		Свойство возвращает адрес электронной почты аэродрома
		Тип: 			str
		'''
		try:
			f = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
			возврат = f.loc[я.ICAO]['Email']
		except: 
			print('ОШИБКА! Не найден код ИКАО в перечне аэродромов АОПА')
			возврат = None
		finally: return возврат
	
	@property
	def Город(я):
		'''
		Свойство возвращает регион аэродрома
		Тип: 			str
		'''
		try:
			f = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
			возврат = f.loc[я.ICAO]['Город']
		except: 
			print('ОШИБКА! Не найден код ИКАО в перечне аэродромов АОПА')
			возврат = None
		finally: return возврат
	
	@property
	def Название(я):
		'''
		Свойство возвращает регион аэродрома
		Тип: 			str
		'''
		try:
			f = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
			возврат = f.loc[я.ICAO]['Название']
		except: 
			print('ОШИБКА! Не найден код ИКАО в перечне аэродромов АОПА')
			возврат = None
		finally: return возврат
	
	@property
	def Действующий(я):
		'''
		Свойство возвращает True или False
		Тип: 			bool
		'''
		try:
			f = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
			возврат = True if f.loc[я.ICAO]['Действующий'] == 'Действующий' else False
		except: 
			print('ОШИБКА! Не найден код ИКАО в перечне аэродромов АОПА')
			возврат = None
		finally: return возврат
	
	@property
	def Тип(я):
		'''
		Свойство возвращает регион аэродрома
		Тип: 			str
		'''
		try:
			f = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
			возврат = f.loc[я.ICAO]['Тип']
		except: 
			print('ОШИБКА! Не найден код ИКАО в перечне аэродромов АОПА')
			возврат = None
		finally: return возврат
	
	@property
	def Направления(я):
		'''
		Свойство возвращает список аэродромов в радиусе зоны влияния аэродрома
		Тип: 			list
		'''
		возврат = []
		try:
			f = read_csv('../csv/FTD.csv', index_col='FT')
			for _ in f.index:
				FT = я.ICAO+_[4:]
				if (FT == _ )and (f.loc[FT]['D'] < 1000):
					возврат.append(БПМ(я.ICAO, _[4:], f.loc[FT]['D']))
		except: 
			print('ОШИБКА! Не найден файл дистанций')
		finally: return возврат
	
	@property
	def СПП(я):
		'''
		СПП - Существующий пассажиропоток
		Свойство возвращает значение текущего пассажиропотока из аэропорта
		Тип: 			float
		'''
		try:
			f = read_csv('../csv/Сводка.csv', index_col='ICAO')
			возврат = f.loc[я.ICAO]['Пассажиропоток']
		except: 
			print('ОШИБКА! Не найден файл Сводка.csv')
			возврат = None
		finally: return возврат
	
	@property
	def СГП(я):
		'''
		СГП - Существующий грузопотокоток
		Свойство возвращает значение текущего грузопотока из аэропорта
		Тип: 			float
		'''
		try:
			f = read_csv('../csv/Сводка.csv', index_col='ICAO')
			возврат = f.loc[я.ICAO]['Груз, тонн']
		except: 
			print('ОШИБКА! Не найден файл Сводка.csv')
			возврат = None
		finally: return возврат
		
	@property
	def СПО(я):
		'''
		СПО - Существующий потокоток почтовых отправдений
		Свойство возвращает значение текущей отправки почтв из аэропорта
		Тип: 			float
		'''
		try:
			f = read_csv('../csv/Сводка.csv', index_col='ICAO')
			возврат = f.loc[я.ICAO]['Почта, тонн']
		except: 
			print('ОШИБКА! Не найден файл Сводка.csv')
			возврат = None
		finally: return возврат
		
	@property
	def ТС(я):
		'''
		ТС - Стоимость ТС-1 в аэропорте
		Свойство возвращает значение текущей стоимости ТС-1 в аэропорте. Если 0 - заправка отсутствует
		Тип: 			float
		'''
		try:
			f = read_csv('../csv/Сводка.csv', index_col='ICAO')
			возврат = f.loc[я.ICAO]['Цена ТС-1, руб']
		except: 
			print('ОШИБКА! Не найден файл Сводка.csv')
			возврат = None
		finally: return возврат
	
	@property
	def Категория(я):
		'''
		ТС - Стоимость ТС-1 в аэропорте
		Свойство возвращает значение текущей стоимости ТС-1 в аэропорте. Если 0 - заправка отсутствует
		Тип: 			float
		'''
		try:
			f = read_csv('../csv/Сводка.csv', index_col='ICAO')
			возврат = int(f.loc[я.ICAO]['Категория'])
		except: 
			print('ОШИБКА! Не найден файл Сводка.csv')
			возврат = None
		finally: return возврат
	
	@property
	def Заправка(я):
		'''
		Свойство возвращает True если заправка есть и False, если заправка в аэропорте не производится
		Тип: 			bool
		'''
		if int(я.ТС): return  True
		else: return False