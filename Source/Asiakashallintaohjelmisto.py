import flowcontrol,dumper,os


def main():
    nimilista = {}
    nimilista = dumper.load()
    while True:
        print("-----------------------------------------------------------------------------")
        print("How to use this program:")
        print("Press 1 to list all the customers")
        print("Press 2 to add a customer to the list")
        print("Press 3 to modify customers data in the registry")
        print("Press 4 to remove customers data from the registry")
        print("Press 5 to close the program and save the data")
        print("Press 6 to search for a customer")
        choice = int(input("Input your choice: "))
        os.system('cls')
        print("-----------------------------------------------------------------------------")
        nimilista = flowcontrol.flowcontrol(choice, nimilista) #Flowcontrolli palauttaa nimilistaa

        if nimilista == False:
            break
main()
