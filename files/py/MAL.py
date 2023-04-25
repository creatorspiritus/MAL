import pandas as pd
from pathlib import Path
from operator import attrgetter
from collections import namedtuple
from configparser import ConfigParser
from datetime import timedelta, time, datetime

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
	При создании экземпляра класса требуется
	обязательный ввод значения кода ИКАО аэродрома
	Пример: NOZ = А('UNWW')
	'''
	def __init__(я, *СЧ, **РЧ):
		_РЧ = РЧ
		_СЧ = []
		f = pd.read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
		for _ in f.columns:
			_РЧ[_] = РЧ.get(_, f.loc[СЧ[0].upper()][_])
		f = pd.read_csv('../csv/СА1.csv', index_col='ICAO')
		for _ in f.columns:
			_РЧ[_] = РЧ.get(_, f.loc[СЧ[0].upper()][_])
		f = pd.read_csv('../csv/FTD.csv', index_col='FT')
		for _ in f.index:
			if _[:4] == СЧ[0].upper():
				if f.loc[_]['D'] < 1000:
					_СЧ.append(_[4:])
		super().__init__(*_СЧ, **_РЧ)
		del _РЧ, f, _СЧ
	
	def __repr__(я):
		возврат = ''
		for _ in я.РЧ:
			показатель = _ + ': \n'
			значение = str(я.РЧ[_]) +'\n\n'
			возврат += показатель + значение
		del  показатель, значение
		return возврат