class Syntaxfel(Exception):

    def __init__(self,message):
        self.message = message

def isNum(x):
    if len(x) >=1:
        utskrift = x.replace(x[0], '')

    x = str(x)
    try:

        n = int(x)
        if x[0] == '0': raise Syntaxfel("För litet tal vid radslutet " + utskrift)
        if n < 2: raise Syntaxfel("För litet tal vid radslutet " )
    except ValueError:
        # Not number or Nothing
        pass #Do nothing

def is_smallLetter(x):
    y = ord(x)
    if (ord('a') > y) or (y> ord('z')):
        # not a small letter
        # undescribed state: HH
        raise Syntaxfel

def is_capitalLetter(x , atom_name):
    y = ord(x)
    if (ord('A') > y) or (y> ord('Z')):
        raise Syntaxfel("Saknad stor bokstav vid radslutet "+atom_name)

def is_atom(x,atom_name):
    # 1
    if len(x)==1:
        is_capitalLetter(x, atom_name)
    elif len(x)==2:
        is_capitalLetter(x[0],atom_name)
        is_smallLetter(x[1])
    elif len(x)==0:
        raise Syntaxfel("Saknad stor bokstav vid radslutet "+atom_name)
    else:
        is_capitalLetter(x[0], atom_name)
        is_smallLetter(x[1])
        # more letters aotms
        pass

def is_molecule(x):
    # sepearte the two parts
    atom , num = '', ''
    for k in x:
        if k in '0123456789':
            num += k
        else:
            if num=='':
                atom += k
    # test the atom part
    is_atom(atom, x)
    # then test the num part

    isNum(num)

    print("Formeln är syntaktiskt korrekt")