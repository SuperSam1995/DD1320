import csv

class Pokemon():

    def __init__(self,Name,Type1,Type2,
                Total ,HP, Attack, Defense,Sp_Atk, Sp_Def,Speed,
                Generation, Legendary):


        self.AllAtr = {
            "Name":Name,               "Type1":Type1 ,      "Type2":Type2                ,"Total":int(Total),
            "HP":int(HP),              "Attack":int(Attack),"Defense": int(Defense)      ,"Sp_Atk": int(Sp_Atk),
            "Sp_Def":int(Sp_Def),      "Speed": int(Speed), "Generation": int(Generation),
            "Legendary":("T" in Legendary.upper())
        }

        """
        self.Name = Name
        self.Type1 = Type1
        self.Type2 = Type2
        self.Total = Total
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.Sp_Atk = Sp_Atk
        self.Sp_Def = Sp_Def
        self.Speed = Speed
        self.Generation = Generation
        self.Legendary = Legendary
        """
    def __str__(self):
        str_ = ["Propierties of the Pokemon: "+self.AllAtr["Name"],
                "============================================="]
        for label,value in zip(self.AllAtr.keys(),self.AllAtr.values()):
            str_.append("\t".join(["{:12s}".format(label),str(value)]))
        return "\n".join(str_)

    def __getitem__(self,name):
        return self.AllAtr[name]

    def __setitem__(self,name, value):
        self.AllAtr[name] = value



    def __lt__(self,OtherPoke):
        return self.Calculate_power_def(OtherPoke) <0
    def __le__(self,OtherPoke):
        return self.Calculate_power_def(OtherPoke) <=0
    def __eq__(self, OtherPoke):
        return self.Calculate_power_def(OtherPoke) ==0
    def __ne__(self, OtherPoke):
        return self.Calculate_power_def(OtherPoke) !=0
    def __gt__(self, OtherPoke):
        return self.Calculate_power_def(OtherPoke) >0
    def __ge__(self, OtherPoke):
        return self.Calculate_power_def(OtherPoke) >=0


    def Calculate_power_def(self, OtherPoke_):
        return self["Total"] - OtherPoke_["Total"]

def create_pokemon():
    print("Please enter your pokemon attribute as requested:")
    AttrList = [
            "Name","Type1","Type2","Total","HP","Attack","Defense","Sp_Atk",
            "Sp_Def","Speed", "Generation","Legendary(True/False)"]
    PokemonList = []
    for Atr in AttrList:
        PokemonList.append(input("{:12s}".format(Atr)+"\t: "))
    result = Pokemon(*PokemonList)
    print("Done, your pokemon is created")
    return result


file_name = "pokemon.csv"
def read_pokemons(filename):
    with open(file_name,newline="") as f:
        pokemons_gen = csv.reader(f)
        All_Pokemons = []
        _ = pokemons_gen.__next__()
        for poke in pokemons_gen:
            All_Pokemons.append(Pokemon(*poke[1:]))
    return All_Pokemons

def search_for_a_pokemon(Pokemons_list):
    print("Please enter an attribute or more for the Pokemon you search for:")
    print("Just press enter for undefinded attributes")
    AttrList = [
            "Name","Type1","Type2","Total","HP","Attack","Defense","Sp_Atk",
            "Sp_Def","Speed", "Generation","Legendary"]

    PokemonList = []
    for Atr in AttrList:
        PokemonList.append(input("{:12s}".format(Atr)+"\t: "))
    Some_Attrs = []
    for k,v in zip(AttrList,PokemonList):
        if v:Some_Attrs.append((k,v))
    result = []
    for pokem in Pokemons_list:
        if all([str(pokem[attr]).lower()==a_value.lower() for attr,a_value in Some_Attrs]) and Some_Attrs:
            result.append(pokem)
    if result:
        return result
    else:
        print("No Pokemon with this attributes")
        return []

if __name__ == "__main__":
    AllPokemons = read_pokemons(file_name)
    r = search_for_a_pokemon(AllPokemons)

    for p in r:
        print(p)
        print("**********************")