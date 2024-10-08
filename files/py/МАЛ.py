import pandas as pd
import json
from pathlib import Path
from operator import attrgetter
from collections import namedtuple
from configparser import ConfigParser
from datetime import timedelta, time, datetime
import numpy as np
import folium
from folium.raster_layers import WmsTileLayer
from folium.raster_layers import TileLayer
from dateutil.relativedelta import relativedelta

КТА = namedtuple('КТА', 'широта долгота превышение')
ВПП = namedtuple('ВПП', 'длина ширина тип курс освещение')

# Беспосадочный маршрут 
# АВ - агломерация аэропорта вылета
# АП - агломерация аэропорта прибытия
БПМ = namedtuple('Маршрут', 'откуда куда дистанция АВ АП')
СДА = namedtuple('АЭРОДРОМ', 'ICAO IATA название город широта долгота превышение узловой категория агломерация очередь дата')
ВРЕМЯ = namedtuple('ВРЕМЯ', 'timedelta час мин')



# Структура себестоимости рейса
# АвиаГСМ = 25
# Амортизация = 1
# Аэропортовое = 30
# ТОиР = 13
# АЭНО = 3
# Метео = 1
# Агентские = 1
# Аренда = 3
# Страхование = 0.6
# Прочие = 5
# Общепроизводственные = 4.4
# ФОТ = 10
# Начисления = 3
ССР = namedtuple('СЕБЕСТОИМОСТЬ', 'АвиаГСМ Амортизация Аэропортовое ТОиР АЭНО Метео Агентские Аренда Страхование Прочие Общепроизводственные ФОТ Начисления')

class Я:
	def __init__(я, *СЧ, **РЧ):
		я.__СЧ = СЧ
		я.__РЧ = РЧ
	
	@property
	def СЧ(я): return я.__СЧ
		
	@property
	def РЧ(я): return я.__РЧ
 
	def ДЧ(я, *СЧ, **РЧ):
		"""
		Метод добавляет содержательные и реквизитные элементы в экемпляр класса
		"""	
		я.__СЧ = я.СЧ + СЧ 
		я.__РЧ = я.РЧ | РЧ


class ИД(Я):
	"""
	Класс ИД (ИСХОДНЫЕ ДАННЫЕ)
	Хранение и обновление исходных данных проекта
	"""
	def __init__(я, *СЧ, **РЧ):
		try:
			i = ConfigParser()
			i.read('../ini/МАЛ.ini', encoding='utf8')
			доллар = i['Курсы валют']['доллар']
			евро = i['Курсы валют']['евро']
			юань = i['Курсы валют']['юань']
			try:
				kv = pd.read_xml('https://www.cbr-xml-daily.ru/daily_utf8.xml')
				доллар = str(float(kv.set_index('Name').loc['Доллар США']['Value'].replace(',', '.')))
				евро = str(float(kv.set_index('Name').loc['Евро']['Value'].replace(',', '.')))
				юань = str(float(kv.set_index('Name').loc['Китайский юань']['Value'].replace(',', '.')))
				with open('../ini/МАЛ.ini', 'w') as configfile:
					i.write(configfile)
			except: ...
			finally:
				i.set('Курсы валют', 'Доллар', доллар)
				i.set('Курсы валют', 'Евро', евро)
				i.set('Курсы валют', 'Юань', юань)
			for _ in i.sections():
				РЧ[_] = РЧ.get(_, {})
				for __ in i[_]:
					РЧ[_][__] = i[_][__]
			РЧ['Каталог'] = Path().absolute().parent		
		except:
			print('ОШИБКА! Проверить наличие файла МАЛ.ini')
		finally:
			return super().__init__(*СЧ, **РЧ)
	
	@property
	def СА(я):
		"""
		СВОЙСТВО 
		Сумма агломераций в радиусе 100 км от КТА всех аэропортов проекта
		"""
		возврат = 0
		for _ in я.РЧ['Аэродромы проекта']:
			возврат += АЭРОДРОМ(_).Агломерация
		# Исключение из расчётов трёх аэропортов московского авиаузла
		возврат -= (АЭРОДРОМ('UUDD').Агломерация + АЭРОДРОМ('UUEE').Агломерация + АЭРОДРОМ('UUBW').Агломерация)
		return возврат

	def Карта(я, тип = 'аэродромы', вид = 'рельеф', 
		направления=False, зона500 = False, зона1000 = False):
		"""
        ФУНКЦИЯ
		Возвращает карту с опорными аэродромами проекта
        Исходные данные:
            - тип:
                - аэродромы
            - вид:
                - рельеф
			- направления:
				- False (аэродромы направлений не отображаются)
				- True (аэродромы направлений отображаются)
			- зона500:
				- True (на карту наносится зона полётов ЛМС-901 в радиусе 500 км от КТА)
				- False (не отображается)
			- зона1000:
				- True (на карту наносится зона полётов Ил-114-300 и ТВРС-44 в радиусе 1000 км от КТА)
				- False (не отображается)
        """
		карта = None
		центр = (66.413951, 94.241942)  # Географический центр РФ
		if тип == 'аэродромы':
			карта = folium.Map(
				location=центр, zoom_start=4, width='100%')
			"""
			    "http://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer" // World Topographic Map
			    "http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer" // World Street Map
			    "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer" // Light Gray Canvas
			    "http://services.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer" // National Geographic World Map
			    "http://services.arcgisonline.com/ArcGIS/rest/services/Ocean_Basemap/MapServer" // Ocean Basemap
			    "http://services.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer" // Terrain with Labels
			    "http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer" // World Imagery
			"""
			ссылка = (
				'http://services.arcgisonline.com/arcgis/rest/services/World_Shaded_Relief'
				+ '/MapServer/tile/{z}/{y}/{x}')
			WmsTileLayer(
				url=ссылка,
				layers=None,
				name='ESRI Shaded',
				attr='ESRI World Shaded Relief',).add_to(карта)
			for _ in я.ОА:
				точка = folium.map.FeatureGroup()
				точка.add_child(
					folium.features.CircleMarker(
						[_.широта, _.долгота], radius=3,
						color='blue', fill_color='blue', 
					)
				)
				карта.add_child(точка)
            
			if зона500:
				folium.Polygon(
					[(_.latitude, _.longitude) for _ in я.Круг(радиус=500)],
					color='blue', weight=0, fill=True, fill_color='blue',
					fill_opacity=0.1).add_to(карта)

			if зона1000:
				folium.Polygon(
					[(_.latitude, _.longitude) for _ in я.Круг()],
					color='blue', weight=0, fill=True, fill_color='blue',
					fill_opacity=0.1).add_to(карта)
			
			if направления:
				for _ in я.РЧ['Аэродромы проекта']:
					аэродром = АЭРОДРОМ(_)
					точка = folium.map.FeatureGroup()
					точка.add_child(
						folium.features.CircleMarker(
							[аэродром.КТА.широта, аэродром.КТА.долгота], 
							radius=2, color='grey', fill_color='grey',
						tooltip=_))
					карта.add_child(точка)

		elif тип == 'города':
			карта = folium.Map(
				location=центр, zoom_start=8, width='100%')
			folium.Polygon([(_.latitude, _.longitude) for _ in я.Круг(радиус=100)],
				color='gray',
				weight=0,
				fill=True,
				fill_color='gray',
				fill_opacity=0.1).add_to(карта)
            
			try:
				путь = '../csv/Агломерации/'+str(я.ICAO)+'_агломерации.csv'
				g = pd.read_csv(путь)
				for _ in g.index:
					точка = folium.map.FeatureGroup()
					точка.add_child(
						folium.features.CircleMarker(
							[g.loc[_]['Широта'], g.loc[_]['Долгота']], 
							radius=3, color='gray', fill_color='gray', 
							tooltip=g.loc[_]['Название'] + '|' + str(g.loc[_]['Население'])))
					карта.add_child(точка)
			except: ...
			finally: ...
		return карта
	
	@property
	def ОА(я):
		"""
  		СВОЙСТВО 
		Список кодов ИКАО опорных аэродромов проекта
		ТВЗ: namedtuple СДА
		"""
		возврат = []
		for _ in я.РЧ['Опорные аэродромы']:
			значение = я.РЧ['Опорные аэродромы'][_].split(' ')
			очередь = значение[0]
			# Следующий месяц
			# print(dt_now + relativedelta(months=+1))
			СП = datetime(
				int(я.РЧ['Даты']['начало проекта'].split('.')[0]),
				int(я.РЧ['Даты']['начало проекта'].split('.')[1]),
				int(я.РЧ['Даты']['начало проекта'].split('.')[2]))
			дата = СП + relativedelta(months=+3*int(очередь))
			возврат.append(
       			СДА(
            # ICAO IATA название город широта долгота превышение узловой категория агломерация
            АЭРОДРОМ(_.upper()).ICAO,
            АЭРОДРОМ(_.upper()).IATA,
            АЭРОДРОМ(_.upper()).Название,
            АЭРОДРОМ(_.upper()).Город,
            АЭРОДРОМ(_.upper()).КТА.широта,
            АЭРОДРОМ(_.upper()).КТА.долгота,
            АЭРОДРОМ(_.upper()).КТА.превышение,
            АЭРОДРОМ(_.upper()).Узловой,
            АЭРОДРОМ(_.upper()).Категория,
            АЭРОДРОМ(_.upper()).Агломерация,
            очередь,
            дата
				)
			)
		return возврат
     
	@property
	def ДНОЭ(я):
		"""
		СВОЙСТВО
		ДНОЭ - дата начала основного этапа
		ТВЗ: datetime
		"""
		return datetime(
			int(я.РЧ['Даты']['начало проекта'].split('.')[0]),
			int(я.РЧ['Даты']['начало проекта'].split('.')[1]),
			int(я.РЧ['Даты']['начало проекта'].split('.')[2]))


class АЭРОДРОМ(Я):
	'''
	Класс АЭРОДРОМ
	При создании экземпляра класса требуется обязательный ввод значения 
	кода ИКАО аэродрома. Значение используется для получения основных данных
	аэродрома и аэропорта.
	Пример: NOZ = АЭРОДРОМ('UNWW')
	'''
	def __init__(я, *СЧ, **РЧ):
		аэродромы = pd.read_csv('../csv/Сводка.csv', index_col='ICAO')
		try:
			РЧ['ICAO'] = РЧ.get('ICAO', СЧ[0])
		except:
			print('[ОШИБКА] Проверить код ICAO' )
		finally: del аэродромы
		super().__init__(*СЧ, **РЧ)

	@property
	def ICAO(я):
		try: 
			if len(я.СЧ[0]) == 4: возврат = я.СЧ[0].upper()
			elif len(я.СЧ[0]) == 3:
				f = pd.read_csv('../csv/IATA.csv', index_col='iata')
				возврат = f.loc[я.СЧ[0]]['icao'].upper()
			else: raise ValueError()
		except:
			print('[ОШИБКА] Нет информации о коде ИКАО')
			возврат = None
		finally: return возврат
	
	@property
	def IATA(я):
		'''
		Свойство возвращает код ИАТА аэропорта или None, когда для указанного кода ИКАО 
		аэродрома не найден соответствующий код ИАТА 
		аэропорта. 
		Тип: 			str
		'''
		try:
			f = pd.read_csv('../csv/IATA.csv', index_col='icao')
			возврат = f.loc[я.ICAO]['iata']
		except: 
			print('[ПРЕДУПРЕЖДЕНИЕ] Не найден код ИАТА для аэродрома ' + я.ICAO)
			возврат = ''
		finally:
			if isinstance(возврат, float): возврат = ''
			return возврат
	
	@property
	def КТА(я):
		'''
		Свойство возвращает координаты и высоту КТА аэродрома
		Тип: 			namedtuple('КТА' 'широта долгота превышение')
		'''
		try:
			f = pd.read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
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
			f = pd.read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
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
			f = pd.read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
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
			f = pd.read_csv('../csv/aopa-points-export.csv', encoding='utf8', sep=';', index_col='Индекс')
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
			f = pd.read_csv('../csv/aopa-points-export.csv', encoding='utf8', sep=';', index_col='Индекс')
			возврат = str(f.loc[я.ICAO]['Город'])
		except: 
			print('ОШИБКА! Не найден код ИКАО в перечне аэродромов АОПА')
			возврат = ''
		finally:
			if isinstance(возврат, float) or (возврат == 'nan'): возврат = ''
			return возврат
	
	@property
	def Название(я):
		'''
		Свойство возвращает регион аэродрома
		Тип: 			str
		'''
		try:
			f = pd.read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
			возврат = str(f.loc[я.ICAO]['Название'])
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
			f = pd.read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
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
			f = pd.read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
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
			f = pd.read_csv('../csv/FTD.csv', index_col='FT')
			a = pd.read_csv('../csv/Агломерация.csv', index_col='ICAO')
			for _ in f.index:
				FT = я.ICAO+_[4:]
				if (FT == _ )and (f.loc[FT]['D'] < 1000):
					возврат.append(БПМ(я.ICAO, _[4:], f.loc[FT]['D'], a.loc[я.ICAO]['Агломерация'], a.loc[_[4:]]['Агломерация']))
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
			f = pd.read_csv('../csv/Сводка.csv', index_col='ICAO')
			возврат = f.loc[я.ICAO]['Пассажиропоток']
		except: 
			print('ОШИБКА! Не найден код ' + str(я.ICAO) + ' в файле Сводка.csv')
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
			f = pd.read_csv('../csv/Сводка.csv', index_col='ICAO')
			возврат = f.loc[я.ICAO]['Груз, тонн']
		except: 
			print('ОШИБКА! Не найдено значение грзопотока для кода ' + str(я.ICAO) + ' файл Сводка.csv')
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
			f = pd.read_csv('../csv/Сводка.csv', index_col='ICAO')
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
			f = pd.read_csv('../csv/Сводка.csv', index_col='ICAO')
			возврат = f.loc[я.ICAO]['Цена ТС-1, руб']
		except: 
			print('ОШИБКА! Не найдено значение стоимости ТС-1 для кода ' + str(я.ICAO) + ' файл Сводка.csv')
			возврат = None
		finally: return возврат
	
	@property
	def Категория(я):
		'''
		Свойство возвращает категорию аэродрома в терминологии проекта МАЛ.
		Возвращаемые значения:
			- 1 (возможна эксплуатация всех расчётных типов проекта);
			- 2 (возможна эксплуатация ТВРС-44 и ЛМС-901);
			- 3 (возможна эксплуатация ЛМС-901);
			- 0 (нет технической возможности эксплуатации ВС расчётных типов)
		Тип: 	int
		'''
		try:
			f = pd.read_csv('../csv/Сводка.csv', index_col='ICAO')
			возврат = int(f.loc[я.ICAO]['Категория'])
		except: 
			print('ОШИБКА! Не найдено значение категории для кода ' + str(я.ICAO) + ' файл Сводка.csv')
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
		
	@property
	def Узловой(я):
		'''
		Свойство возвращает True когда аэропорт узловой. В другом случае - False 
		Тип: 			bool
		'''
		f = pd.read_csv('../csv/Сводка.csv', index_col='ICAO')
		if f.loc[я.ICAO]['Вид'] == 'УА': return True
		else: return False
	
	@property
	def Кандидат(я):
		'''
		Свойство возвращает True при наличии технической возможности использования аэропорта в качестве опорного аэродрома проекта. В другом случае - False 
		Тип: 			bool
		'''
		f = pd.read_csv('../csv/Сводка.csv', index_col='ICAO')
		if f.loc[я.ICAO]['Вид'] == 'УА': return True
		else: return False
		
	@property
	def Агломерация(я):
		'''
		Свойство возвращает значение агломерации населения в районе аэродрома
		Тип: 			int
		'''
		try:
			f = pd.read_csv('../csv/Агломерация.csv', index_col='ICAO')
			возврат = f.loc[я.ICAO]['Агломерация']
		except: 
			print('ОШИБКА! Не найден файл Агломерация.csv')
			возврат = None
		finally: return возврат
	
	@property
	def МВПП(я):
		'''
		МВПП - маскимально возможный пассажиропоток аэропорта
		Свойство возвращает значение максимально возможного пассажиропотока.
		Расчёт значения производится по формуле:
			МВПП = Капа * Ан,
			где
				Капа 	- коэффициент авиационной подвижности населения для данного вида
								аэродрома. Для узлового аэропорта коэффициент равен 2.5.
								Для аэропорта назначения - 4.2 (см. исходные данныые ini-файла)
				Ан		- Агломерация населения
		В том случае, когда значение агломерации населения не опрелено (равно нулю),
		максимально возможный пассажиропоток определяется как произведение пассажирской
		вместимости самолёта ЛМС-901 на количество дней в календарном году.
		
		Тип: 			int
		'''
		try:
			f = pd.read_csv('../csv/Агломерация.csv', index_col='ICAO')
			i = ConfigParser()
			i.read('../ini/МАЛ.ini', encoding='utf8')
			if я.Узловой: возврат = int(f.loc[я.ICAO]['Агломерация'] * float(i['Коэффициенты авиационной подвижности населения']['Средний']))
			else: возврат = int(f.loc[я.ICAO]['Агломерация'] * float(i['Коэффициенты авиационной подвижности населения']['Максимальный']))
			if not возврат: возврат = int(9 * 365)
		except: 
			print('ОШИБКА! Проверить файлы Агломерация.csv и МАЛ.ini')
			возврат = None
		finally: return возврат
		
	@property
	def МВКРИЛ(я):
		'''
		МВКРИЛ - маскимально возможное количество рейсов самолёта Ил-114-300 
		из аэропорта при расчётном значениии МВПП
		Свойство возвращает значение максимально возможное ежедневное количество
		рейсов для самолёта Ил-114-300 при расчётном значении МВПП
		Расчёт значения производится по формуле:
			МВКРИЛ = (МВПП - я.СПП)/ (Кпк * 365) ,
			где
				Кпк 	- Количество пассажирских кресел в самолёте Ил-114-300
				МВПП	- Максимально возможное годовое значение пассажиропотока из аэропорта
		
		Тип: 			int
		'''
		return int((я.МВПП - я.СПП) / (68 * 365))
	
	@property
	def МВКРТВРС(я):
		'''
		МВКРТВРС - маскимально возможное количество рейсов самолёта ТВРС-44 "Ладога" 
		из аэропорта при расчётном значениии МВПП
		Свойство возвращает значение максимально возможное ежедневное количество
		рейсов для самолёта ТВРС-44 "Ладога" при расчётном значении МВПП
		Расчёт значения производится по формуле:
			МВКРИЛ = (МВПП - я.СПП)/ (Кпк * 365) ,
			где
				Кпк 	- Количество пассажирских кресел в самолёте ТВРС-44 "Ладога"
				МВПП	- Максимально возможное годовое значение пассажиропотока из аэропорта
		
		Тип: 			int
		'''
		return int((я.МВПП - я.СПП) / (44 * 365))
	
	@property
	def МВКРЛМС(я):
		'''
		МВКРЛМС - маскимально возможное количество рейсов самолёта ЛМС-901 "Байкал" 
		из аэропорта при расчётном значениии МВПП
		Свойство возвращает значение максимально возможное ежедневное количество
		рейсов для самолёта ЛМС-901 "Байкал" при расчётном значении МВПП
		Расчёт значения производится по формуле:
			МВКРИЛ = (МВПП - я.СПП)/ (Кпк * 365) ,
			где
				Кпк 	- Количество пассажирских кресел в самолёте ЛМС-901 "Байкал"
				МВПП	- Максимально возможное годовое значение пассажиропотока из аэропорта
		
		Тип: 			int
		'''
		return int((я.МВПП - я.СПП) / (9 * 365))
	
	@property
	def МВКРОАЭ(я):
		'''
		МВКРОАЭ - маскимально возможное количество рейсов самолётов объединённой авиационной эскадрильи из аэропорта при расчётном значениии МВПП
		Свойство возвращает значение максимально возможное ежедневное количество
		рейсов для самолётов ОАЭ (3 ВС каждого типа) при расчётном значении МВПП
		Расчёт значения производится по формуле:
			МВКРИЛ = (МВПП - я.СПП)/ (Кпк * 365) ,
			где
				Кпк 	- Количество пассажирских кресел в самолётах ОАЭ I-III этапов
				МВПП	- Максимально возможное годовое значение пассажиропотока из аэропорта
		
		Тип: 			int
		'''
		return int((я.МВПП - я.СПП) / ((9 + 44 + 68) * 365))
	
	@property
	def Капн(я):
		'''
		Свойство возвращает коэффициент авиационной подвижности населения для данного аэропорта. Коэффициент определяется как средний (2.5) для узловых аэропортов (в терминологии Транспортной стратегии Российской Федерации) или максимальный (4.2) для аэродромов (аэропортов) обеспечения транспортной доступности, расположенных в удалённых и труднодоступных районах Российской Федерации, согласно Приложению № 7 к Распоряжению Правительства РФ от 27 ноября 2021 года № 3363-р
		'''
		try:
			f = pd.read_csv('../csv/Сводка.csv', index_col='ICAO')
			i = ConfigParser()
			i.read('../ini/МАЛ.ini', encoding='utf8')
			if я.Узловой: возврат = float(i['Коэффициенты авиационной подвижности населения']['Средний'])
			else: возврат = float(i['Коэффициенты авиационной подвижности населения']['Максимальный'])
		except:
			print('ОШИБКА! Проверить файлы Сводка.csv и МАЛ.ini')
			возврат = None
		finally: return возврат
	
	@property
	def РППМАКС(я):
		"""
		РППМАКС - максимальное значение расчётного пассажиропотока. Определяется как произведение агломерации населения на максимально возможный коэффициент авиационной подвижности населения (4.2 - для аэродромов удалённых и труднодоступных районов; 2.5 - для остальных аэродромов)
		"""
		возврат = 0
		if я.Узловой: возврат = я.Агломерация * 2.5
		else: возврат = я.Агломерация * 4.2 
		return int(возврат)
	
	@property
	def РСН(я):
		"""
		РСН - расчётный список направлений полётов
		Алгоритм определяет направления полётов из аэропорта с учётом 
		максимально возможного пассажиропотока из данного аэропорта.
		Алгоритм последовательно анализирует максимально возможный
		пассажиропоток.
		В случае, когда значение максимально возможного пассажиропотока
		менее минимального значения пассажиропотока, свойство возвращает
		единственное направление полётов в сторону узлового аэропорта.
		При значении МВПП от минимального до минимального для ТВРС-44
		возвращает перечень направлений в стороны узловых аэропортов
		В случае, когда аэропорт не является узловым в перечень включаются
		только направления в сторону узловых аэропортов. Для остальных
		случаев возвращается перечень всех доступных направлений полётов
		"""
		список = []
		if я.МВПП < int(ИД().РЧ['Пассажиропотоки']['минимальный']):
			for _ in sorted(я.Направления, key=attrgetter('дистанция')):
				if АЭРОДРОМ(_.куда).Узловой:
					список.append(_)
					return список
				else: ...
		elif int(ИД().РЧ['Пассажиропотоки']['минимальный']) <= я.МВПП <= int(ИД().РЧ['Пассажиропотоки']['минимальный для тврс-44']):
			for _ in sorted(я.Направления, key=attrgetter('дистанция')):
				if АЭРОДРОМ(_.куда).Узловой:
					список.append(_)
		elif я.Узловой: return я.Направления
		else:
			for _ in я.Направления:
				if АЭРОДРОМ(_.куда).Узловой:
					список.append(_)
			return я.список
		return список

	
	def __repr__(я):
		return я.ICAO + '|' + я.IATA + '|' + я.Название + '|' + я.Город

# ====================================================================

class САМОЛЁТ(Я):
	"""
	Класс С (САМОЛЁТ) обеспечивает хранение и применение свойств самолётов.
	При создании экземпляра класса необходимо вводить следующие возможные значения:
		- Ил-114-300
		- ТВРС-44
		- ЛМС-901
		- L410 UVP-E20
		- Ан-24
		- Ан-26
		- Ан-38
		- Як-40
		- EMB120ER
		- EMB135
		- EMB145
		- CRJ-100
		- CRJ-200
		- ATR-42
		- DASH-8
		- Ту-134
		- Ан-148-1
		- EMB170
		- DASH8-300
		- DASH8-400
		- ATR-72
		- SSJ-100
	"""
	
	def __repr__(я): return я.Тип
	
	@property
	def Тип(я):
		try:
			i = ConfigParser()
			i.read('../ini/МАЛ.ini', encoding='utf8')
			возврат = я.СЧ[0] if i['ЛТХ ' + я.СЧ[0]] else None
		except: 
			print('ОШИБКА! Проверить наличие данных по типу в файле МАЛ.ini')
			возврат = None
		finally: return возврат
	
	@property
	def КС(я):
		"""
		Крейсерская скорость в км/час
		Тип:	int
		"""
		try:
			i = ConfigParser()
			i.read('../ini/МАЛ.ini', encoding='utf8')
			возврат = int(i['ЛТХ ' + я.СЧ[0]]['Крейсерская скорость, км/ч'])
		except: 
			print('ОШИБКА! Проверить наличие данных по типу в файле МАЛ.ini')
			возврат = None
		finally: return возврат
	
	@property
	def МВМ(я):
		"""
		Максимальная взлётная масса в тоннах
		Тип:	float
		"""
		try:
			i = ConfigParser()
			i.read('../ini/МАЛ.ini', encoding='utf8')
			возврат = float(i['ЛТХ ' + я.СЧ[0]]['Максимальная взлётная масса, т'])
		except: 
			print('ОШИБКА! Проверить наличие данных по типу в файле МАЛ.ini')
			возврат = None
		finally: return возврат
		
	@property
	def СЧР(я):
		"""
		Средний часовой расход, кг/лч
		Тип:	float
		"""
		try:
			i = ConfigParser()
			i.read('../ini/МАЛ.ini', encoding='utf8')
			возврат = float(i['ЛТХ ' + я.СЧ[0]]['Расход ТС-1, кг/лётный час'])
		except: 
			print('ОШИБКА! Проверить наличие данных по типу в файле МАЛ.ini')
			возврат = None
		finally: return возврат
	
	@property
	def КПК(я):
		"""
		Количество пассажирских кресел пассажирского салона, шт
		Тип:	int
		"""
		try:
			i = ConfigParser()
			i.read('../ini/МАЛ.ini', encoding='utf8')
			возврат = int(i['ЛТХ ' + я.СЧ[0]]['Пассажиров, чел'])
		except: 
			print('ОШИБКА! Проверить наличие данных по типу в файле МАЛ.ini')
			возврат = None
		finally: return возврат
	
	@property
	def Ресурс(я):
		"""
		Полный ресурс самолёта, лч
		Тип:	timedelta
		"""
		try:
			i = ConfigParser()
			i.read('../ini/МАЛ.ini', encoding='utf8')
			возврат = timedelta(seconds = int(i['ЛТХ ' + я.СЧ[0]]['Полный ресурс, лч'])*3600)
		except: 
			print('ОШИБКА! Проверить наличие данных по типу в файле МАЛ.ini')
			возврат = None
		finally: return возврат
	
	@property
	def МРРП(я):
		"""
		Межремонтный ресурс планера, лч
		Тип:	timedelta
		"""
		try:
			i = ConfigParser()
			i.read('../ini/МАЛ.ini', encoding='utf8')
			возврат = timedelta(seconds = int(i['ЛТХ ' + я.СЧ[0]]['Межремонтный ресурс планера, лч'])*3600)
		except: 
			print('ОШИБКА! Проверить наличие данных по типу в файле МАЛ.ini')
			возврат = None
		finally: return возврат
	
	@property
	def МРРД(я):
		"""
		Межремонтный ресурс двигателей, лч
		Тип:	timedelta
		"""
		try:
			i = ConfigParser()
			i.read('../ini/МАЛ.ini', encoding='utf8')
			возврат = timedelta(seconds = int(i['ЛТХ ' + я.СЧ[0]]['Межремонтный ресурс двигателей, лч'])*3600)
		except: 
			print('ОШИБКА! Проверить наличие данных по типу в файле МАЛ.ini')
			возврат = None
		finally: return возврат

# ====================================================================

class МАРШРУТ(Я):
	"""
	Класс М (МАРШРУТ) обеспечивает хранение данных о маршрутах полётов
	"""
	@property
	def Расстояние(я):
		try:
			if len(я.СЧ[0]) == 3:
				#print('Код ИАТА аэропорта вылета получен')
				f = pd.read_csv('../csv/IATA.csv', index_col='iata')
				АПВ = f.loc[я.СЧ[0]]['icao']
			elif len(я.СЧ[0]) == 4: 
				#print('Код ИКАО аэропорта вылета получен')
				АПВ = я.СЧ[0]
			else: raise ValueError
			if len(я.СЧ[1]) == 3:
				f = pd.read_csv('../csv/IATA.csv', index_col='iata')
				АПП = f.loc[я.СЧ[1]]['icao']
				#print('Код ИАТА аэропорта прибытия получен')
			elif len(я.СЧ[1]) == 4: 
				АПП = я.СЧ[1]
				#print('Код ИАТА аэропорта вылета получен')
			else: raise ValueError
			f = pd.read_csv('../csv/FTD.csv', index_col='FT')
			#print(АПВ+АПП)
			возврат = f.loc[АПВ+АПП]['D']
			#print(возврат)
		except: 
			print('ОШИБКА! Проверить коды ИКАО (ИАТА)')
			возврат = None
		finally: return возврат
	
	@property
	def АПВ(я):
		"""
		АПВ - аэропорт вылета
		"""
		try:
			if len(я.СЧ[0]) == 3:
				#print('Код ИАТА аэропорта вылета получен')
				f = pd.read_csv('../csv/IATA.csv', index_col='iata')
				возврат = АЭРОДРОМ(f.loc[я.СЧ[0]]['icao'])
			elif len(я.СЧ[0]) == 4: 
				#print('Код ИКАО аэропорта вылета получен')
				возврат = АЭРОДРОМ(я.СЧ[0])
			else: raise ValueError
		except: 
			print('ОШИБКА! Проверить коды ИКАО (ИАТА)')
			возврат = None
		finally: return возврат
	
	@property
	def АПП(я):
		"""
		АПВ - аэропорт прибытия
		"""
		try:
			if len(я.СЧ[1]) == 3:
				#print('Код ИАТА аэропорта прибытия получен')
				f = pd.read_csv('../csv/IATA.csv', index_col='iata')
				возврат = АЭРОДРОМ(f.loc[я.СЧ[1]]['icao'])
			elif len(я.СЧ[1]) == 4: 
				#print('Код ИКАО аэропорта прибытия получен')
				возврат = АЭРОДРОМ(я.СЧ[1])
			else: raise ValueError
		except: 
			print('ОШИБКА! Проверить коды ИКАО (ИАТА)')
			возврат = None
		finally: return возврат

# ====================================================================

class РЕЙС(АЭРОДРОМ, САМОЛЁТ, МАРШРУТ):
	"""
	Класс Р (РЕЙС) обеспечивает хранение и применение данных о рейсе между аэродромами (аэропортами). Входные данные при создании экземпляра:
		- код ИКАО или ИАТА аэропорта вылета
		- код ИКАО или ИАТА аэропорта прибытия
		- тип воздушного судна
	"""
	
	def __repr__(я):
		возврат = "Сводные данные по рейсу\n\nАэропорт вылета:   "
		возврат += я.АПВ.ICAO + '|' + я.АПВ.IATA + '|' + я.АПВ.Город + '|' + я.АПВ.Название + '\n'
		возврат += "Аэропорт прибытия: " + я.АПП.ICAO + '|' + я.АПП.IATA + '|' + я.АПП.Город + '|' + я.АПП.Название + '\n'
		возврат += "Расчётный тип ВС:  " + я.ВС.Тип + '\n'
		возврат += "Дистанция:         " + str(я.ГРКТА) + ' км\n'
		возврат += "Продолжительность: " + str(я.ПП.час) + ":" + str(я.ПП.мин) + '\n'
		возврат += "Вылет:             " + str(я.Вылет) + '\n'
		возврат += "Прибытие:          " + str(я.Прибытие) + '\n'
		возврат += "Отправление:       " + str(я.Отправление) + '\n'
		возврат += "Себестоимость:     " + str(я.СР) + '\n'
			
		return возврат
	
	
	@property
	def Вылет(я):
		return я.РЧ.get('Вылет', datetime(year=2025, month=5, day=1, hour=0, minute=0))
	
	@property
	def Прибытие(я):
		возврат = я.Вылет + я.ПП.timedelta
		if (я.ПП.мин - (я.ПП.мин//10*10)) < 5: 
			возврат = я.Вылет + (я.ПП.timedelta + timedelta(seconds = (20 - (я.ПП.мин - я.ПП.мин//10*10))*60))
		else: 
			возврат = я.Вылет + (я.ПП.timedelta + timedelta(seconds = (25 - (я.ПП.мин - я.ПП.мин//10*10))*60))
		return возврат
	
	@property
	def Обслуживание(я):
		return я.РЧ.get('Обслуживание', timedelta(seconds=int(ИД().РЧ['Интервалы']['время обслуживания в аэропорте транзита, мин'])*60))
	
	@property
	def Отправление(я):
		"""
		Отправление - дата и время отправления после обслуживания в аэропорте транзита
		"""
		return я.Прибытие + я.Обслуживание
		
	@property
	def АПВ(я):
		"""
		АПВ - аэропорт вылета
		"""
		try:
			возврат = АЭРОДРОМ(я.СЧ[0])
		except:
			print('ОШИБКА! Проверить данные аэропорта вылета')
			возврат = None
		finally: return возврат
	
	@property
	def АПП(я):
		"""
		АПП - аэропорт прибытия
		"""
		try:
			возврат = АЭРОДРОМ(я.СЧ[1])
		except:
			print('ОШИБКА! Проверить данные аэропорта прибытия')
			возврат = None
		finally: return возврат
	
	@property
	def ВС(я):
		"""
		ВС - тип воздушного судна для выполнения рейса
		"""
		try:
			возврат = САМОЛЁТ(я.СЧ[2])
		except:
			print('ОШИБКА! Проверить тип ВС')
			возврат = None
		finally: return возврат
	
	@property
	def ГРКТА(я):
		"""
		ГРКТА - геодезическое расстояние между контрольными точками аэродромов
		"""
		try:
			if len(я.СЧ[0]) == 3:
				#print('Код ИАТА аэропорта вылета получен')
				f = pd.read_csv('../csv/IATA.csv', index_col='iata')
				АПВ = f.loc[я.СЧ[0]]['icao']
			elif len(я.СЧ[0]) == 4: 
				#print('Код ИКАО аэропорта вылета получен')
				АПВ = я.СЧ[0]
			else: raise ValueError
			if len(я.СЧ[1]) == 3:
				f = pd.read_csv('../csv/IATA.csv', index_col='iata')
				АПП = f.loc[я.СЧ[1]]['icao']
				#print('Код ИАТА аэропорта прибытия получен')
			elif len(я.СЧ[1]) == 4: 
				АПП = я.СЧ[1]
				#print('Код ИАТА аэропорта вылета получен')
			else: raise ValueError
			f = pd.read_csv('../csv/FTD.csv', index_col='FT')
			#print(АПВ+АПП)
			возврат = f.loc[АПВ+АПП]['D']
			#print(возврат)
		except: 
			print('ОШИБКА! Проверить коды ИКАО (ИАТА)')
			возврат = None
		finally: return возврат
	
	@property
	def ТС(я):
		"""
		ТС - техническая скорость расчётного типа ВС в км/час
		"""
		try:
			возврат = (я.ГРКТА * я.ВС.КС)/(я.ГРКТА + (я.DT * я.ВС.КС))
		except:
			print('ОШИБКА! Проверить данные ВС')
			возврат = None
		finally: return возврат
		
	@property
	def DT(я):
		"""
		DT - эмпирический коэффициент, учитывающий потери времени при маневрировании в районе аэропортов
		"""
		xp = [3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]
		fp = [0.165, 0.17, 0.177, 0.19, 0.22, 0.25, 0.3, 0.355, 0.435]
		xp1 = [100, 400]
		fp1 = [3000, 7000]
		if я.ГРКТА < 100:
			возврат = fp[0]
		elif (100 <= я.ГРКТА <= 400) and (я.ВС != 'ЛМС-901'):
			возврат = np.interp(я.ГРКТА, xp1, fp1)
			возврат = np.interp(возврат, xp, fp)
		elif (400 < я.ГРКТА) and (я.ВС != 'ЛМС-901'):
			возврат = fp[4]
		else:
			возврат = fp[0]
		return возврат
	
	@property
	def ПП(я):
		"""
		ПП - продолжительность беспосадочного полёта
		"""
		td = timedelta(seconds = (я.ГРКТА/я.ТС)*3600)
		return ВРЕМЯ(td, td.seconds//3600, (td.seconds//60)%60)
	
	@property
	def МТР(я):
		"""
		МТР - масса авиатоплива для выполнения рейса, кг
		"""
		return (я.ПП.timedelta.seconds/3600)*я.ВС.СЧР
	
	@property
	def СРСС(я):
		"""
		СРСС - себестоимость рейса через структуру себестоимости
		"""
		СС = ИД()
		АвиаГСМ = float(СС.РЧ['Структура себестоимости рейса']['авиагсм, %'])
		Амортизация = float(СС.РЧ['Структура себестоимости рейса']['амортизация, %'])
		Аэропортовое = float(СС.РЧ['Структура себестоимости рейса']['аэропортовое обслуживание, %'])
		ТОиР = float(СС.РЧ['Структура себестоимости рейса']['тоир свад, %'])
		АЭНО = float(СС.РЧ['Структура себестоимости рейса']['аэно, %'])
		Метео = float(СС.РЧ['Структура себестоимости рейса']['метео, %'])
		Агентские = float(СС.РЧ['Структура себестоимости рейса']['агентские отчисления, %'])
		Аренда = float(СС.РЧ['Структура себестоимости рейса']['аренда, %'])
		Страхование = float(СС.РЧ['Структура себестоимости рейса']['страхование, %'])
		Прочие = float(СС.РЧ['Структура себестоимости рейса']['прочие, %'])
		Общепроизводственные = float(СС.РЧ['Структура себестоимости рейса']['общепроизводственные, %'])
		ФОТ = float(СС.РЧ['Структура себестоимости рейса']['фот, %'])
		Начисления = float(СС.РЧ['Структура себестоимости рейса']['начисления, %'])
		
		возврат = None
		
		ССТС1 = int(ИД().РЧ['Исходные данные']['средняя стоимость авиагсм, руб/т'])/1000
		возврат = ССР(
			round(я.МТР*ССТС1, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*Амортизация, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*Аэропортовое, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*ТОиР, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*АЭНО, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*Метео, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*Агентские, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*Аренда, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*Страхование, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*Прочие, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*Общепроизводственные, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*ФОТ, 2),
			round((я.МТР*ССТС1/АвиаГСМ)*Начисления, 2))
		return возврат
	
	@property
	def СР(я):
		"""
		СР - себестоимость рейса
		"""
		return  round(я.СРСС.АвиаГСМ + я.СРСС.Амортизация + я.СРСС.Аэропортовое + я.СРСС.ТОиР + я.СРСС.АЭНО + я.СРСС.Метео + я.СРСС.Агентские + я.СРСС.Аренда + я.СРСС.Страхование + я.СРСС.Прочие + я.СРСС.Общепроизводственные + я.СРСС.ФОТ + я.СРСС.Начисления, 2)
	
class ПРОЕКТ(Я):
	def __init__(я, *СЧ, **РЧ):
		РЧ['вариант'] = РЧ.get('вариант', "Центр 51")
		try:
			with open('../json/МАЛ.json', 'r') as f:
				d = json.load(f)
			РЧ['ЮВК'] = [ АЭРОДРОМ(_) for _ in d['вариант'][РЧ['вариант']]['ЮВК']]
			РЧ['СВК'] = [ АЭРОДРОМ(_) for _ in d['вариант'][РЧ['вариант']]['СВК']]
			РЧ['ЦВК'] = [ АЭРОДРОМ(_) for _ in d['вариант'][РЧ['вариант']]['ЦВК']]
		except:
			print('[ОШИБКА] Проверить файл МАЛ.json')
		finally: ...
		super().__init__(*СЧ, **РЧ)
	
	@property
	def ЮВК(я):
		"""Возвращает опорные аэродромы ЮВК"""
		return я.РЧ.get('ЮВК', [])
	
	@property
	def СВК(я):
		"""Возвращает опорные аэродромы СВК"""
		return я.РЧ.get('СВК', [])
	
	@property
	def ЦВК(я):
		"""Возвращает опорные аэродромы СВК"""
		return я.РЧ.get('ЦВК', [])
