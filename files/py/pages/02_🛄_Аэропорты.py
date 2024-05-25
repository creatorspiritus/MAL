import streamlit as st
from pandas import read_csv
from функции import Наименование

st.title("Аэропорты")
st.divider()

# a = read_csv('../csv/Сводка.csv', index_col='ICAO')
# названия = [Наименование(_) for _ in a.index]

# st.write(названия)



st.write(len(st.session_state))


if "UNAA" not in st.session_state: st.session_state.UNAA = True
if "UERA" not in st.session_state: st.session_state.UERA = True
if "UEEA" not in st.session_state: st.session_state.UEEA = True
if "ULDD" not in st.session_state: st.session_state.ULDD = True
if "UHMA" not in st.session_state: st.session_state.UHMA = True
if "URKA" not in st.session_state: st.session_state.URKA = True
if "ULMK" not in st.session_state: st.session_state.ULMK = True
if "ULAA" not in st.session_state: st.session_state.ULAA = True
if "URWA" not in st.session_state: st.session_state.URWA = True
if "UHNA" not in st.session_state: st.session_state.UHNA = True
if "UNIB" not in st.session_state: st.session_state.UNIB = True
if "UWSB" not in st.session_state: st.session_state.UWSB = True
if "UNBB" not in st.session_state: st.session_state.UNBB = True
if "UEBB" not in st.session_state: st.session_state.UEBB = True
if "UESG" not in st.session_state: st.session_state.UESG = True
if "UUOB" not in st.session_state: st.session_state.UUOB = True
if "UHMR" not in st.session_state: st.session_state.UHMR = True
if "UHBB" not in st.session_state: st.session_state.UHBB = True
if "USDB" not in st.session_state: st.session_state.USDB = True
if "UHNB" not in st.session_state: st.session_state.UHNB = True
if "UIKB" not in st.session_state: st.session_state.UIKB = True
if "UHHG" not in st.session_state: st.session_state.UHHG = True
if "UIBB" not in st.session_state: st.session_state.UIBB = True
if "UUBP" not in st.session_state: st.session_state.UUBP = True
if "UNIW" not in st.session_state: st.session_state.UNIW = True
if "ULDW" not in st.session_state: st.session_state.ULDW = True
if "ULLK" not in st.session_state: st.session_state.ULLK = True
if "UENI" not in st.session_state: st.session_state.UENI = True
if "UENW" not in st.session_state: st.session_state.UENW = True
if "UHWW" not in st.session_state: st.session_state.UHWW = True
if "URMO" not in st.session_state: st.session_state.URMO = True
if "URWW" not in st.session_state: st.session_state.URWW = True
if "ULWW" not in st.session_state: st.session_state.ULWW = True
if "UUYW" not in st.session_state: st.session_state.UUYW = True
if "UUOO" not in st.session_state: st.session_state.UUOO = True
if "URKG" not in st.session_state: st.session_state.URKG = True
if "UNBG" not in st.session_state: st.session_state.UNBG = True
if "URMG" not in st.session_state: st.session_state.URMG = True
if "UEBD" not in st.session_state: st.session_state.UEBD = True
if "UODD" not in st.session_state: st.session_state.UODD = True
if "USSS" not in st.session_state: st.session_state.USSS = True
if "UNII" not in st.session_state: st.session_state.UNII = True
if "UIKE" not in st.session_state: st.session_state.UIKE = True
if "UEVV" not in st.session_state: st.session_state.UEVV = True
if "UUBW" not in st.session_state: st.session_state.UUBW = True
if "UHME" not in st.session_state: st.session_state.UHME = True
if "UHML" not in st.session_state: st.session_state.UHML = True
if "UHBE" not in st.session_state: st.session_state.UHBE = True
if "UESU" not in st.session_state: st.session_state.UESU = True
if "UUBI" not in st.session_state: st.session_state.UUBI = True
if "UOII" not in st.session_state: st.session_state.UOII = True
if "USII" not in st.session_state: st.session_state.USII = True
if "UIII" not in st.session_state: st.session_state.UIII = True
if "UWKJ" not in st.session_state: st.session_state.UWKJ = True
if "UWKD" not in st.session_state: st.session_state.UWKD = True
if "UMKK" not in st.session_state: st.session_state.UMKK = True
if "UUBC" not in st.session_state: st.session_state.UUBC = True
if "UHPZ" not in st.session_state: st.session_state.UHPZ = True
if "UNEE" not in st.session_state: st.session_state.UNEE = True
if "UHMK" not in st.session_state: st.session_state.UHMK = True
if "UIKK" not in st.session_state: st.session_state.UIKK = True
if "USKK" not in st.session_state: st.session_state.USKK = True
if "USRK" not in st.session_state: st.session_state.USRK = True
if "UNKI" not in st.session_state: st.session_state.UNKI = True
if "UHKK" not in st.session_state: st.session_state.UHKK = True
if "UUBA" not in st.session_state: st.session_state.UUBA = True
if "URKK" not in st.session_state: st.session_state.URKK = True
if "UNKL" not in st.session_state: st.session_state.UNKL = True
if "USUU" not in st.session_state: st.session_state.USUU = True
if "UUOK" not in st.session_state: st.session_state.UUOK = True
if "UNKY" not in st.session_state: st.session_state.UNKY = True
if "UERL" not in st.session_state: st.session_state.UERL = True
if "UUOL" not in st.session_state: st.session_state.UUOL = True
if "UHMM" not in st.session_state: st.session_state.UHMM = True
if "UEMM" not in st.session_state: st.session_state.UEMM = True
if "URMS" not in st.session_state: st.session_state.URMS = True
if "USCM" not in st.session_state: st.session_state.USCM = True
if "UHPN" not in st.session_state: st.session_state.UHPN = True
if "UHMO" not in st.session_state: st.session_state.UHMO = True
if "URML" not in st.session_state: st.session_state.URML = True
if "UHPM" not in st.session_state: st.session_state.UHPM = True
if "URMM" not in st.session_state: st.session_state.URMM = True
if "UERR" not in st.session_state: st.session_state.UERR = True
if "UEMA" not in st.session_state: st.session_state.UEMA = True
if "UUWW" not in st.session_state: st.session_state.UUWW = True
if "UUDD" not in st.session_state: st.session_state.UUDD = True
if "UUEE" not in st.session_state: st.session_state.UUEE = True
if "UNIM" not in st.session_state: st.session_state.UNIM = True
if "ULMM" not in st.session_state: st.session_state.ULMM = True
if "USMM" not in st.session_state: st.session_state.USMM = True
if "URMN" not in st.session_state: st.session_state.URMN = True
if "ULAM" not in st.session_state: st.session_state.ULAM = True
if "UELL" not in st.session_state: st.session_state.UELL = True
if "UIUN" not in st.session_state: st.session_state.UIUN = True
if "USNN" not in st.session_state: st.session_state.USNN = True
if "UWKE" not in st.session_state: st.session_state.UWKE = True
if "UWGG" not in st.session_state: st.session_state.UWGG = True
if "UHNN" not in st.session_state: st.session_state.UHNN = True
if "UHPX" not in st.session_state: st.session_state.UHPX = True
if "UNWW" not in st.session_state: st.session_state.UNWW = True
if "UNNT" not in st.session_state: st.session_state.UNNT = True
if "USMU" not in st.session_state: st.session_state.USMU = True
if "UHSN" not in st.session_state: st.session_state.UHSN = True
if "UOOO" not in st.session_state: st.session_state.UOOO = True
if "USRO" not in st.session_state: st.session_state.USRO = True
if "UENN" not in st.session_state: st.session_state.UENN = True
if "UHQO" not in st.session_state: st.session_state.UHQO = True
if "UEMO" not in st.session_state: st.session_state.UEMO = True
if "UERO" not in st.session_state: st.session_state.UERO = True
if "UHMN" not in st.session_state: st.session_state.UHMN = True
if "UNOO" not in st.session_state: st.session_state.UNOO = True
if "UHMF" not in st.session_state: st.session_state.UHMF = True
if "UWOO" not in st.session_state: st.session_state.UWOO = True
if "UWOR" not in st.session_state: st.session_state.UWOR = True
if "UHPD" not in st.session_state: st.session_state.UHPD = True
if "UHSH" not in st.session_state: st.session_state.UHSH = True
if "UHOO" not in st.session_state: st.session_state.UHOO = True
if "UHPL" not in st.session_state: st.session_state.UHPL = True
if "ZD5W" not in st.session_state: st.session_state.ZD5W = True
if "UHPA" not in st.session_state: st.session_state.UHPA = True
if "UHMP" not in st.session_state: st.session_state.UHMP = True
if "UWPP" not in st.session_state: st.session_state.UWPP = True
if "USPP" not in st.session_state: st.session_state.USPP = True
if "ULPB" not in st.session_state: st.session_state.ULPB = True
if "UHPP" not in st.session_state: st.session_state.UHPP = True
if "UNIP" not in st.session_state: st.session_state.UNIP = True
if "UERP" not in st.session_state: st.session_state.UERP = True
if "UHMD" not in st.session_state: st.session_state.UHMD = True
if "ULOO" not in st.session_state: st.session_state.ULOO = True
if "URRP" not in st.session_state: st.session_state.URRP = True
if "USDA" not in st.session_state: st.session_state.USDA = True
if "UEBS" not in st.session_state: st.session_state.UEBS = True
if "USDD" not in st.session_state: st.session_state.USDD = True
if "UWWW" not in st.session_state: st.session_state.UWWW = True
if "UEMS" not in st.session_state: st.session_state.UEMS = True
if "ULLI" not in st.session_state: st.session_state.ULLI = True
if "UWPS" not in st.session_state: st.session_state.UWPS = True
if "UWSG" not in st.session_state: st.session_state.UWSG = True
if "UERS" not in st.session_state: st.session_state.UERS = True
if "URFB" not in st.session_state: st.session_state.URFB = True
if "UNIS" not in st.session_state: st.session_state.UNIS = True
if "UHMW" not in st.session_state: st.session_state.UHMW = True
if "UHMS" not in st.session_state: st.session_state.UHMS = True
if "URFF" not in st.session_state: st.session_state.URFF = True
if "UHPS" not in st.session_state: st.session_state.UHPS = True
if "ULAS" not in st.session_state: st.session_state.ULAS = True
if "URSS" not in st.session_state: st.session_state.URSS = True
if "UESK" not in st.session_state: st.session_state.UESK = True
if "URMT" not in st.session_state: st.session_state.URMT = True
if "UENS" not in st.session_state: st.session_state.UENS = True
if "USRR" not in st.session_state: st.session_state.USRR = True
if "UUYY" not in st.session_state: st.session_state.UUYY = True
if "UIKG" not in st.session_state: st.session_state.UIKG = True
if "UECT" not in st.session_state: st.session_state.UECT = True
if "UUOT" not in st.session_state: st.session_state.UUOT = True
if "USDS" not in st.session_state: st.session_state.USDS = True
if "UHPG" not in st.session_state: st.session_state.UHPG = True
if "UEST" not in st.session_state: st.session_state.UEST = True
if "UHPT" not in st.session_state: st.session_state.UHPT = True
if "USDO" not in st.session_state: st.session_state.USDO = True
if "UNTT" not in st.session_state: st.session_state.UNTT = True
if "UNIT" not in st.session_state: st.session_state.UNIT = True
if "UOTT" not in st.session_state: st.session_state.UOTT = True
if "UHBW" not in st.session_state: st.session_state.UHBW = True
if "USTR" not in st.session_state: st.session_state.USTR = True
if "UIUU" not in st.session_state: st.session_state.UIUU = True
if "UWLL" not in st.session_state: st.session_state.UWLL = True
if "UUYS" not in st.session_state: st.session_state.UUYS = True
if "UHPK" not in st.session_state: st.session_state.UHPK = True
if "UEBT" not in st.session_state: st.session_state.UEBT = True
if "UITT" not in st.session_state: st.session_state.UITT = True
if "UEMU" not in st.session_state: st.session_state.UEMU = True
if "UEMT" not in st.session_state: st.session_state.UEMT = True
if "UHPU" not in st.session_state: st.session_state.UHPU = True
if "USDM" not in st.session_state: st.session_state.USDM = True
if "UWUU" not in st.session_state: st.session_state.UWUU = True
if "UHHH" not in st.session_state: st.session_state.UHHH = True
if "UEMH" not in st.session_state: st.session_state.UEMH = True
if "USHH" not in st.session_state: st.session_state.USHH = True
if "UOHH" not in st.session_state: st.session_state.UOHH = True
if "UHNH" not in st.session_state: st.session_state.UHNH = True
if "UIAR" not in st.session_state: st.session_state.UIAR = True
if "UWKS" not in st.session_state: st.session_state.UWKS = True
if "USCC" not in st.session_state: st.session_state.USCC = True
if "ULWC" not in st.session_state: st.session_state.ULWC = True
if "UESS" not in st.session_state: st.session_state.UESS = True
if "UIAA" not in st.session_state: st.session_state.UIAA = True
if "UESO" not in st.session_state: st.session_state.UESO = True
if "UHHY" not in st.session_state: st.session_state.UHHY = True
if "UHSK" not in st.session_state: st.session_state.UHSK = True
if "HC3Y" not in st.session_state: st.session_state.HC3Y = True
if "UHBP" not in st.session_state: st.session_state.UHBP = True
if "URWI" not in st.session_state: st.session_state.URWI = True
if "UHSM" not in st.session_state: st.session_state.UHSM = True
if "UHSS" not in st.session_state: st.session_state.UHSS = True
if "UEEE" not in st.session_state: st.session_state.UEEE = True
if "USMQ" not in st.session_state: st.session_state.USMQ = True
if "UUDL" not in st.session_state: st.session_state.UUDL = True
if "UHSI" not in st.session_state: st.session_state.UHSI = True
if "ZFC7" not in st.session_state: st.session_state.ZFC7 = True
if "UKCC" not in st.session_state: st.session_state.UKCC = False
if "UKCW" not in st.session_state: st.session_state.UKCW = False
if "UKDE" not in st.session_state: st.session_state.UKDE = False
if "UKOH" not in st.session_state: st.session_state.UKOH = False
if "UKCM" not in st.session_state: st.session_state.UKCM = False

if "радиус_зоны_ответственности" not in st.session_state:
    st.session_state["радиус_зоны_ответственности"] = 1000
if "радиус_зоны_агломерации" not in st.session_state:
    st.session_state["радиус_зоны_агломерации"] = 100

st.sidebar.number_input(
    "Радиус зоны агломерации",
    min_value=50, max_value=500,
    value=st.session_state["радиус_зоны_агломерации"],
    key="радиус_зоны_агломерации"
)

st.sidebar.number_input(
    "Радиус зоны ответственности",
    min_value=0, max_value=2000,
    value=st.session_state["радиус_зоны_ответственности"],
    key="радиус_зоны_ответственности"
)

st.write(len(st.session_state))


st.checkbox("UNAA | ABA | Абакан", value=True, key="UNAA")
st.checkbox("UERA | Айхал", value=True, key="UERA")
st.checkbox("UEEA | ADH | Алдан", value=True, key="UEEA")
st.checkbox("ULDD | AMV | Амдерма", value=True, key="ULDD")
st.checkbox("UHMA | DYR | Анадырь | Угольный", value=True, key="UHMA")
st.checkbox("URKA | AAQ | Анапа | Витязево", value=True, key="URKA")
st.checkbox("ULMK | KVK | Апатиты | Хибины", value=True, key="ULMK")
st.checkbox("ULAA | ARH | Архангельск | Талаги", value=True, key="ULAA")
st.checkbox("URWA | ASF | Астрахань", value=True, key="URWA")
st.checkbox("UHNA | Аян | Мунук", value=True, key="UHNA")
st.checkbox("UNIB | Байкит", value=True, key="UNIB")
st.checkbox("UWSB | BWO | Балаково | Малая Быковка", value=True, key="UWSB")
st.checkbox("UNBB | BAX | Барнаул | Имени Германа Титова", value=True, key="UNBB")
st.checkbox("UEBB | Батагай", value=True, key="UEBB")
st.checkbox("UESG | BGN | Белая Гора", value=True, key="UESG")
st.checkbox("UUOB | EGO | Белгород", value=True, key="UUOB")
st.checkbox("UHMR | Беринговский", value=True, key="UHMR")
st.checkbox("UHBB | BQS | Благовещенск | Игнатьево", value=True, key="UHBB")
st.checkbox("USDB | BVJ | Бованенково", value=True, key="USDB")
st.checkbox("UHNB | BQG | Богородское", value=True, key="UHNB")
st.checkbox("UIKB | ODO | Бодайбо", value=True, key="UIKB")
st.checkbox("UHHG | Бомнак", value=True, key="UHHG")
st.checkbox("UIBB | BTK | Братск", value=True, key="UIBB")
st.checkbox("UUBP | BZK | Брянск", value=True, key="UUBP")
st.checkbox("UNIW | Ванавара", value=True, key="UNIW")
st.checkbox("ULDW | VRI | Варандей", value=True, key="ULDW")
st.checkbox("ULLK | Великий Новгород | Кречевицы", value=True, key="ULLK")
st.checkbox("UENI | VHV | Верхневилюйск", value=True, key="UENI")
st.checkbox("UENW | VYI | Вилюйск", value=True, key="UENW")
st.checkbox("UHWW | VVO | Владивосток | Кневичи", value=True, key="UHWW")
st.checkbox("URMO | OGZ | Владикавказ | Беслан", value=True, key="URMO")
st.checkbox("URWW | VOG | Волгоград | Гумрак", value=True, key="URWW")
st.checkbox("ULWW | VGD | Вологда", value=True, key="ULWW")
st.checkbox("UUYW | VKT | Воркута", value=True, key="UUYW")
st.checkbox("UUOO | VOZ | Воронеж | Чертовицкое", value=True, key="UUOO")
st.checkbox("URKG | GDZ | Геленджик", value=True, key="URKG")
st.checkbox("UNBG | RGK | Горно-Алтайск", value=True, key="UNBG")
st.checkbox("URMG | GRV | Грозный | Северный", value=True, key="URMG")
st.checkbox("UEBD | Депутатский", value=True, key="UEBD")
st.checkbox("UODD | DKS | Диксон", value=True, key="UODD")
st.checkbox("USSS | SVX | Екатеринбург | Кольцово", value=True, key="USSS")
st.checkbox("UNII | EIE | Енисейск", value=True, key="UNII")
st.checkbox("UIKE | ERG | Ербогачен", value=True, key="UIKE")
st.checkbox("UEVV | ZIX | Жиганск", value=True, key="UEVV")
st.checkbox("UUBW | ZIA | Раменское | Жуковский", value=True, key="UUBW")
st.checkbox("UHME | Залив Креста", value=True, key="UHME")
st.checkbox("UHML | Залив Лаврентия", value=True, key="UHML")
st.checkbox("UHBE | Зея | Зея", value=True, key="UHBE")
st.checkbox("UESU | ZKP | Зырянка", value=True, key="UESU")
st.checkbox("UUBI | IWA | Иваново | Южный", value=True, key="UUBI")
st.checkbox("UOII | IAA | Игарка", value=True, key="UOII")
st.checkbox("USII | IJK | Ижевск", value=True, key="USII")
st.checkbox("UIII | IKT | Иркутск", value=True, key="UIII")
st.checkbox("UWKJ | JOK | Йошкар-Ола", value=True, key="UWKJ")
st.checkbox("UWKD | KZN | Казань", value=True, key="UWKD")
st.checkbox("UMKK | KGD | Калининград | Храброво", value=True, key="UMKK")
st.checkbox("UUBC | KLF | Калуга | Грабцево", value=True, key="UUBC")
st.checkbox("UHPZ | Каменское", value=True, key="UHPZ")
st.checkbox("UNEE | KEJ | Кемерово | Имени Алексея Леонова", value=True, key="UNEE")
st.checkbox("UHMK | KPW | Кепервеем", value=True, key="UHMK")
st.checkbox("UIKK | KCK | Киренск", value=True, key="UIKK")
st.checkbox("USKK | KVX | Киров | Победилово", value=True, key="USKK")
st.checkbox("USRK | KGP | Когалым", value=True, key="USRK")
st.checkbox("UNKI | Кодинск", value=True, key="UNKI")
st.checkbox("UHKK | KXK | Комсомольск-на-Амуре | Хурба", value=True, key="UHKK")
st.checkbox("UUBA | KMW | Кострома | Сокеркино", value=True, key="UUBA")
st.checkbox("URKK | KRR | Краснодар | Пашковский", value=True, key="URKK")
st.checkbox("UNKL | KJA | Красноярск | Емельяново", value=True, key="UNKL")
st.checkbox("USUU | KRO | Курган", value=True, key="USUU")
st.checkbox("UUOK | URS | Курск | Восточный", value=True, key="UUOK")
st.checkbox("UNKY | KYZ | Кызыл", value=True, key="UNKY")
st.checkbox("UERL | ULK | Ленск | Ленск", value=True, key="UERL")
st.checkbox("UUOL | LPK | Липецк", value=True, key="UUOL")
st.checkbox("UHMM | GDX | Магадан | Сокол", value=True, key="UHMM")
st.checkbox("UEMM | GYG | Маган", value=True, key="UEMM")
st.checkbox("URMS | IGT | Магас", value=True, key="URMS")
st.checkbox("USCM | MQF | Магнитогорск", value=True, key="USCM")
st.checkbox("UHPN | Манилы", value=True, key="UHPN")
st.checkbox("UHMO | KVM | Марково | Марково", value=True, key="UHMO")
st.checkbox("URML | MCX | Махачкала | Уйташ", value=True, key="URML")
st.checkbox("UHPM | Мильково", value=True, key="UHPM")
st.checkbox("URMM | MRV | Минеральные Воды", value=True, key="URMM")
st.checkbox("UERR | MJZ | Мирный", value=True, key="UERR")
st.checkbox("UEMA | MQJ | Мома", value=True, key="UEMA")
st.checkbox("UUWW | VKO | Москва | Внуково", value=True, key="UUWW")
st.checkbox("UUDD | DME | Москва | Домодедово", value=True, key="UUDD")
st.checkbox("UUEE | SVO | Москва | Шереметьево", value=True, key="UUEE")
st.checkbox("UNIM | Мотыгино", value=True, key="UNIM")
st.checkbox("ULMM | MMK | Мурманск", value=True, key="ULMM")
st.checkbox("USMM | NYM | Надым", value=True, key="USMM")
st.checkbox("URMN | NAL | Нальчик", value=True, key="URMN")
st.checkbox("ULAM | NNM | Нарьян-Мар", value=True, key="ULAM")
st.checkbox("UELL | NER | Нерюнгри | Чульман", value=True, key="UELL")
st.checkbox("UIUN | Нижнеангарск", value=True, key="UIUN")
st.checkbox("USNN | NJC | Нижневартовск | Нижневартовск", value=True, key="USNN")
st.checkbox("UWKE | NBC | Нижнекамск | Бегишево", value=True, key="UWKE")
st.checkbox("UWGG | GOJ | Нижний Новгород | Стригино", value=True, key="UWGG")
st.checkbox("UHNN | NLI | Николаевск-на-Амуре", value=True, key="UHNN")
st.checkbox("UHPX | Никольское", value=True, key="UHPX")
st.checkbox("UNWW | NOZ | Новокузнецк | Спиченково", value=True, key="UNWW")
st.checkbox("UNNT | OVB | Новосибирск | Толмачёво", value=True, key="UNNT")
st.checkbox("USMU | NUX | Новый Уренгой", value=True, key="USMU")
st.checkbox("UHSN | NGK | Ноглики", value=True, key="UHSN")
st.checkbox("UOOO | NSK | Норильск | Алыкель", value=True, key="UOOO")
st.checkbox("USRO | NOJ | Ноябрьск", value=True, key="USRO")
st.checkbox("UENN | NYR | Нюрба", value=True, key="UENN")
st.checkbox("UHQO | Запорожье | Озерная", value=True, key="UHQO")
st.checkbox("UEMO | OLZ | Олёкминск", value=True, key="UEMO")
st.checkbox("UERO | ONK | Оленек", value=True, key="UERO")
st.checkbox("UHMN | Омолон", value=True, key="UHMN")
st.checkbox("UNOO | OMS | Омск Центральный", value=True, key="UNOO")
st.checkbox("UHMF | Омсукчан", value=True, key="UHMF")
st.checkbox("UWOO | REN | Оренбург", value=True, key="UWOO")
st.checkbox("UWOR | OSW | Орск", value=True, key="UWOR")
st.checkbox("UHPD | Оссора", value=True, key="UHPD")
st.checkbox("UHSH | OHH | Оха | Новостройка", value=True, key="UHSH")
st.checkbox("UHOO | OHO | Охотск", value=True, key="UHOO")
st.checkbox("UHPL | Палана", value=True, key="UHPL")
st.checkbox("ZD5W | Парамушир", value=True, key="ZD5W")
st.checkbox("UHPA | Пахачи", value=True, key="UHPA")
st.checkbox("UHMP | PWE | Певек", value=True, key="UHMP")
st.checkbox("UWPP | PEZ | Пенза", value=True, key="UWPP")
st.checkbox("USPP | PEE | Пермь | Большое Савино", value=True, key="USPP")
st.checkbox("ULPB | PES | Петрозаводск | Бесовец", value=True, key="ULPB")
st.checkbox("UHPP | PKC | Петропавловск-Камчатский | Елизово", value=True, key="UHPP")
st.checkbox("UNIP | TGP | Подкаменная Тунгуска", value=True, key="UNIP")
st.checkbox("UERP | PYJ | Полярный", value=True, key="UERP")
st.checkbox("UHMD | PVS | Бухта Провидения", value=True, key="UHMD")
st.checkbox("ULOO | PKV | Псков | Кресты", value=True, key="ULOO")
st.checkbox("URRP | ROV | Ростов-на-Дону | Платов", value=True, key="URRP")
st.checkbox("USDA | SBT | Сабетта", value=True, key="USDA")
st.checkbox("UEBS | SUK | Саккырыр", value=True, key="UEBS")
st.checkbox("USDD | SLY | Салехард", value=True, key="USDD")
st.checkbox("UWWW | KUF | Самара | Курумоч", value=True, key="UWWW")
st.checkbox("UEMS | Сангар", value=True, key="UEMS")
st.checkbox("ULLI | LED | Санкт-Петербург | Пулково", value=True, key="ULLI")
st.checkbox("UWPS | SKX | Саранск", value=True, key="UWPS")
st.checkbox("UWSG | Саратов | Гагарин", value=True, key="UWSG")
st.checkbox("UERS | SYS | Саскылах", value=True, key="UERS")
st.checkbox("URFB | Севастополь | Бельбек", value=True, key="URFB")
st.checkbox("UNIS | Северо-Енисейск", value=True, key="UNIS")
st.checkbox("UHMW | SWV | Северо-Эвенск", value=True, key="UHMW")
st.checkbox("UHMS | Сеймчан", value=True, key="UHMS")
st.checkbox("URFF | Симферополь", value=True, key="URFF")
st.checkbox("UHPS | Соболево | Соболево", value=True, key="UHPS")
st.checkbox("ULAS | CSH | Соловки", value=True, key="ULAS")
st.checkbox("URSS | AER | Сочи", value=True, key="URSS")
st.checkbox("UESK | SEK | Среднеколымск", value=True, key="UESK")
st.checkbox("URMT | STW | Ставрополь | Шпаковское", value=True, key="URMT")
st.checkbox("UENS | SUY | Сунтар", value=True, key="UENS")
st.checkbox("USRR | SGC | Сургут", value=True, key="USRR")
st.checkbox("UUYY | SCW | Сыктывкар", value=True, key="UUYY")
st.checkbox("UIKG | Таксимо", value=True, key="UIKG")
st.checkbox("UECT | TLK | Талакан", value=True, key="UECT")
st.checkbox("UUOT | TBW | Тамбов | Донское", value=True, key="UUOT")
st.checkbox("USDS | TQL | Тарко-Сале", value=True, key="USDS")
st.checkbox("UHPG | Тигиль", value=True, key="UHPG")
st.checkbox("UEST | IKS | Тикси", value=True, key="UEST")
st.checkbox("UHPT | Тиличики", value=True, key="UHPT")
st.checkbox("USDO | Толька", value=True, key="USDO")
st.checkbox("UNTT | TOF | Томск | Богашёво", value=True, key="UNTT")
st.checkbox("UNIT | Тура-Горный", value=True, key="UNIT")
st.checkbox("UOTT | THX | Туруханск | Туруханск", value=True, key="UOTT")
st.checkbox("UHBW | TYD | Тында | Тында", value=True, key="UHBW")
st.checkbox("USTR | TJM | Тюмень | Рощино", value=True, key="USTR")
st.checkbox("UIUU | UUD | Улан-Удэ | Байкал", value=True, key="UIUU")
st.checkbox("UWLL | ULV | Ульяновск | Баратаевка", value=True, key="UWLL")
st.checkbox("UUYS | USK | Усинск", value=True, key="UUYS")
st.checkbox("UHPK | Усть-Камчатск", value=True, key="UHPK")
st.checkbox("UEBT | UKG | Усть-Куйга", value=True, key="UEBT")
st.checkbox("UITT | UKX | Усть-Кут | Усть-Кут", value=True, key="UITT")
st.checkbox("UEMU | UMS | Усть-Мая", value=True, key="UEMU")
st.checkbox("UEMT | USR | Усть-Нера", value=True, key="UEMT")
st.checkbox("UHPU | Усть-Хайрюзово", value=True, key="UHPU")
st.checkbox("USDM | Утренний", value=True, key="USDM")
st.checkbox("UWUU | UFA | Уфа", value=True, key="UWUU")
st.checkbox("UHHH | KHV | Хабаровск | Новый", value=True, key="UHHH")
st.checkbox("UEMH | KDY | Хандыга | Теплый Ключ", value=True, key="UEMH")
st.checkbox("USHH | HMA | Ханты-Мансийск", value=True, key="USHH")
st.checkbox("UOHH | HTG | Хатанга", value=True, key="UOHH")
st.checkbox("UHNH | Херпучи", value=True, key="UHNH")
st.checkbox("UIAR | Чара", value=True, key="UIAR")
st.checkbox("UWKS | CSY | Чебоксары", value=True, key="UWKS")
st.checkbox("USCC | CEK | Челябинск | Баландино", value=True, key="USCC")
st.checkbox("ULWC | CEE | Череповец", value=True, key="ULWC")
st.checkbox("UESS | CYX | Черский", value=True, key="UESS")
st.checkbox("UIAA | HTA | Чита | Кадала", value=True, key="UIAA")
st.checkbox("UESO | CKH | Чокурдах", value=True, key="UESO")
st.checkbox("UHHY | Чумикан", value=True, key="UHHY")
st.checkbox("UHSK | EKS | Шахтерск", value=True, key="UHSK")
st.checkbox("HC3Y | Малокурильское", value=True, key="HC3Y")
st.checkbox("UHBP | Экимчан | Экимчан", value=True, key="UHBP")
st.checkbox("URWI | ESL | Элиста", value=True, key="URWI")
st.checkbox("UHSM | DEE | Южно-Курильск | Менделеево", value=True, key="UHSM")
st.checkbox("UHSS | UUS | Южно-Сахалинск | Хомутово", value=True, key="UHSS")
st.checkbox("UEEE | YKS | Якутск", value=True, key="UEEE")
st.checkbox("USMQ | Ямбург", value=True, key="USMQ")
st.checkbox("UUDL | IAR | Ярославль | Туношна", value=True, key="UUDL")
st.checkbox("UHSI | ITU | Итуруп", value=True, key="UHSI")
st.checkbox("ZFC7 | Сухум | Бабушара", value=True, key="ZFC7")
st.checkbox("UKCC | DOK | Донецк | Донецк", value=False, key="UKCC")
st.checkbox("UKCW | VSG | Луганск | Луганск", value=False, key="UKCW")
st.checkbox("UKDE | OZH | Запорожье | Мокрая", value=False, key="UKDE")
st.checkbox("UKOH | KHE | Херсон | Чернобаевка", value=False, key="UKOH")
st.checkbox("UKCM | MPW | Мариуполь", value=False, key="UKCM")
