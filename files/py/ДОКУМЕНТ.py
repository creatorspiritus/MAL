from Я import *

class ТЕКСТ(Я):
    def __init__(я, *СЧ, **РЧ):
        РЧ['Текст'] = РЧ.get('Текст', СЧ[0])
        super().__init__(*СЧ, **РЧ)
    
    @property
    def Текст(я): return я.РЧ['Текст']
    
    @Текст.setter
    def Текст(я, значение):
        if isinstance(значение, str):
            я.ДЧ(Текст = значение)
        else: ...
        return None