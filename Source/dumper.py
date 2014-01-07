import pickle


def dump(nimilista):
    with open("nimet.txt","wb") as file:
        pickle.dump(nimilista,file)
def load():
    nimilista = {}
    try:
        with open("nimet.txt","rb") as file:
            nimilista = pickle.load(file)
            if nimilista == None:
                return {}
            else:
                return nimilista
    except IOError:
        return {}
    except EOFError:
        return {}
