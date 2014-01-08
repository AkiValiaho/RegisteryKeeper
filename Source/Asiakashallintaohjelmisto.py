import flowcontrol,dumper,os
from AsiakasGUI import AsiakasGUI
#Tässä kaikki importit

def main():
    asiakasgui = AsiakasGUI()
    nimilista = {}
    nimilista = dumper.load()
    flag1 = True
    while flag1 == True:
        flag2 = True
        print("-----------------------------------------------------------------------------")
        print("How to use this program:")
        print("Press 1 to list all the customers")
        print("Press 2 to add a customer to the list")
        print("Press 3 to modify customers data in the registry")
        print("Press 4 to remove customers data from the registry")
        print("Press 5 to close the program and save the data")
        print("Press 6 to search for a customer")
        while flag2 == True:
            try:
                choice = int(input("Input your choice: "))
                if choice < 1 or choice > 6:
                    raise ValueError

                flag2 = False
            except ValueError:
                print("Your choice made no sense")
                print("Please try again")
                continue

        os.system('cls')
        print("-----------------------------------------------------------------------------")
        nimilista = flowcontrol.flowcontrol(choice, nimilista) #Flowcontrolli palauttaa nimilistaa

        if nimilista == False:
            flag1 = False
    print("Ending program")

main()
