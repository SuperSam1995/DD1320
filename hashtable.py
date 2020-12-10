from pokemon import Pokemon, read_pokemons
from math import sqrt


## DictHash
class DictHash:
    def __init__(self):
        self.Table = {}
        #Skapar min dictionary

    def store(self, nyckel, data):
        self.Table.update({nyckel: data})
    #update innebär att jag ej behöver en size för min dictionary då update increases the size of elements

    def search(self, nyckel):
        return self.Table[nyckel]
    #returnerar value

    def __getitem__(self, nyckel):
        return self.search(nyckel)
    #getitem skulle funka precis som search, så man kan return self.Table[nyckel] här också

    def __contains__(self, nyckel):
        return nyckel in self.Table.keys()
    #True eller False
    #Kollar alltså om key finns bland keys listan

class Node:
    """Nodes for the class Hashtable """

    def __init__(self, key="", data=None):
        """key: The key used in hashing
        data: The object which shall hashes in"""
        self.key = key
        self.data = data
    # ^ givet



class Hashtable:
    def __init__(self, size):
        """size: hash tables size"""

        self.size = int(size) * 2
        self.table = [[] for _ in range(self.size)]

        #skapar en stor lista med en tom lista inuti för varje element
        '''
        en dict can se så här ut  {key1: value1 , key2:value2} men lista är[[value1],[value2]]
        så vi skapar en funktion f som gör följande typ: f(key1) ==> 0, f(key2) ==> 1 
        på så sätt så "lagrar" min lista båda key och value samtidigt med hjälp av lista egenskaper
        f funktionen är alltså min hashfunction
        '''







    def store(self, key, data):
        """key: key
        data: object to be saved
        puts in "data" with key "key" in table."""
        index = self.hashfunction(key)

        # test if a key already exit:
        added = False
        for n in self.table[index]:
            if key == n.key:
                n.data = data
                added = True
                #Detta gjordes för att klara första inmattningen på kattis
        if not (added): self.table[index].append(Node(key, data))



    def search(self, key):
        """key: key
        brings object saved with key "key" and returns it.
        if "key" doesn't exist , get an Exception, KeyError """

        index = self.hashfunction(key)
        for n in self.table[index]:
            if key == n.key:
                return n.data
        raise KeyError("This Key cannot be found")


    def hashfunction(self, key):
        """key: key
        calculates hashfunktion for key"""

        return (int(''.join(map(lambda x: str(ord(x)), key))) * 3) % self.size
            #hash(str(key)) % self.size
        #Detta kommer alltid att vara mindre än size

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        try:
            _ = self.search(key)
            return True
        except KeyError:
            return False

    def measure_distrbution(self):
        # std, len of every entry
        elements_lengths = []
        for element in self.table:
            elements_lengths.append(len(element))
        # standard deviation = root_square(sum(element - average)**2/number of element)
        mean = sum(elements_lengths) / float(len(elements_lengths))
        sum_ = 0.0
        for element_len in elements_lengths:
            sum_ += (element_len - mean) ** 2
        print("std of the lenghts of the lists (lower value means good distrbution):")
        print(sqrt(sum_ / self.size))
        #print("Collosions per each Entry")
        #print([x - 1 for x in elements_lengths])


if __name__ == "__main__":

    file_name = "pokemon.csv"
    D_Hash = DictHash()
    All_pokemons = read_pokemons(file_name)
    Htable = Hashtable(800)
    #typ 700 pokemon alltså 70 pokemon per list
    for p in All_pokemons:
        D_Hash.store(p["Name"], p)
        Htable.store(p["Name"], p)

    p_test = All_pokemons[10]
    #Searchar för den 10:e pokemon
    print(D_Hash.search(p_test["Name"]).AllAtr)

    # Test for the collisions:
    Htable.measure_distrbution()

