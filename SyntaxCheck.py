from linkedQfile import LinkedQ


class Syntaxfel(Exception):

    def __init__(self, message):
        self.message = message


def readformel(mol):
    # Heighest level
    que = LinkedQ(list(mol) + ['$'])
    # $ representerar att molekylen tog slut
    next_tecken = que.peek()
    while next_tecken.value != '$':
        que = readmol(que)
        next_tecken = que.peek()
    return que


def readmol(que):
    # separate the two parts

    que = readatom(que)
    current_t = que.peek()
    if (current_t.value in '0123456789'):
        que = isNum(que)
    # if not the end , then test for group:
    next_t = que.peek()
    # is there any additional molecules
    while True:

        if (next_t.value >= 'A') and (next_t.value <= 'Z'):
            que = readmol(que)
        elif next_t.value == '(':
            que = readgroup(que)
        else:
            break
        next_t = que.peek()
    return que


def readgroup(que):
    n_t = que.peek()
    if n_t.value == '(':

        _ = que.dequeue()
        que = readmol(que)
        n_t = que.peek()
        if n_t.value != ')':
            # raise error
            raise Syntaxfel("Saknad högerparentes vid radslutet %s" % show_rest(n_t))
        else:
            _ = que.dequeue()
        # there should be a number
        n_t = que.peek()
        if n_t.value in '0123456789':
            que = isNum(que)
        else:
            raise Syntaxfel("Saknad siffra vid radslutet %s" % show_rest(n_t))
    else:
        # not a group
        pass
    return que


def show_rest(x):
    s = ''
    while x.value != '$':
        s += x.value
        x = x.next
    return s


def isNum(que):
    # match
    current_t = que.dequeue()
    # the first must not be zero
    if current_t.value == '0':
        raise Syntaxfel("För litet tal vid radslutet %s" % show_rest(current_t.next))
    go_on = True
    num = current_t.value
    while go_on:
        try:
            n_t = que.peek()
            _ = int(n_t.value)
            num += n_t.value
            _ = que.dequeue()
        except ValueError:
            go_on = False
    if int(num) < 2:
        raise Syntaxfel("För litet tal vid radslutet %s" % show_rest(current_t.next))
    return que


def readatom(que):
    # test if small letter capital --> ecxp
    atoms = load_atoms()
    n_t = que.peek()
    if (n_t.value >= 'a') and (n_t.value <= 'z'):
        # first small letter
        raise Syntaxfel("Saknad stor bokstav vid radslutet %s" % show_rest(n_t))
    elif n_t.value == '(':
        # treat as group
        return que #return and treat it as a group
    elif (n_t.value >= 'A') and (n_t.value <= 'Z'):
        current_t = que.dequeue()
        n_t_ = que.peek()
        atom = current_t.value
        if (n_t_.value >= 'a') and (n_t_.value <= 'z'):
            # second small letter
            atom = current_t.value + n_t_.value
            _ = que.dequeue()
            if atom not in atoms:
                raise Syntaxfel("Okänd atom vid radslutet %s" % show_rest(n_t_.next))
        if atom in atoms:
            # only big letter
            return que
        else:
            # Not known element
            raise Syntaxfel("Okänd atom vid radslutet %s" % show_rest(n_t_))
    else:
        # not a letter or parenthesis
        raise Syntaxfel("Felaktig gruppstart vid radslutet %s" % show_rest(n_t))


def load_atoms():
    atoms = """
    H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn
    Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd
    In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu 
    Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am
    Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv
    """.split()

    return [x.strip() for x in atoms]