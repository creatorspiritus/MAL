import streamlit as st
from функции import *
from классы import *
from перечни import *


if "радиус_зоны_ответственности" not in st.session_state:
    st.session_state["радиус_зоны_ответственности"] = 1000

if "радиус_зоны_агломерации" not in st.session_state:
    st.session_state["радиус_зоны_агломерации"] = 100

if "аэродром" not in st.session_state:
    st.session_state["аэродром"] = "UNWW | NOZ | Новокузнецк | Спиченково"

if "аэропорты" not in st.session_state:
    st.session_state["аэропорты"] = перечень_МАЛ

if "самолёты" not in st.session_state:
    st.session_state["самолёты"] = [_['тип'] for _ in перечень_самолёты]

if 'самолёты_проекта' not in st.session_state:
    st.session_state['самолёты_проекта'] = [
        "Ил-114-300",
        "ТВРС-44 Ладога",
        "ЛМС-192 Освей",
        "ЛМС-901 Байкал"
    ]

if 'опорные_аэродромы_ЮВК' not in st.session_state:
    st.session_state['самолёты_проекта'] = [
        "Ил-114-300",
        "ТВРС-44 Ладога",
        "ЛМС-192 Освей",
        "ЛМС-901 Байкал"
    ]

if 'капн_макс' not in st.session_state:
    st.session_state['капн_макс'] = 4.2

if 'капн_мин' not in st.session_state:
    st.session_state['капн_мин'] = 2.5

if 'ЮВК' not in st.session_state:
    st.session_state['ЮВК'] = [
        "UNWW | NOZ | Новокузнецк | Спиченково",
        "UNKY | KYZ | Кызыл",
        "UNOO | OMS | Омск Центральный",
        "UIUU | UUD | Улан-Удэ | Байкал",
        "USCC | CEK | Челябинск | Баландино",
        "UIAA | HTA | Чита | Кадала",
        "UWOR | OSW | Орск",
        "UHBW | TYD | Тында | Тында",
        "URWA | ASF | Астрахань",
        "UHBB | BQS | Благовещенск | Игнатьево",
        "ZFC7 | Сухум | Бабушара",
        "UHWW | VVO | Владивосток | Кневичи"
    ]

if 'СВК' not in st.session_state:
    st.session_state['СВК'] = [
        "UUOB | EGO | Белгород",
        "ULOO | PKV | Псков | Кресты",
        "ULAA | ARH | Архангельск | Талаги",
        "ULAM | NNM | Нарьян-Мар",
        "UUYW | VKT | Воркута",
        "USMU | NUX | Новый Уренгой",
        "UOOO | NSK | Норильск | Алыкель",
        "UOHH | HTG | Хатанга",
        "UEST | IKS | Тикси",
        "UESO | CKH | Чокурдах",
        "UESS | CYX | Черский",
        "UHMA | DYR | Анадырь | Угольный"
    ]

if 'ЦВК' not in st.session_state:
    st.session_state['ЦВК'] = [
        "UHPD | Оссора",
        "UHMM | GDX | Магадан | Сокол",
        "UEEE | YKS | Якутск",
        "UERR | MJZ | Мирный",
        "UIBB | BTK | Братск",
        "UNIP | TGP | Подкаменная Тунгуска",
        "USRR | SGC | Сургут",
        "USSS | SVX | Екатеринбург | Кольцово",
        "USKK | KVX | Киров | Победилово",
        "ULWW | VGD | Вологда",
        "UUBC | KLF | Калуга | Грабцево",
        "UUOL | LPK | Липецк"
    ]

if 'цена_через_зарплату' not in st.session_state:
    st.session_state['цена_через_зарплату'] = 0.1

if 'цена_через_доход' not in st.session_state:
    st.session_state['цена_через_доход'] = 0.1

if 'загрузка_рейса' not in st.session_state:
    st.session_state['загрузка_рейса'] = 0.7

if 'доход_билет' not in st.session_state:
    st.session_state['доход_билет'] = 3000

if 'доход_груз' not in st.session_state:
    st.session_state['доход_груз'] = 50

if 'доход_почта' not in st.session_state:
    st.session_state['доход_почта'] = 50

st.title("Общая информация о проекте МАЛ")
st.divider()

with st.sidebar.expander('Радиусы'):
    st.session_state["радиус_зоны_агломерации"] = st.number_input(
        "Радиус агломерации, км",
        min_value=100, max_value=100,
        value=st.session_state["радиус_зоны_агломерации"],
        help="Значение определяет радиус круга с центром в контрольной точке аэродрома, который ограничивает количество населённых пунктов, население которых учитывается при подсчёте количества жителей, проживающих в районе аэропорта") 
    st.session_state["радиус_зоны_ответственности"] = st.number_input(
        "Радиус доступности, км",
        min_value=1000, max_value=1000,
        value=int(st.session_state["радиус_зоны_ответственности"]))
    
with st.sidebar.expander('Цены'):
    цена_через_зарплату = st.number_input(
        "Стоимость авиабилета, руб",
        value=st.session_state['доход_билет'],
        help="Указывается средняя сумма, полученная авиапредприятием с одного пассажира за рейс. Сумма используется для предварительных расчётов доходности рейса"
    )
    цена_груз = st.number_input(
        "Стоимость перевозки груза, руб/кг",
        value=st.session_state['доход_груз'],
        help="Указывается средняя сумма, полученная авиапредприятием за перевозку одного килограмма груза за рейс. Сумма используется для предварительных расчётов доходности рейса"
    )
    цена_почта = st.number_input(
        "Стоимость перевозки почты, руб/кг",
        value=st.session_state['доход_почта'],
        help="Указывается средняя сумма, полученная авиапредприятием за перевозку одного почтовых отправлений за рейс. Сумма используется для предварительных расчётов доходности рейса"
    )
    АвиаГСМсреднее = st.number_input(
        "Стоимость ТС-1, руб. без НДС",
        value=Керосин_сегодня(аэропорт=st.session_state["аэродром"][:4]),
        min_value=1, max_value=1000000, step=1,
        help="Указывается расчётное значение стоимости авиационного керосина ТС-1 в рублях без НДС при заправке самолёта на перроне из топливозаправщика"
        )
    
with st.sidebar.expander('Коэффициенты'):
    st.session_state['капн_мин'] = st.number_input(
        "Коэффициент авиационной подвижности населения для узловых аэропортов",
        value=st.session_state['капн_мин'],
        min_value=1.0, max_value=2.5, step=0.1,
        help="Указывается минимальное значение коэффициента авиационной подвижности населения, используемое для расчётов вероятных пассажиропотоков из узловых аэропортов"
        )
    st.session_state['капн_макс'] = st.number_input(
        "Коэффициент авиационной подвижности населения для аэропортов назначения",
        value=st.session_state['капн_макс'],
        min_value=2.6, max_value=4.6, step=0.1,
        help="Указывается минимальное значение коэффициента авиационной подвижности населения, используемое для расчётов вероятных пассажиропотоков из аэропортов назначения в направлении узловых аэропортов",
        )
    st.session_state['цена_через_зарплату'] = st.number_input(
        "Зарплатный коэффициент",
        value=st.session_state['цена_через_зарплату'],
        min_value=0.01, max_value=0.3, step=0.01,
        help="Коэффициент, применяемый для автоматизированного расчёта стоимости авиабилета через процент от среднемесячной стоимости заработной платы по региону аэропорта вылета. Указываются сотые доли (проценты, разделённые на 100) от среднемесячной заработной платы рабочих и служащих, расчитанной или полученной из объективных источников информации",
        )
    st.session_state['цена_через_доход'] = st.number_input(
        "Доходный коэффициент",
        value=st.session_state['цена_через_доход'],
        min_value=0.01, max_value=0.3, step=0.01,
        help="Коэффициент, применяемый для автоматизированного расчёта стоимости авиабилета через процент от среднемесячного дохода жителей в регионе аэропорта вылета. Указываются сотые доли (проценты, разделённые на 100) от среднемесячного дохода каждого жителя, расчитанного или полученного из объективных источников информации",
        )
    st.session_state['загрузка_рейса'] = st.number_input(
        "Загрузка рейса",
        value=st.session_state['загрузка_рейса'],
        min_value=0.01, max_value=1.0, step=0.01,
        help="Коэффициент, применяемый для расчёта себестоимости рейса. Указываются сотые доли (проценты, разделённые на 100) от полной загрузка самолёта"
        )
    
