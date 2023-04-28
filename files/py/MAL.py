import pandas as pd
from pathlib import Path
from operator import attrgetter
from collections import namedtuple
from configparser import ConfigParser
from datetime import timedelta, time, datetime

КТА = namedtuple('КТА', 'широта долгота превышение')

class Я:
	def __init__(я, *СЧ, **РЧ):
		я.__СЧ = СЧ
		я.__РЧ = РЧ
	
	@property
	def СЧ(я): return я.__СЧ
		
	@property
	def РЧ(я): return я.__РЧ

class ИД(Я):
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