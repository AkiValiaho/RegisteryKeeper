class henkilo():
    def __init__(self,nimi,osoite,puhelinnumero):
        self.nimi = nimi
        self.puhelinnumero = puhelinnumero
        self.osoite = osoite
    def get_name(self):
        return self.nimi
    def set_name(self,nimi):
        self.nimi = nimi
    def get_puhelinnumero(self):
        return self.puhelinnumero
    def set_puhelinnumero(self, puhelinnumero):
        self.puhelinnumero = puhelinnumero
    def get_osoite(self):
        return osoite
    def set_osoite(self):
        self.osoite = osoite
    def __str__(self):
        return 'Nimi {0}, Osoite {1}, Puhelinnumero {1}'.format(self.get_name(), self.get_puhelinnumero(),self.get_osoite)

