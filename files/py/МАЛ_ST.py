import streamlit as st
from pandas import read_csv
from collections import namedtuple

разделитель = lambda x: " | " + x if x else ''

@st.cache_data
def Сводка():
    return read_csv('../csv/Сводка.csv', index_col='ICAO')

сводка = Сводка()

@st.cache_data
def IATA():
    return read_csv('../csv/iata.csv', index_col='icao')

iata = IATA()

@st.cache_data
def Агломерация():
    return read_csv('../csv/Агломерация.csv', index_col='ICAO')

агломерация = Агломерация()

@st.cache_data
def Маршруты():
    return read_csv('../csv/ftd.csv', index_col='FT')

маршруты = Маршруты()

ЮВК = сводка[сводка.ВК == 1]
СВК = сводка[сводка.ВК == 2]
ЦВК = сводка[сводка.ВК == 3]

ЮВК_наименования = [_ + разделитель(iata.loc[_]['iata'])]

###
### Боковая панель исходных данных
###

st.sidebar.header('Исходные данные', divider= True)
ИД_ЮВК = [
    "NOZ | UNWW | Новокузнецк",
    "OMS | UNOO | Омск",
    "OMS | UNOO | Омск"]
ИД_ЮВК_17 = [
    "NOZ | UNWW | Новокузнецк",
    "OMS | UNOO | Омск",
    "OMS | UNOO | Омск"]
ИД_СВК = [
    "NOZ | UNWW | Новокузнецк",
    "OMS | UNOO | Омск",
    "OMS | UNOO | Омск"]
ИД_СВК_17 = [
    "NOZ | UNWW | Новокузнецк",
    "OMS | UNOO | Омск",
    "OMS | UNOO | Омск"]
ИД_ЦВК = [
    "NOZ | UNWW | Новокузнецк",
    "OMS | UNOO | Омск",
    "OMS | UNOO | Омск"]
ИД_ЦВК_17 = [
    "NOZ | UNWW | Новокузнецк",
    "OMS | UNOO | Омск",
    "OMS | UNOO | Омск"]
ЮВК = st.sidebar.multiselect(
    "Южный воздушный коридор",
    ИД_ЮВК, 
    default=ИД_ЮВК_17,
    max_selections=17)
# st.sidebar.divider()
СВК = st.sidebar.multiselect(
    "Северный воздушный коридор",
    ИД_СВК,
    default=ИД_СВК_17,
    max_selections=17)
# st.sidebar.divider()
ЦВК = st.sidebar.multiselect(
    "Центральный воздушный коридор",
    ИД_ЦВК,
    default=ИД_ЦВК_17,
    max_selections=17,
    )
st.sidebar.divider()




# Расчётные типы воздушных судов
РТВС_ИД = [
    "Ил-114-300",
    "ТВРС-44 Ладога",
    "ЛМС-901 Байкал"
]
РТВС = st.sidebar.multiselect(
    "Расчётные типы воздушных судов",
    РТВС_ИД,
    default=РТВС_ИД,
    max_selections=5,
    )


st.sidebar.header('Расчётные показатели', divider= True)


# Количество самолётов одного типа на опорном аэродроме
КСОТ = st.sidebar.number_input(
    "Количество самолётов одного типа на опорном аэродроме, штук в авиационном звене",
    min_value=0,
    max_value=9,
    value=3,
    help="Указывается количество самолётов одного типа в целочисленных значениях")
st.sidebar.divider()




# Расчётный радиус агломерации населения
РРАН = st.sidebar.number_input(
    "Расчётный радиус агломерации населения в районе аэродрома, км",
    min_value=10,
    max_value=200,
    value=100,
    help="Указывается значение радиуса условной окружности с центром в контрольной точке аэродрома, в километрах")
st.sidebar.divider()



# Расчётная минимальная длина ВПП
РМИНДВПП = st.sidebar.number_input(
    "Расчётная минимальная длина ВПП опорного аэродрома, м",
    min_value=500,
    max_value=5000,
    value=1400,
    help="Указывается минимальное допустимое значение длины взлётно-посадочной полосы для безопасной эксплуатации всех расчётных типов воздушных судов, в метрах")
# st.sidebar.divider()




# Расчётная минимальная ширина ВПП
РМИНШВПП = st.sidebar.number_input(
    "Расчётная минимальная ширина ВПП опорного аэродрома, м",
    min_value=20,
    max_value=60,
    value=30,
    help="Указывается минимальное допустимое значение ширины взлётно-посадочной полосы для безопасной эксплуатации всех расчётных типов воздушных судов, в метрах")
st.sidebar.divider()



# Курс юаня
юань = st.sidebar.number_input(
    "Курс юаня, руб",
    min_value=1,
    max_value=300,
    value=13,
    help="Указывается стоимость юаня КНР в рублях по курсу ЦБ РФ")
# st.sidebar.divider()




# Курс доллара США
доллар = st.sidebar.number_input(
    "Курс доллара США, руб",
    min_value=1,
    max_value=300,
    value=93,
    help="Указывается стоимость доллара США в рублях по курсу ЦБ РФ")
# st.sidebar.divider()




# Курс евро
евро = st.sidebar.number_input(
    "Курс евро, руб",
    min_value=1,
    max_value=300,
    value=100,
    help="Указывается стоимость евро в рублях по курсу ЦБ РФ")
st.sidebar.divider()





st.header('МУНИЦИПАЛЬНЫЕ АВИАЛИНИИ')
st.caption('Проект развития региональных воздушных перевозок с применениеме самолётов российского производства')

try:
    df = read_csv('../csv/aopa-points-export.csv', sep=';', index_col='Индекс')
except:
    # Получение данных из указанного файла
    aopa = st.sidebar.file_uploader('Загрузить данные аэродромов')
    df = read_csv(aopa, sep=';', index_col='Индекс')
finally:
    st.write("Всего ", str(len(df)), " записи в базе данных")
    st.write("из них")
    # st.sidebar.write("Аэродромов: ", len(df[df["Тип"] == "Аэродром"]))
    col1, col2 = st.columns([4,1])
    col1.write('Аэродромов, всего')
    col2.write(str(len(df[df["Тип"] == "Аэродром"])))
    col1.write('- действующих')
    col2.write(len(df[(df["Тип"] == "Аэродром") & (df["Действующий"] == "Действующий")]))
    col1.write('Вертодромов, всего')
    col2.write(str(len(df[df["Тип"] == "Вертодром"])))
    col1.write('- действующих')
    col2.write(len(df[(df["Тип"] == "Вертодром") & (df["Действующий"] == "Действующий")]))
    




# with st.spinner(text='Загрузка данных...'):
#     st.success('Выполнено', icon="✅")









# st.write(df)

# st.download_button(
#     label="Download data as CSV",
#     data=csv,
#     file_name='large_df.csv',
#     mime='text/csv',
#     )