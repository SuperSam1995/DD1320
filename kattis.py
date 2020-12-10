from SyntaxCheck import is_molecule, Syntaxfel


mol = input()

while mol!="#":
    try:
        is_molecule(mol)
    except Syntaxfel as e:
        print(e.message)
    mol = input()