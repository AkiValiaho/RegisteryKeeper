from AsiakasGUI import *
import dumper

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
