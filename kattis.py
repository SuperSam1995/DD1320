from SyntaxCheck import readformel, Syntaxfel #is_molecule, Syntaxfel
from molgrafik import Molgrafik
from mol_weight import weight

def main(input_str):

    output_str_que =readformel(input_str)
    current_t = output_str_que.dequeue()
    if current_t.value == "$": #end of input code.
        print("Formeln är syntaktiskt korrekt")
    print("The weights is: %s"%(weight(output_str_que.draw_mol)))
    return output_str_que.draw_mol


if __name__ == "__main__":
    print("Enter the molcues (# to end) ")
    print("Molecule: ",end='')
    mol = input()
    mg = Molgrafik()
    while mol!="#":
        try:
            mol_graph = main(mol)

            mg.show(mol_graph)
            mg.mainloop()
        except Syntaxfel as e:
            print(e.message)
        mol = input()
