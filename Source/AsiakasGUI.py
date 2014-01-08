import tkinter

class AsiakasGUI:
    def __init__(self):
        #Konstruktori
        self.mainwindow = tkinter.Tk()
        #Tässä käynnistetään tkinter-moduulilla ohjelman käyttöliittymän pääikkuna
        self.tiedotus = tkinter.Label(self.mainwindow, text='Asiakashallintaohjelmisto 1.0')
        #Käytetään paddinglabel-tekstiä välin luomiseksi käyttöliittymään
        self.paddinglabel = tkinter.Label(self.mainwindow, text='')
        #Seuraavaksi tehdään checkbuttonit käyttöliittymän vaihtoehdoille
        #Luodaan ensin variable
        self.radiovalinta = tkinter.IntVar()
        self.radiovalinta.set(0)
        #Luodaan BUTTONIT-niminen tietorakenne, jossa moniulotteisia alkioita
        BUTTONIT = [("Listaa kaikki asiakkaat", 1), ("Lisää asiakas listaan",2),("Muokkaa listalla olevaa asiakasta",3),("Poista asiakkaan tiedot listalta",4),
                    ("Etsi asiakasta listalta", 5),("Sulje ohjelma ja tallenna tiedot",6)
                    ]
        #Seuraaksi otetaan jokaisesta alkiosta data ja tehdään dataa vastaava buttoni
        for teksti, arvo in BUTTONIT:
            self.buttoni = tkinter.Radiobutton(self.mainwindow, text=teksti, variable=self.radiovalinta, value=arvo,indicatoron=0).pack(anchor='w')

        #Tehdään metodi, jolla voidaan palauttaa pääohjelmaan radiovalinta-muuttujan senhetkinen arvo
        def get__radiovalinta(self):
            return self.radiovalinta

        #Tkinter-moduulin päälooppi
        tkinter.mainloop()
