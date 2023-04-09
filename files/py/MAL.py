from pandas import read_csv
from collections import namedtuple

КТА = namedtuple('КТА', 'широта долгота превышение')

ВПП = namedtuple('ВПП', 'длина ширина тип курс освещение')

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