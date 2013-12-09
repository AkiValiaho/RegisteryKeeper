import pickle

def dumpdictionary(osoitteet):
    with open('osoitteet.dat','wb') as file: #We dump the dictionary with wb mode to overwrite it
        pickle.dump(osoitteet,file)

def loaddictionary():
    try:
        with open('osoitteet.dat','rb') as file:
            osoitteet =pickle.load(file)
            if osoitteet == None:
                return {}
            return osoitteet
    except IOError:
        return {}
    except EOFError:
        return {}
