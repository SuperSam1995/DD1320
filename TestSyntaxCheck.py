from linkedQfile import LinkedQ
from SyntaxCheck import readformel, Syntaxfel
import unittest


###############################
# Unit Tests
###############################
class TestSyntax(unittest.TestCase):

    def test_true_molcules(self):
        print("**********Right Formel Tests***********")
        test_data = make_true_formel()
        for mol, _ in test_data:
            try:
                q = readformel(mol)
                v = q.dequeue()
                if v.value != "$":
                    self.fail("No True Confirmation statment found!")
            except Syntaxfel:
                self.fail("Syntaxfel has been raised unexpectadly!")
            except:
                self.fail("Other Error has been raised unexpectadly!")


##########################################
def make_true_formel():
    mols = ["Na", "H2O", "Si(C3(COOH)2)4(H2O)7", "Na332"]
    results = ["Formeln är syntaktiskt korrekt" for _ in mols]
    return zip(mols, results)


def make_false_formel():
    mols = ["C(Xx4)5", "C(OH4)C", "C(OH4C", "H2O)Fe", "H0", "H1C",
            "H02C", "Nacl", "a", "(Cl)2)3", ")", "2"]
    results = ["Okänd atom vid radslutet 4)5",
               "Saknad siffra vid radslutet C",
               "Saknad högerparentes vid radslutet ",
               "Felaktig gruppstart vid radslutet )Fe",
               "För litet tal vid radslutet ",
               "För litet tal vid radslutet C",
               "För litet tal vid radslutet 2C",
               "Saknad stor bokstav vid radslutet cl",
               "Saknad stor bokstav vid radslutet a",
               "Felaktig gruppstart vid radslutet )3",
               "Felaktig gruppstart vid radslutet )",
               "Felaktig gruppstart vid radslutet 2"]
    return zip(mols, results)


def main_err_tests():
    test_data = make_false_formel()
    passed = False
    for mol, expect_res in test_data:
        try:
            _ = readformel(mol)
            passed = True
        except Syntaxfel as e:
            if e.message == expect_res:
                print("Test is passed!")
            else:
                print("Wrong message content for Syntaxfel Exception")
                print("For " + mol)
                print("Got: " + e.message)
                print("Expected: " + expect_res)
        if passed:
            # error, it shouldn't
            passed = False
            print("The wrong formel " + mol + " is not detected.")


if __name__ == "__main__":
    print("**********Wrong Formel Tests***********")
    main_err_tests()
    unittest.main()