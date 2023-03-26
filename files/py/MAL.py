import configparser
class Я:
    def __init__(я, *СЧ, **РЧ):
        я.__СЧ = СЧ
        я.__РЧ = РЧ

    @property
    def СЧ(я): return я.__СЧ

    @property
    def РЧ(я): return я.__РЧ

    @property
    def ИД(я):
        возврат = configparser.ConfigParser()
        try:
            файл = я.РЧ.get('ini', '../ini/Я.ini')
            возврат.read(файл, encoding='utf8')
        except: возврат = {}
        finally: return возврат

if __name__ == '__main__':
    МАЛ = Я(Фамилия = "Котляров", ini = '../ini/МАЛ.ini')
    print(МАЛ.ИД.sections())