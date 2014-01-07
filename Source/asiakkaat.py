

class asiakkaat:
    def __init__(self,nimi, osasto, toimi):
        self.__nimi = nimi
        self.__osasto = osasto
        self.__toimi = toimi
    def get__nimi(self):
        return self.__nimi
    def set__nimi(self,nimi):
        self.__nimi = nimi
    def get__osasto(self):
        return self.__osasto
    def set__osasto(self,osasto):
        self.__osasto = osasto
    def get__toimi(self):
        return self.__toimi
    def set__toimi(self,toimi):
        self.__toimi = toimi
    def __str__(self):
        return "Nimi: {0} Osasto: {1} Toimi: {2}".format(self.get__nimi(),self.get__osasto(),self.get__toimi())
