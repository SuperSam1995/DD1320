from SyntaxCheck import readformel, Syntaxfel #is_molecule, Syntaxfel

def main(input_str):
    #global current_t
    #current_t = input_str_que.dequeue()
    output_str_que =readformel(input_str)
    current_t = output_str_que.dequeue()
    if current_t.value == "$": #end of input code.
        print("Formeln är syntaktiskt korrekt")

if __name__ == "__main__":
    mol = input()
    while mol!="#":
        try:
            main(mol)
        except Syntaxfel as e:
            print(e.message)
        mol = input()

