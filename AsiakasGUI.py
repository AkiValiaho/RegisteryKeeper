import tkinter,dumper,asiakkaat,tkinter.messagebox,tkinter.simpledialog
class popupWindow:
    def __init__(self,nimilista,currentitem):
        self.mainframe = tkinter.Toplevel()
        self.nimilista = nimilista
        self.currentitem = currentitem
        self.label1 = tkinter.Label(self.mainframe,text='Muokkaat tällä hetkellä henkilöä: {0}'.format(self.currentitem)).pack()
        self.label = tkinter.Label(self.mainframe,text='Henkilön nimi').pack()
        self.e=tkinter.Entry(self.mainframe)
        self.e.pack()
        self.label1 = tkinter.Label(self.mainframe,text='Kanta-asiakaskortti?').pack()
        self.radiobuttonvariable = tkinter.IntVar()
        self.radiobutton1 = tkinter.Radiobutton(self.mainframe,text='Kyllä',variable=self.radiobuttonvariable,value = 1,indicatoron=0).pack()
        self.radiobutton2 = tkinter.Radiobutton(self.mainframe,text='Ei',variable=self.radiobuttonvariable, value = 2,indicatoron=0).pack(ipadx=5)
        self.label2 = tkinter.Label(self.mainframe,text='Viimeisin käynti:').pack()
        self.e3=tkinter.Entry(self.mainframe)
        self.e3.pack()
        self.okbutton = tkinter.Button(self.mainframe,text='Ok',command=self.quit).pack()
    def quit(self):
        if self.e.get() != '':
            self.nimilista[self.currentitem].set__nimi(self.e.get())

        if self.radiobuttonvariable.get() == 1:
            self.nimilista[self.currentitem].set__osasto('Kyllä')
        if self.radiobuttonvariable.get() == 2:
            self.nimilista[self.currentitem].set__osasto('Ei')
        if self.e3.get() != '':
            self.nimilista[self.currentitem].set__toimi(self.e3.get())
        self.mainframe.destroy()
    def get__mainframeidentity(self):
        return self.mainframe


class uusiasiakas:
    def __init__(self,nimilista):
        self.mainframe = tkinter.Toplevel()
        self.nimilista = nimilista
        self.radiobuttonvariable = tkinter.IntVar()
        self.welcomelabel = tkinter.Label(self.mainframe,text='Lisäät tällähetkellä uutta henkilöä').pack()
        self.label = tkinter.Label(self.mainframe,text='Henkilön nimi').pack()
        self.e=tkinter.Entry(self.mainframe)
        self.e.pack()
        self.label1 = tkinter.Label(self.mainframe,text='Kanta-asiakaskortti?').pack()
        self.radiobutton1 = tkinter.Radiobutton(self.mainframe,text='Kyllä',variable=self.radiobuttonvariable,value = 1,indicatoron=0).pack()
        self.radiobutton2 = tkinter.Radiobutton(self.mainframe,text='Ei',variable=self.radiobuttonvariable, value = 2,indicatoron=0).pack()
        self.label2 = tkinter.Label(self.mainframe,text='Viimeisin käynti:').pack()
        self.e3=tkinter.Entry(self.mainframe)
        self.e3.pack()
        self.okbutton = tkinter.Button(self.mainframe,text='Ok',command=self.quit).pack()

    def quit(self):
        if self.radiobuttonvariable.get() ==1:
            oikeavalinta = 'Kyllä'
        if self.radiobuttonvariable.get() == 2:
            oikeavalinta = 'Ei'
        if self.radiobuttonvariable.get() == 0 or self.e.get() == '':
            pass


        else:
            self.asiakas = asiakkaat.asiakkaat(self.e.get(),oikeavalinta,self.e3.get())
            self.nimilista[self.asiakas.get__nimi()] = self.asiakas
            self.mainframe.destroy()
    def get__mainframeidentity(self):
        return self.mainframe
    def asiakascurrentidentity(self):
        return self.asiakas


class AsiakasGUI:
        def __init__(self,nimilista,frame):
            #Konstruktorimetodi, joka ottaa vastaan attribuutit nimilista ja frame.
            #Nimilista sen takia, että kyseisellä listalla olevia olioita voidaan moduulissa käsitellä.
            #frame taas sisältää tkinter-mainloopin identiteetin.
            self.nimilista = nimilista
            self.mainframe = tkinter.Frame(frame)
            #Tässä käynnistetään tkinter-moduulilla ohjelman käyttöliittymän pääikkuna
            self.tiedotus = tkinter.Label(frame, text='Asiakashallintaohjelmisto 1.0')
            #Luodaan tässä ensin Labeli
            self.paddinglabel = tkinter.Label(frame, text='')
            #Luodaan listboxi, johon conffataan erikseen scrollbar
            self.listbox = tkinter.Listbox(frame)
            self.listbox.bind("<Double-Button-1>", self.showinfo)
            self.listbox.pack(fill = 'x')
            scrollbar = tkinter.Scrollbar(frame)
            scrollbar.pack(side='right', fill='y' )
            #Testaus
            for i in sorted(self.nimilista):
                    self.listbox.insert('end',i)
            #Yhdistetään sitten scrollbar toimimaan listboxin kanssa
            self.listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=self.listbox.yview)
            self.buttoni1 = tkinter.Button(frame, text='Lisää asiakas', command=self.popupnewcustomer).pack(anchor='w',fill = 'x')
            self.buttoni2 = tkinter.Button(frame, text='Muokkaa listalla olevaa asiakasta', command=self.popup).pack(anchor='w', fill = 'x')
            self.buttoni3 = tkinter.Button(frame, text='Poista asiakas', command=self.deletecustomer).pack(anchor='w',fill = 'x')
            self.buttoni4 = tkinter.Button(frame, text='Etsi asiakas', command=self.searchcustomer).pack(anchor='w',fill = 'x')

        def showinfo(self,asdf):
            currentitem =self.listbox.get('active')
            tkinter.messagebox.showinfo(self.nimilista[currentitem].get__nimi(), self.nimilista[currentitem].__str__())
        def popup(self):
            currentitem = self.listbox.get('active')
            if self.nimilista != {}:
                self.nimilistat=popupWindow(self.nimilista,currentitem)
                self.mainframe.wait_window(self.nimilistat.get__mainframeidentity())
                self.listbox.delete(0, 'end')
                for i in self.nimilista:
                    uusinimi =self.nimilista[i].get__nimi()#Sanakirja on luokkaa avain: arvo ---> luupataan avainten nimien läpi ja attribuuteista ulos get__nimi()
                    self.nimilista[uusinimi]=self.nimilista.pop(i) #poistetaan vanha nimi ja lisätään se self.nimilista[uusinimi]-avaimeen
                for key in sorted(self.nimilista):
                    self.listbox.insert('end',key)
            else:
                tkinter.messagebox.showinfo('Virhe', 'Ei nimiä joita muokata!')
        def popupnewcustomer(self):
            self.nimilistar = uusiasiakas(self.nimilista)
            self.mainframe.wait_window(self.nimilistar.get__mainframeidentity())
            self.listbox.delete(0,'end')
            for key in sorted(self.nimilista):
                self.listbox.insert('end',key)
        def deletecustomer(self):
            currentitem = self.listbox.get('active')
            if self.nimilista != {}:
                if tkinter.messagebox.askokcancel('Poista asiakas','Oletko varma että haluat poistaa asiakkaan {0}?'.format(currentitem)):
                    self.listbox.delete(0,'end')
                    del self.nimilista[currentitem]
                    for key in sorted(self.nimilista):
                        self.listbox.insert('end' ,key)
            else:
                tkinter.messagebox.showinfo('Virhe','Ei asiakkaita joita poistaa!')
        def eventhandler(self):
            if tkinter.messagebox.askokcancel('Lopeta?', 'Haluatko lopettaa ja tallentaa muutokset?'):
                dumper.dump(self.nimilista)
                self.mainframe.quit() #Quit pysäyttää suoraan KAIKKI widgetit

        def searchcustomer(self):
            self.inputastringbox = tkinter.Toplevel()
            self.label = tkinter.Label(self.inputastringbox,text="Anna etsimäsi henkilön nimi tai osa siitä:").pack()
            self.entrybox = tkinter.Entry(self.inputastringbox)
            self.entrybox.pack()
            self.okbutton = tkinter.Button(self.inputastringbox,text='Ok',command=self.quit).pack()
        def quit(self):
            if self.entrybox.get() in self.nimilista:
                newdict = {}
                tkinter.messagebox.showinfo('Asiakas löydetty','Löydettiin asiakas: {0}'.format(self.entrybox.get()))
                newdict[self.entrybox.get()] = self.nimilista[self.entrybox.get()]
                del self.nimilista[self.entrybox.get()]
                self.listbox.delete(0,'end')
                self.listbox.insert(0,newdict[self.entrybox.get()].get__nimi())
                for key in sorted(self.nimilista):
                        self.listbox.insert('end' ,key)
                self.listbox.selection_set(first=0)
                self.nimilista[self.entrybox.get()] = newdict[self.entrybox.get()]
            self.inputastringbox.destroy()
        def newlistbox(self,choice):
            if choice == 1:
                dumper.dump(self.nimilista)
                self.nimilista = {}
                a = tkinter.simpledialog.askstring('Anna etsittävän tiedoston nimi', 'Tiedoston nimi:')
                self.nimilista = dumper.specificload(a)
                if self.nimilista == {}:
                    tkinter.messagebox.showinfo('File not found','Specific file not found')
                    self.nimilista = dumper.load()
                self.listbox.delete(0,'end')
                for i in self.nimilista:
                    self.listbox.insert('end',i)
            if choice == 2:
                a = tkinter.simpledialog.askstring('Anna tallennettavan tiedoston nimi','Tiedoston nimi: ')
                dumper.specificdump(self.nimilista,a)
def main():
    nimilista = {}
    nimilista = dumper.load()
    mainwindow = tkinter.Tk()
    mainwindow.wm_title('Asiakashallintaohjelmisto')
    menubar = tkinter.Menu(mainwindow)

    #mainwindow.iconbitmap(default='transparent.ico') keksi uusi ikoni
    asiakasGUI = AsiakasGUI(nimilista,mainwindow)
    menubar.add_command(label='Lataa',command=lambda: asiakasGUI.newlistbox(1))
    menubar.add_command(label='Tallenna',command=lambda: asiakasGUI.newlistbox(2))
    mainwindow.protocol("WM_DELETE_WINDOW",asiakasGUI.eventhandler)
    mainwindow.config(menu=menubar)
    mainwindow.mainloop()
main()
