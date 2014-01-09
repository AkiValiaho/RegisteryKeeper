import tkinter,flowcontrol,dumper,asiakkaat,tkinter.messagebox


def muokkaa_asiakasta(nimilista):
    pass
def poista_asiakas(nimilista):
    pass
def etsi_asiakas(nimilista):
    pass
def sulje_tallenna(nimilista):
    pass

class AsiakasGUI:
        def __init__(self,nimilista,frame):
            #Konstruktori
            self.nimilista = nimilista
            mainframe = tkinter.Frame(frame)
            #Tässä käynnistetään tkinter-moduulilla ohjelman käyttöliittymän pääikkuna
            self.tiedotus = tkinter.Label(frame, text='Asiakashallintaohjelmisto 1.0')
            #Käytetään paddinglabel-tekstiä välin luomiseksi käyttöliittymään
            self.paddinglabel = tkinter.Label(frame, text='')
            #Luodaan listboxi, johon conffataan erikseen scrollbar
            self.listbox = tkinter.Listbox(frame)
            self.listbox.bind("<Double-Button-1>", self.showinfo)
            self.listbox.pack(fill = 'x')
            scrollbar = tkinter.Scrollbar(frame)
            scrollbar.pack(side='right', fill='y' )
            #Testaus
            for i in nimilista:
                    self.listbox.insert('end',i)
            #Yhdistetään sitten scrollbar toimimaan listboxin kanssa
            self.listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=self.listbox.yview)
            self.buttoni1 = tkinter.Button(frame, text='Lisää asiakas', command=self.lisaa_asiakas).pack(anchor='w',fill = 'x')
            self.buttoni2 = tkinter.Button(frame, text='Muokkaa listalla olevaa asiakasta', command=muokkaa_asiakasta).pack(anchor='w', fill = 'x')
            self.buttoni3 = tkinter.Button(frame, text='Poista asiakas', command=poista_asiakas).pack(anchor='w',fill = 'x')
            self.buttoni4 = tkinter.Button(frame, text='Etsi asiakas', command=etsi_asiakas).pack(anchor='w',fill = 'x')
            self.buttoni5 = tkinter.Button(frame, text='Sulje ja tallenna', command=sulje_tallenna).pack(anchor='w',fill = 'x')
        def lisaa_asiakas(self):
            asiakas = asiakkaat.asiakkaat(input("Anna asiakkaan nimi: "),input("Kanta-asiakaskortti? "), input("Viimeisin käynti: "))
            if self.nimilista != None:
                if asiakas.get__nimi() in self.nimilista:
                        print("Nimilistalla on jo henkilo {0}".format(asiakas.get__nimi()))
                else:
                        self.nimilista[asiakas.get__nimi()] = asiakas
                        self.listbox.insert('end',asiakas.get__nimi())
        def showinfo(self,asdf):
            currentitem =self.listbox.get('active')
            tkinter.messagebox.showinfo(self.nimilista[currentitem].get__nimi(), self.nimilista[currentitem].__str__())




        #Tkinter-moduulin päälooppi
def main():
    nimilista = {}
    nimilista = dumper.load()
    mainwindow = tkinter.Tk()
    mainwindow.wm_title('Asiakashallintaohjelmisto')
    #mainwindow.iconbitmap(default='transparent.ico') keksi uusi ikoni
    asiakasGUI = AsiakasGUI(nimilista,mainwindow)
    mainwindow.mainloop()
