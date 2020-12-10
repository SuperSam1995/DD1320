from linkedQfile import LinkedQ
from SyntaxCheck import is_molecule, Syntaxfel
import unittest


###############################
# Tests
###############################
class TestSyntax(unittest.TestCase):

    def test_err_molcules(self):
        print("Test the error cases in the examples")
        outputs, mols = make_test_molcules("Nonmols")
        for i, mol in enumerate(mols):
            Char_ = mol.peek()
            r = ''
            while Char_:
                r += chr(Char_.value)
                Char_ = Char_.next
            self.assertRaises(Syntaxfel, is_molecule, r)
            try:
                is_molecule(r)
            except Syntaxfel as e:
                self.assertEqual(outputs[i], e.message)

    def test_true_molcules(self):
        print("Test the right cases which makes no expenstions")
        _, mols = make_test_molcules("mols")
        for mol in mols:
            Char_ = mol.peek()
            r = ''
            while Char_:
                r += chr(Char_.value)
                Char_ = Char_.next
            try:
                is_molecule(r)
            except Syntaxfel:
                self.fail("Syntaxfel has been raised unexpectadly!")


##########################################

def make_test_molcules(ind):
    ## Test Cases
    # en 0:  formeln har en korrekt syntax
    # en 1: saknad storbokstav vid radslutet
    # en 2: för litet tal vid radslutet
    answers = ["Formeln är syntaktiskt korrekt",
               "Saknad stor bokstav vid radslutet",
               "För litet tal vid radslutet"]

    result = []

    if ind == "Nonmols":
        Molcules = """a
        cr12
        8
        Cr0 
        Pb1"""
        result = [answers[1], answers[1], answers[1], answers[2], answers[2]]
    else:
        Molcules = """H2
        P21
        Ag3
        Fe12
        Xx5"""

    Mols_list = Molcules.split('\n')
    #############
    if ind == "Nonmols":
        for i in range(3):
            result[i] = result[i] + " " + Mols_list[i].strip()
    ############
    # Turn to linked qeues:
    Mols_qeues = []
    for mol in Mols_list:
        Mols_qeues.append(LinkedQ('i', list(map(ord, mol.strip()))))

    return result, Mols_qeues


if __name__ == "__main__":
    unittest.main()