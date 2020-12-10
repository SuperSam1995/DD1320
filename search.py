import timeit


class customHashTable:
    def __init__(self, table_len=1000):
        #att välja len 1000 i en tabell med 1 mille eleemnt gör att varje hashtable element har 1000 låtar
        self.table_len = table_len
        list_1 = range(self.table_len)
        self.table = dict(zip(map(str, list_1), [[] for _ in list_1]))
        #börjar med en lista med tomma listor, som sen blir dict
        #viktigt att tablen är tom när man börjar

    def __len__(self):
        return self.table_len

    def generate_key(self, song_obj): #Varje element måste ha en unik key
        key = hash(song_obj.trackId + song_obj.songId) % self.table_len #Hash returnerar en stor random siffra
        return str(key)

    '''
    der är här man ser nyttan av hashtabeller, istället för att söka i en milion låtar så
    vi programmet hitta keyn för låten och söka bland elementen för denna key (som innehåller fler låtar)
    Att skapa en random key istället för en key med exemplvis artist namn är nåt jag valde för att en jämn fördelning 
    på stoleken av elementen i tablellen
    '''

    def insert(self, song_obj):
        k = self.generate_key(song_obj)
        self.table[k].append(song_obj)

    def hashtable_search_artist(self, song_obj):
        k = self.generate_key(song_obj)
        # linear search
        for song in self.table[k]:
            if song.artistName == song_obj.artistName:
                return song.trackId, song.songId, song.artistName, song.songTitle
        return -1
    #Här gör man en vanlig linjär sökningen i en "key" i tabellen

class Song_item:

    def __init__(self, songList, idx=-1):
        # [Track ID, Song ID, Artist Name, Song tile]
        self.trackId = songList[0]
        self.songId = songList[1]
        self.artistName = songList[2]
        self.songTitle = songList[3]
        self.idx = idx
        self.val = int(''.join(map(lambda x: str(ord(x)), self.artistName))) #även detta är mer hjälpsam vi sorting
# ord returnerar ASCII code nummer av strängen, som jag gör sen till ett integer för att kunna hantera lättare
    def __lt__(self, other):
        # comparing str som man gjorde i lab 1 tror jag
        return self.artistName < other.artistName

    def __eq__(self, other): #använder ej denna funktion egentligen men det brukar va bra att ha med när man jämför
        return self.artistName == other.artistName


def readfile(file_n):
    song_objs = []  #Sparar resultaten av readfile

    with open(file_n, 'r', encoding="utf8") as f: #vill ej ändra så 'r' är mer lämplig, encoding för att "matcha" filen
        txt = f.readlines()
    for i, song_str in enumerate(txt): # vi får alltså två element ett nummer för raden och en lista för "låten"
        song_list = song_str.split('<SEP>')
        song_objs.append(Song_item(song_list, i)) # numerering finns egentligen för sorting

    return song_objs


def linear_search(list_s, x):
    for i, song in enumerate(list_s):
        if x == song.artistName:
            return i
    return -1


def binary_search(list_s, x):
    first = 0
    last = len(list_s) - 1

    while first <= last:
        mid = first + (last - first) // 2
        # Check if x is present at mid
        if list_s[mid].artistName == x:
            return mid
            # If x is greater, ignore left half
        elif list_s[mid].artistName < x:
            first = mid + 1
        # If x is smaller, ignore right half
        else:
            last = mid - 1
    # If we reach here, then the element
    # was not present
    return -1


def main():
    filename = "./unique_tracks.txt"
    lista = readfile(filename)

    # we can change the list here
    lista = lista[:500000]

    n = len(lista)
    print("Antal element =", n)
    sista = lista[n - 1]

    testartist = sista.artistName
    # search for the first occurance of artist name
    # Linear

    linjtid = timeit.timeit(stmt=lambda: linear_search(lista, testartist), number=10000)
    print("Linjärsökningen tog (Linear) ", round(linjtid, 4), "sekunder")

    # for binary search
    sorted_list = sorted(lista, key=lambda r: r.artistName)
    binarytid = timeit.timeit(stmt=lambda: binary_search(sorted_list, testartist), number=10000)
    print("Binärsökningen tog (Binary search) ", round(binarytid, 4), "sekunder")

    # for hashtable
    Table = customHashTable(n // 10) #ger ett hashtable med 20k låter i varje element
    for song in lista:
        Table.insert(song)
    print(len(Table))

    tabeltid = timeit.timeit(stmt=lambda: Table.hashtable_search_artist(sista), number=10000)
    print("Hashtablesökningen tog (Hashtable) ", round(tabeltid, 4), "sekunder")


if __name__ == "__main__":
    main()

#### Results ###################
#            |   n=250 000   |   n=500 000   |   n=1000 000   |
# ____________|_______________|_______________|________________|
# Linear     |    82.7019    |    4.1893     |     0.7509     |
# ____________|_______________|_______________|________________|
# Binary     |     0.057     |    0.0532     |     0.0496     |
# ____________|_______________|_______________|________________|
# Hashtable  |     0.0607    |     0.058     |     0.0698     |
# ____________|_______________|_______________|________________|

"""
Hashtable skulle kunna göras snabbare om man ändrar 50 till typ 10 eller nåt
Anledningen att tiden minskar med linjära sökningen är valet av element
om vi letar efter första elementet så blir det snabbt, element "längre ner" tar längre tid

viktigt att tänka på att vi har numer 10 000 vilket innebär att prgrammet genomförs 10k gånger
"""