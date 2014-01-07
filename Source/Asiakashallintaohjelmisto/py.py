from dumper import dumpdictionary,loaddictionary
from henkilo import henkilo

def main():
    while True:
        file = 'thefile.txt'
        listofnames = loaddictionary()
        if listofnames == False:
            print("No names on your list, would you like to add?")
        print("Press 1 to add a name to the list")
        valinta = int(input("Input your choice:"))
        if valinta == 1:
            henkilo1 = henkilo(input('Input the name'), input('Input address'), input('Input tel.'))
            listofnames[henkilo1.get_name()] = henkilo1
            dumpdictionary(listofnames)
        elif valinta == 2:
            for i in listofnames:
                print(i.__str__())
        elif valinta == 3:
            pass

main()


