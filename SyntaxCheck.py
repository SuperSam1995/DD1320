from linkedQfile import LinkedQ
from molgrafik import Ruta


# Linked list modified to add Ruta as attribute (draw_mol)
# so , it's treated with the same input.

class Syntaxfel(Exception):

    def __init__(self, message):
        self.message = message


def readformel(mol):
    # general function?
    que = LinkedQ(list(mol) + ['$'])
    n_t = que.peek()
    R = []
    while n_t.value != '$':
        que = readmol(que)
        c_draw = que.draw_mol
        while c_draw.next:
            # så länge det existerar wn c_draw.next appenda till R och ta nästa tecken
            R.append(c_draw)
            c_draw = c_draw.next
        R.append(c_draw) #adderar sista elemntet alltså
        n_t = que.peek()



    # Build the drawing object
    last_sq = R[-1]
    for m in R[-2::-1]:
        m.next = last_sq
        last_sq = m
        #relänkar min formel
    que.draw_mol = last_sq

    return que


def readmol(que):
    # sepearte the two parts

    que = readatom(que)
    ##############
    Sq = Ruta()
    Sq.atom = que.removed
    que.removed = ''
    ##############
    current_t = que.peek()
    if (current_t.value in '0123456789'):
        que = isNum(que)
        Sq.num = int(que.removed)
        que.removed = ''
    # if not the end , then test for group:
    next_t = que.peek()
    # is there additional mols
    All_next_groups = [Sq]
    while True:
        if (next_t.value >= 'A') and (next_t.value <= 'Z'):
            que = readmol(que)
            ### NEXT
            All_next_groups.append(que.draw_mol)


        elif next_t.value == '(':
            que = readgroup(que)
            # just in case there wasn't atom at the start.
            # only a group
            if All_next_groups[0].atom:
                All_next_groups.append(que.draw_mol)
            else:
                All_next_groups[0] = que.draw_mol
                # Sq.next = que.draw_mol
                # que.draw_mol = Sq
        elif next_t.value in ')$':
            # called from group or only atom
            # que.draw_mol = Sq
            break
        else:
            break

        next_t = que.peek()
        # Sq = que.draw_mol

    # form draw mol: Same logic as above:
    last_sq = All_next_groups[-1]
    for m in All_next_groups[-2::-1]:
        m.next = last_sq
        last_sq = m
    que.draw_mol = last_sq

    return que


def readgroup(que):
    n_t = que.peek()
    if n_t.value == '(':
        #
        _ = que.dequeue()
        Sq = Ruta(atom="( )")

        que.removed = ''
        que = readmol(que)
        Sq.down = que.draw_mol

        n_t = que.peek()
        if n_t.value != ')':
            # raise error
            raise Syntaxfel("Saknad högerparentes vid radslutet %s" % show_rest(n_t))
        else:
            _ = que.dequeue()
        # there should be a number
        n_t = que.peek()
        if n_t.value in '0123456789':
            que.removed = ''
            que = isNum(que)
            Sq.num = int(que.removed)
            que.removed = ''
        else:
            raise Syntaxfel("Saknad siffra vid radslutet %s" % show_rest(n_t))
    else:
        # not a group
        pass
    que.draw_mol = Sq
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
        return que
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
        # not a letter or parthese
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