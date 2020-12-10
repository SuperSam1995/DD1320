from BST import *
from linkedQfile import LinkedQ
import sys

global Alphabet
Alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
Alphabet.extend(['å', 'ö', 'ä'])


class ParentNode: #Difinerar parentNode klassen enligt instruktioner
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent


def makechildren(word_obj, words_tree):
    global Alphabet
    result = [word_obj]
    word = word_obj.word
    for letter_place in range(3):
        word_c = list(word)
        for letter in Alphabet:
            word_c[letter_place] = letter
            word_r = ''.join(word_c)
            if word_r in words_tree:
                result.append(ParentNode(word_r, word_obj)) #Word-obj är fadern och word-r är ordet
    return result


def writechain(word_obj):
    # recrusive
    result = [word_obj.word]
    if word_obj.parent: #sträng
        result = writechain(word_obj.parent) + result #Vi adderar result så att det kan printa sista ordet
    return result


def main():

    ## Build the Words Tree
    svenska = Bintree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()  # One three letter word per row
            if ordet not in svenska:
                svenska.put(ordet)  # in the searchtree

    ## Ask for start and end words

    start_word = input("Please Enter the Start Word: ")
    end_word = input("Please Enter the End Word: ")

    ## Second Version: call makechildren and print in a loop
    start_word_obj = ParentNode(start_word)
    children = LinkedQ([start_word_obj])

    gamla = Bintree()

    while not children.isEmpty():
        node = children.dequeue()
        new_children = makechildren(node, svenska)
        for child in new_children:
            if child.word == end_word:
                msg = "Det finns en väg till "+end_word
                msg += "\nThe solution is: " + " ".join(writechain(child))
                print('\n')
                print(msg)
                sys.exit()
            if child.word not in gamla:
                children.enqueue(child)
                gamla.put(child.word)
    print('\n')
    print("Det finns ingen väg till " + end_word)
main()