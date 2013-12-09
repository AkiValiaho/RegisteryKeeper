from dumper import dumpdictionary,loaddictionary
from henkilo import henkilo

def main():
    listofnames = loaddictionary()
    while True:
        file = 'thefile.txt'
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
                print(listofnames[i].__str__())
        elif valinta == 3:
            sname = input("Input the name you wish to search for.")
            if sname in listofnames:
                print("Found info for {0}".format(sname))
                print("Number: {0}, Address: {1}".format(listofnames[sname].get_puhelinnumero(), listofnames[sname].get_osoite()))
            else:
                print("The name was not found")
        elif valinta == 4:
            sname = input("Input name of a person whose details you would like to change")
            if sname in listofnames:
                listofnames[sname].set_osoite(input("Input the persons new address"))


main()


