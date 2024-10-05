import streamlit as st
st.logo("./files/png/МАЛ Логотип и название.png", link="https://мал.орг/ru", icon_image="./files/png/МАЛ Логотип без аббревиатуры.png")
st.set_page_config(
    "МАЛ", page_icon="🛩️", layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://xn--80awb.xn--c1avg/ru',
        'Report a bug': "https://xn--80awb.xn--c1avg/ru",
        'About': """### МУНИЦИПАЛЬНЫЕ АВИАЛИНИИ
Проект развития региональных воздушных перевозок с применением самолётов российского производства.

Расчётные типы воздушных судов:
- Ил-114-300
- ТВРС-44 Ладога
- ЛМС-192 Освей
- ЛМС-901 Байкал"""
        }
)


#st.session_state={
#    "РТВС": ["Ил-114-300", "ТВРС-44 Ладога", "ЛМС-192 Освей", "ЛМС-901 Байкал"], # РТВС - расчётные типы воздушных судов проекта
#    "ЮВК": [
#        "UNAA | ABA | Абакан",
#        "URKA | AAQ | Анапа | Витязево",
#        "URWA | ASF | Астрахань",
#        "UNBB | BAX | Барнаул | Имени Германа Титова",
#        "UHBB | BQS | Благовещенск | Игнатьево",
#        "UHWW | VVO | Владивосток | Кневичи",
#        "URMO | OGZ | Владикавказ | Беслан",
#        "URWW | VOG | Волгоград | Гумрак",
#        "URKG | GDZ | Геленджик",
#        "UNBG | RGK | Горно-Алтайск",
#        "URMG | GRV | Грозный | Северный",
#        "UNEE | KEJ | Кемерово | Имени Алексея Леонова",
#        "URKK | KRR | Краснодар | Пашковский",
#        "USUU | KRO | Курган",
#        "UUOK | URS | Курск | Восточный",
#        "UNKY | KYZ | Кызыл",
#        "URMS | IGT | Магас",
#        "USCM | MQF | Магнитогорск",
#        "URML | MCX | Махачкала | Уйташ",
#        "URMM | MRV | Минеральные Воды",
#        "URMN | NAL | Нальчик",
#        "UNWW | NOZ | Новокузнецк | Спиченково",
#        "UNNT | OVB | Новосибирск | Толмачёво",
#        "UNOO | OMS | Омск Центральный",
#        "UWOO | REN | Оренбург",
#        "UWOR | OSW | Орск",
#        "URRP | ROV | Ростов-на-Дону | Платов",
#        "UWWW | KUF | Самара | Курумоч",
#        "UWSG | Саратов | Гагарин",
#        "URFB | Севастополь | Бельбек",
#        "URFF | Симферополь",
#        "URSS | AER | Сочи",
#        "URMT | STW | Ставрополь | Шпаковское",
#        "UHBW | TYD | Тында | Тында",
#        "UIUU | UUD | Улан-Удэ | Байкал",
#        "UHHH | KHV | Хабаровск | Новый",
#        "USCC | CEK | Челябинск | Баландино",
#        "UIAA | HTA | Чита | Кадала",
#        "ZFC7 | Сухум | Бабушара",
#        "UKCC | DOK | Донецк | Донецк",
#        "UKCW | VSG | Луганск | Луганск",
#        "UKDE | OZH | Запорожье | Мокрая",
#        "UKOH | KHE | Херсон | Чернобаевка",
#        "UKCM | MPW | Мариуполь",
#    ],
#    "СВК": [
#        "ULDD | AMV | Амдерма",
#        "UHMA | DYR | Анадырь | Угольный",
#        "ULMK | KVK | Апатиты | Хибины",
#        "ULAA | ARH | Архангельск | Талаги",
#        "UESG | BGN | Белая Гора",
#        "UUOB | EGO | Белгород",
#        "UHMR | Беринговский",
#        "USDB | BVJ | Бованенково",
#        "ULDW | VRI | Варандей",
#        "ULLK | Великий Новгород | Кречевицы",
#        "UUYW | VKT | Воркута",
#        "UEBD | Депутатский",
#        "UODD | DKS | Диксон",
#        "UHME | Залив Креста",
#        "UHML | Залив Лаврентия",
#        "UOII | IAA | Игарка",
#        "UMKK | KGD | Калининград | Храброво",
#        "UHMK | KPW | Кепервеем",
#        "ULMM | MMK | Мурманск",
#        "USMM | NYM | Надым",
#        "ULAM | NNM | Нарьян-Мар",
#        "USMU | NUX | Новый Уренгой",
#        "UOOO | NSK | Норильск | Алыкель",
#        "UHMP | PWE | Певек",
#        "ULPB | PES | Петрозаводск | Бесовец",
#        "UERP | PYJ | Полярный",
#        "UHMD | PVS | Бухта Провидения",
#        "ULOO | PKV | Псков | Кресты",
#        "USDA | SBT | Сабетта",
#        "USDD | SLY | Салехард",
#        "ULLI | LED | Санкт-Петербург | Пулково",
#        "UERS | SYS | Саскылах",
#        "ULAS | CSH | Соловки",
#        "UESK | SEK | Среднеколымск",
#        "UUYY | SCW | Сыктывкар",
#        "UEST | IKS | Тикси",
#        "UUYS | USK | Усинск",
#        "UEBT | UKG | Усть-Куйга",
#        "USDM | Утренний",
#        "UOHH | HTG | Хатанга",
#        "UESS | CYX | Черский",
#        "UESO | CKH | Чокурдах",
#        "USMQ | Ямбург",
#        "UHMM | GDX | Магадан | Сокол",
#        "UEEE | YKS | Якутск",
#    ],
#    "ЦВК": [
#        "UHPK | Усть-Камчатск",
#        "UHPP | PKC | Петропавловск-Камчатский | Елизово",
#        "UERA | Айхал",
#        "UEEA | ADH | Алдан",
#        "UHNA | Аян | Мунук",
#        "UNIB | Байкит",
#        "UWSB | BWO | Балаково | Малая Быковка",
#        "UEBB | Батагай",
#        "UHNB | BQG | Богородское",
#        "UIKB | ODO | Бодайбо",
#        "UHHG | Бомнак",
#        "UIBB | BTK | Братск",
#        "UUBP | BZK | Брянск",
#        "UNIW | Ванавара",
#        "UENI | VHV | Верхневилюйск",
#        "UENW | VYI | Вилюйск",
#        "ULWW | VGD | Вологда",
#        "UUOO | VOZ | Воронеж | Чертовицкое",
#        "USSS | SVX | Екатеринбург | Кольцово",
#        "UNII | EIE | Енисейск",
#        "UIKE | ERG | Ербогачен",
#        "UEVV | ZIX | Жиганск",
#        "UUBW | ZIA | Раменское | Жуковский",
#        "UHBE | Зея | Зея",
#        "UESU | ZKP | Зырянка",
#        "UUBI | IWA | Иваново | Южный",
#        "USII | IJK | Ижевск",
#        "UIII | IKT | Иркутск",
#        "UWKJ | JOK | Йошкар-Ола",
#        "UWKD | KZN | Казань",
#        "UUBC | KLF | Калуга | Грабцево",
#        "UHPZ | Каменское",
#        "UIKK | KCK | Киренск",
#        "USKK | KVX | Киров | Победилово",
#        "USRK | KGP | Когалым",
#        "UNKI | Кодинск",
#        "UHKK | KXK | Комсомольск-на-Амуре | Хурба",
#        "UUBA | KMW | Кострома | Сокеркино",
#        "UNKL | KJA | Красноярск | Емельяново",
#        "UERL | ULK | Ленск | Ленск",
#        "UUOL | LPK | Липецк",
#        "UEMM | GYG | Маган",
#        "UHPN | Манилы",
#        "UHMO | KVM | Марково | Марково",
#        "UHPM | Мильково",
#        "UERR | MJZ | Мирный",
#        "UEMA | MQJ | Мома",
#        "UUWW | VKO | Москва | Внуково",
#        "UUDD | DME | Москва | Домодедово",
#        "UUEE | SVO | Москва | Шереметьево",
#        "UNIM | Мотыгино",
#        "UELL | NER | Нерюнгри | Чульман",
#        "UIUN | Нижнеангарск",
#        "USNN | NJC | Нижневартовск | Нижневартовск",
#        "UWKE | NBC | Нижнекамск | Бегишево",
#        "UWGG | GOJ | Нижний Новгород | Стригино",
#        "UHNN | NLI | Николаевск-на-Амуре",
#        "UHPX | Никольское",
#        "UHSN | NGK | Ноглики",
#        "USRO | NOJ | Ноябрьск",
#        "UENN | NYR | Нюрба",
#        "UHQO | Запорожье | Озерная",
#        "UEMO | OLZ | Олёкминск",
#        "UERO | ONK | Оленек",
#        "UHMN | Омолон",
#        "UHMF | Омсукчан",
#        "UHPD | Оссора",
#        "UHSH | OHH | Оха | Новостройка",
#        "UHOO | OHO | Охотск",
#        "UHPL | Палана",
#        "ZD5W | Парамушир",
#        "UHPA | Пахачи",
#        "UWPP | PEZ | Пенза",
#        "USPP | PEE | Пермь | Большое Савино",
#        "UNIP | TGP | Подкаменная Тунгуска",
#        "UNSS | SWT | Стрежевой",
#        "UEBS | SUK | Саккырыр",
#        "UEMS | Сангар",
#        "UWPS | SKX | Саранск",
#        "UNIS | Северо-Енисейск",
#        "UHMW | SWV | Северо-Эвенск",
#        "UHMS | Сеймчан",
#        "UHPS | Соболево | Соболево",
#        "UENS | SUY | Сунтар",
#        "USRR | SGC | Сургут",
#        "UIKG | Таксимо",
#        "UECT | TLK | Талакан",
#        "UUOT | TBW | Тамбов | Донское",
#        "USDS | TQL | Тарко-Сале",
#        "UHPG | Тигиль",
#        "UHPT | Тиличики",
#        "USDO | Толька",
#        "UNTT | TOF | Томск | Богашёво",
#        "UNIT | Тура-Горный",
#        "UOTT | THX | Туруханск | Туруханск",
#        "USTR | TJM | Тюмень | Рощино",
#        "UWLL | ULV | Ульяновск | Баратаевка",
#        "UITT | UKX | Усть-Кут | Усть-Кут",
#        "UEMU | UMS | Усть-Мая",
#        "UEMT | USR | Усть-Нера",
#        "UHPU | Усть-Хайрюзово",
#        "UWUU | UFA | Уфа",
#        "UEMH | KDY | Хандыга | Теплый Ключ",
#        "USHH | HMA | Ханты-Мансийск",
#        "UHNH | Херпучи",
#        "UIAR | Чара",
#        "UWKS | CSY | Чебоксары",
#        "ULWC | CEE | Череповец",
#        "UHHY | Чумикан",
#        "UHSK | EKS | Шахтерск",
#        "HC3Y | Малокурильское",
#        "UHBP | Экимчан | Экимчан",
#        "URWI | ESL | Элиста",
#        "UHSM | DEE | Южно-Курильск | Менделеево",
#        "UHSS | UUS | Южно-Сахалинск | Хомутово",
#        "UUDL | IAR | Ярославль | Туношна",
#        "UHSI | ITU | Итуруп",
#    ],
#    "ЮВК_36": [
#        "URWA | ASF | Астрахань",
#        "UHBB | BQS | Благовещенск | Игнатьево",
#        "URMO | OGZ | Владикавказ | Беслан",
#        "UNKY | KYZ | Кызыл",
#        "UNWW | NOZ | Новокузнецк | Спиченково",
#        "UNOO | OMS | Омск Центральный",
#        "UWOR | OSW | Орск",
#        "UHBW | TYD | Тында | Тында",
#        "UIUU | UUD | Улан-Удэ | Байкал",
#        "UHHH | KHV | Хабаровск | Новый",
#        "UIAA | HTA | Чита | Кадала",
#        "ZFC7 | Сухум | Бабушара",
#    ],
#    "СВК_36": [
#        "UUOB | EGO | Белгород",
#        "ULAA | ARH | Архангельск | Талаги",
#        "UUYW | VKT | Воркута",
#        "ULAM | NNM | Нарьян-Мар",
#        "USMU | NUX | Новый Уренгой",
#        "UOOO | NSK | Норильск | Алыкель",
#        "UERP | PYJ | Полярный",
#        "ULOO | PKV | Псков | Кресты",
#        "UEST | IKS | Тикси",
#        "UOHH | HTG | Хатанга",
#        "UEEE | YKS | Якутск",
#        "UHMM | GDX | Магадан | Сокол",
#    ],
#    "ЦВК_36": [
#        "UHPP | PKC | Петропавловск-Камчатский | Елизово",
#        "UHPK | Усть-Камчатск",
#        "UHSH | OHH | Оха | Новостройка",
#        "UELL | NER | Нерюнгри | Чульман",
#        "UERR | MJZ | Мирный",
#        "UIBB | BTK | Братск",
#        "UNIP | TGP | Подкаменная Тунгуска",
#        "UNSS | SWT | Стрежевой",
#        "USHH | HMA | Ханты-Мансийск",
#        "UUYY | SCW | Сыктывкар",
#        "UUWW | VKO | Москва | Внуково",
#        "UUDL | IAR | Ярославль | Туношна",
#    ]
#}

#



ЮВК = [
        "UNAA | ABA | Абакан",
        "URKA | AAQ | Анапа | Витязево",
        "URWA | ASF | Астрахань",
        "UNBB | BAX | Барнаул | Имени Германа Титова",
        "UHBB | BQS | Благовещенск | Игнатьево",
        "UHWW | VVO | Владивосток | Кневичи",
        "URMO | OGZ | Владикавказ | Беслан",
        "URWW | VOG | Волгоград | Гумрак",
        "URKG | GDZ | Геленджик",
        "UNBG | RGK | Горно-Алтайск",
        "URMG | GRV | Грозный | Северный",
        "UNEE | KEJ | Кемерово | Имени Алексея Леонова",
        "URKK | KRR | Краснодар | Пашковский",
        "USUU | KRO | Курган",
        "UUOK | URS | Курск | Восточный",
        "UNKY | KYZ | Кызыл",
        "URMS | IGT | Магас",
        "USCM | MQF | Магнитогорск",
        "URML | MCX | Махачкала | Уйташ",
        "URMM | MRV | Минеральные Воды",
        "URMN | NAL | Нальчик",
        "UNWW | NOZ | Новокузнецк | Спиченково",
        "UNNT | OVB | Новосибирск | Толмачёво",
        "UNOO | OMS | Омск Центральный",
        "UWOO | REN | Оренбург",
        "UWOR | OSW | Орск",
        "URRP | ROV | Ростов-на-Дону | Платов",
        "UWWW | KUF | Самара | Курумоч",
        "UWSG | Саратов | Гагарин",
        "URFB | Севастополь | Бельбек",
        "URFF | Симферополь",
        "URSS | AER | Сочи",
        "URMT | STW | Ставрополь | Шпаковское",
        "UHBW | TYD | Тында | Тында",
        "UIUU | UUD | Улан-Удэ | Байкал",
        "UHHH | KHV | Хабаровск | Новый",
        "USCC | CEK | Челябинск | Баландино",
        "UIAA | HTA | Чита | Кадала",
        "ZFC7 | Сухум | Бабушара",
        "UKCC | DOK | Донецк | Донецк",
        "UKCW | VSG | Луганск | Луганск",
        "UKDE | OZH | Запорожье | Мокрая",
        "UKOH | KHE | Херсон | Чернобаевка",
        "UKCM | MPW | Мариуполь",
    ]

ЮВК_36 = [
    "UNWW | NOZ | Новокузнецк | Спиченково",
    "UNKY | KYZ | Кызыл",
    "UNOO | OMS | Омск Центральный",
    "UIUU | UUD | Улан-Удэ | Байкал",
    "UWOR | OSW | Орск",
    "UIAA | HTA | Чита | Кадала",
    "URWA | ASF | Астрахань",
    "UHBW | TYD | Тында | Тында",
    "URMO | OGZ | Владикавказ | Беслан",
    "UHBB | BQS | Благовещенск | Игнатьево",
    "ZFC7 | Сухум | Бабушара",
    "UHHH | KHV | Хабаровск | Новый",]

СВК = [
    "ULDD | AMV | Амдерма",
    "UHMA | DYR | Анадырь | Угольный",
    "ULMK | KVK | Апатиты | Хибины",
    "ULAA | ARH | Архангельск | Талаги",
    "UESG | BGN | Белая Гора",
    "UUOB | EGO | Белгород",
    "UHMR | Беринговский",
    "USDB | BVJ | Бованенково",
    "ULDW | VRI | Варандей",
    "ULLK | Великий Новгород | Кречевицы",
    "UUYW | VKT | Воркута",
    "UEBD | Депутатский",
    "UODD | DKS | Диксон",
    "UHME | Залив Креста",
    "UHML | Залив Лаврентия",
    "UOII | IAA | Игарка",
    "UMKK | KGD | Калининград | Храброво",
    "UHMK | KPW | Кепервеем",
    "ULMM | MMK | Мурманск",
    "USMM | NYM | Надым",
    "ULAM | NNM | Нарьян-Мар",
    "USMU | NUX | Новый Уренгой",
    "UOOO | NSK | Норильск | Алыкель",
    "UHMP | PWE | Певек",
    "ULPB | PES | Петрозаводск | Бесовец",
    "UERP | PYJ | Полярный",
    "UHMD | PVS | Бухта Провидения",
    "ULOO | PKV | Псков | Кресты",
    "USDA | SBT | Сабетта",
    "USDD | SLY | Салехард",
    "ULLI | LED | Санкт-Петербург | Пулково",
    "UERS | SYS | Саскылах",
    "ULAS | CSH | Соловки",
    "UESK | SEK | Среднеколымск",
    "UUYY | SCW | Сыктывкар",
    "UEST | IKS | Тикси",
    "UUYS | USK | Усинск",
    "UEBT | UKG | Усть-Куйга",
    "USDM | Утренний",
    "UOHH | HTG | Хатанга",
    "UESS | CYX | Черский",
    "UESO | CKH | Чокурдах",
    "USMQ | Ямбург",
    "UHMM | GDX | Магадан | Сокол",
    "UEEE | YKS | Якутск",
    ]



st.multiselect('Южный воздушный коридор', options=ЮВК, default=ЮВК_36)

#st.write(st.session_state["ЮВК"])