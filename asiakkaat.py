class asiakkaat:
    def __init__(self,nimi, kanta_asiakas, kaynti,ika, sukupuoli):
        self.__nimi = nimi
        self.__kanta_asiakas = kanta_asiakas
        self.__kaynti = kaynti
        self.__ika = ika
        self.__sukupuoli = sukupuoli

    def get__ika(self):
        return self.__ika
    def set__ika(self,ika):
        self.__ika = ika
    def get__sukupuoli(self):
        return self.__sukupuoli
    def set__sukupuoli(self,sukupuoli):
        self.__sukupuoli =  sukupuoli
    def get__nimi(self):
        return self.__nimi
    def set__nimi(self,nimi):
        self.__nimi = nimi
    def get__kanta_asiakas(self):
        return self.__kanta_asiakas
    def set__kanta_asiakas(self,kanta_asiakas):
        self.__kanta_asiakas = kanta_asiakas
    def get__kaynti(self):
        return self.__kaynti
    def set__kaynti(self,kaynti):
        self.__kaynti = kaynti
    def __str__(self):
        return "Nimi: {0}\nKanta-asiakkuuskortti: {1}\nViimeisin käynti: {2}\nIkä: {3}\nSukupuoli: {4}".format(self.get__nimi(),\
                                                                                                               self.get__kanta_asiakas(),self.get__kaynti(),\
                                                                                                               self.get__ika(),self.get__sukupuoli())
