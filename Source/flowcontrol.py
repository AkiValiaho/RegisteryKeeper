from asiakkaat import *
import dumper

def flowcontrol(choice, nimilista):
    if choice == 2:
        #Tehdään uusi asiakkaat-olio
        asiakas = asiakkaat(input("Input customers name: "),input("Did the customer have a membership card? "), input("Last visit: "))
        if nimilista != None:
            if asiakas.get__nimi() in nimilista:
                    print("Nimilistalla on jo henkilo {0}".format(asiakas.get__nimi()))
                    return nimilista
            else:
                    nimilista[asiakas.get__nimi()] = asiakas
                    return nimilista
    elif choice == 1:
            for i in nimilista:
                print(nimilista[i].__str__())
            return nimilista


    elif choice == 3:
        etsittavanimi = input("Input the name you wish to search for: ")
        for i in nimilista:
            if etsittavanimi in i:
                print("Found customer {0}".format(nimilista[i].get__nimi()))
                choice3 = int(input("Is this the correct person? Press 1 if true else 0"))
                if choice3 == 1:
                    nimilista[i].set__osasto(input("Did the customer have a membership card?: "))
                    nimilista[i].set__toimi(input("Last visit: "))
                elif choice3 == 0:
                    continue
        return nimilista


    elif choice == 4:
        etsittavanimi = input("Input the persons name whose details you wish to remove from the registry ")
        if etsittavanimi in nimilista:
            del nimilista[etsittavanimi]
            return nimilista
        else:
            print("The name you wish to delete from the registry cannot be found.")
            return nimilista
    elif choice == 5:
        dumper.dump(nimilista)
        return False
    elif choice == 6:
        nametosearchfor = input("Input the customers name or parts of it:")
        for i in nimilista:
                if nametosearchfor in i:
                    print(nimilista[i].__str__())
        return nimilista

    #Implementataan dumppaus prosessille ja muutetaan while:n flagiksi false ---> Suljetaan ohjelma ja tallennetaan tiedot tiedostoon
