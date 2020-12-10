# Python program to demonstrate insert operation in binary search tree

# A utility class that represents an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        # This is added to work with LAB4
        self.next_ = None

    def set_dir(self, direc, value):
        if direc == "right":
            self.right = value
        elif direc == "left":
            self.left = value
        else:
            self = value

    def get_dir(self, direc=""):
        if direc == "right":
            return self.right
        elif direc == "left":
            return self.left
        else:
            return self


class Bintree:

    def __init__(self):
        self.root = None

    def put(self, newvalue):
        # Sorts in newvalue in the tree (in place)
        if newvalue not in self:
            self.root = putta(self.root, "", Node(newvalue))

    def __contains__(self, value):
        # True if value is in the tree, False itherwise
        return None != finns(self.root, value)

    def write(self):
        # writes tree in order
        skriv(self.root)
        print("\n")


# A utility function to insert a new node with the given key

def putta(rootU, dirc, node):
    if dirc:
        root = rootU.get_dir(dirc)
    else:
        root = rootU

    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                root = putta(root, "right", node)
        else:
            if root.left is None:
                root.left = node
            else:
                root = putta(root, "left", node)

    if dirc:
        rootU.set_dir(dirc, root)
    else:
        rootU = root
    return rootU


# A utility function to do inorder tree traversal
def skriv(root):
    if root:
        skriv(root.left)
        print(root.val)
        skriv(root.right)

    # Driver program to test the above functions


# This code is contributed by Bhavya Jain

# A utility function to search a given key in BST
def finns(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

        # Key is greater than root's key
    if root.val < key:
        return finns(root.right, key)

        # Key is smaller than root's key
    return finns(root.left, key)


if __name__ == "__main__":
    btree = Bintree()

    btree.put("Aooo")
    btree.put("zoo")
    btree.put("zoo")
    btree.put("Zoo")
    btree.write()
    ## Second
    svenska = Bintree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()  # One trhee letter word per row
            if ordet in svenska:
                print(ordet, end=" ")
            else:
                svenska.put(ordet)  # in the searchtree
    print("\n")

    ## Third
    EnglishTree = Bintree()
    with open("engelska.txt", "r", encoding="utf-8") as Enfil:
        for rad in Enfil:
            for ordet in rad.split():
                if ordet not in EnglishTree:
                    EnglishTree.put(ordet)  # in the searchtree
                    if ordet in svenska:
                        print(ordet, end=" ")
    print("\n")
    # EnglishTree.write()
