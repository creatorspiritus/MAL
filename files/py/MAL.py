import pandas as pd
from pathlib import Path
from operator import attrgetter
from collections import namedtuple
from configparser import ConfigParser
from datetime import timedelta, time, datetime

КТА = namedtuple('КТА', 'широта долгота превышение')

def MCA(t, h):
	"""
	ФУНКЦИЯ
	Определение МСА аэродрома
	Входные параметры: температура в градусах Цельсия и высота КТА в метрах
	Возвращаемое значение: МСА аэродрома
	ТВЗ: int или None (в случае выхода параметров за предельные значения)
	"""
	h = h / 0.3048 # Перевод метры в футы
	MCAm60t = [-54, -45]
	MCAm60h = [4500, 0]
	MCAm50t = [-54, -35]
	MCAm50h = [9500, 0]
	MCAm40t = [-54, -25]
	MCAm40h = [14500, 0]
	MCAm30t = [-54, -15]
	MCAm30h = [19500, 0]
	MCAm20t = [-54, -5]
	MCAm20h = [24500, 0]
	MCAm10t = [-45, 5]
	MCAm10h = [25000, 0]
	MCAt = [-35, 15]
	MCAh = [25000, 0]
	MCAp10t = [-25, 25]
	MCAp10h = [25000, 0]
	MCAp20t = [-15, 35]
	MCAp20h = [25000, 0]
	MCAp30t = [-5, 45]
	MCAp30h = [25000, 0]
	результат = None
	if (-54 <= t <= -45) and (0 <= h <= 4500):
		результат = interp(t, MCAm60t, MCAm60h)
		if 0 <= результат: return -60
	elif (-54 <= t <= -35) and (0 <= h <= 9500):
		результат = interp(t, MCAm50t, MCAm50h)
		if 0 <= результат: return -50
	elif (-54 <= t <= -25) and (0 <= h <= 14500):
		результат = interp(t, MCAm40t, MCAm40h)
		if 0 <= результат: return -40
	elif (-54 <= t <= -15) and (0 <= h <= 19500):
		результат = interp(t, MCAm30t, MCAm30h)
		if 0 <= результат: return -30
	elif (-54 <= t <= -5) and (0 <= h <= 24500):
		результат = interp(t, MCAm20t, MCAm20h)
		if 0 <= результат: return -20
	elif (-45 <= t <= 5) and (0 <= h <= 25000):
		результат = interp(t, MCAm10t, MCAm10h)
		if 0 <= результат: return -10
	elif (-35 <= t <= 15) and (0 <= h <= 25000):
		результат = interp(t, MCAt, MCAh)
		if 0 <= результат: return 0
	elif (-25 <= t <= 25) and (0 <= h <= 25000):
		результат = interp(t, MCAp10t, MCAp10h)
		if 0 <= результат: return 10
	elif (-15 <= t <= 35) and (0 <= h <= 25000):
		результат = interp(t, MCAp20t, MCAp20h)
		if 0 <= результат: return 20
	elif (-5 <= t <= 45) and (0 <= h <= 25000):
		результат = interp(t, MCAp30t, MCAp30h)
		if 0 <= результат: return 30
	else: print('ВНИМАНИЕ! Выход за пределы эксплуатационных параметров!')
	return результат

class Я:
	def __init__(я, *СЧ, **РЧ):
		я.__СЧ = СЧ
		я.__РЧ = РЧ
	
	@property
	def СЧ(я): return я.__СЧ
		
	@property
	def РЧ(я): return я.__РЧ

class ИД(Я):
	"""
	Класс ИД (Исходные данные) 
	обеспечивает хранение
	и применение исходных данных
	проекта МАЛ
	"""
	def __init__(я, *СЧ, **РЧ):
		i = ConfigParser()
		i.read('../ini/МАЛ.ini', encoding='utf8')
		for _ in i.sections():
			РЧ[_] = РЧ.get(_, {})
			for __ in i[_]:
				РЧ[_][__] = i[_][__]
		РЧ['Каталог'] = Path().absolute().parent
		super().__init__(*СЧ, **РЧ)

class А(Я):
	'''
	Класс АЭРОДРОМ
	При создании экземпляра класса 
	требуется обязательный ввод 
	значения кода ИКАО аэродрома
	Пример: NOZ = А('UNWW')
	'''
	def __init__(я, *СЧ, **РЧ):
		_РЧ = РЧ
		_СЧ = []
		f = pd.read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
		_РЧ['ICAO'] = СЧ[0].upper()
		for _ in f.columns:
			_РЧ[_] = РЧ.get(_, f.loc[СЧ[0].upper()][_])
		f = pd.read_csv('../csv/СА.csv', index_col='ICAO')
		for _ in f.columns:
			_РЧ[_] = РЧ.get(_, f.loc[СЧ[0].upper()][_])
		f = pd.read_csv('../csv/FTD.csv', index_col='FT')
		for _ in f.index:
			if _[:4] == СЧ[0].upper():
				if f.loc[_]['D'] < 1000:
					_СЧ.append(_[4:])
		super().__init__(*_СЧ, **_РЧ)
		del _РЧ, f, _СЧ
	
	@property
	def УА(я):
		if я.РЧ['Вид'] == 'УА': return True
		else: return False
	
	@property
	def АН(я):
		if я.РЧ['Вид'] == 'АН': return True
		else: return False
	
	@property
	def КТА(я):
		'''
		СВОЙСТВО
		Характеристика контрольной точки
		аэродрома
		ТВЗ: namedtuple КТА
		'''
		return КТА(
			я.РЧ['Широта КТА'],
			я.РЧ['Долгота КТА'],
			я.РЧ['Превышение'])
			
	@property
	def НВ(я):
		'''
		СВОЙСТВО
		Все возможные направления полётов
		ТВЗ: list
		'''
		возврат = []
		for _ in я.СЧ:
			if isinstance(_, str) and (len(_) == 4): возврат.append(_)
		return возврат
	
	@property
	def НП(я):
		'''
		СВОЙСТВО
		Направления полётов с учётом 
		категории аэропортов, даты ввода 
		в эксплуатацию ближайших опорных 
		аэродромов, типов ВС
		'''
		возврат = []
		return возврат
	
	@property
	def ОА(я):
		'''
		СВОЙСТВО
		Возвращает именованный кортеж
		с информацией о порядковом
		номере опорного аэродрома,
		дате ввода в эксплуатацию или
		None
		'''
		возврат = False
		for _ in ИД().РЧ['Опорные аэродромы']:
			if я.РЧ['ICAO'].lower() == _.lower():
				возврат = True
			else: ...
		return возврат

	
	def __repr__(я):
		возврат = ''
		for _ in я.РЧ:
			показатель = _ + ': \n'
			значение = str(я.РЧ[_]) +'\n\n'
			возврат += показатель + значение
		del  показатель, значение
		return возврат
