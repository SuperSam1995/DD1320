class ArrayQ:

    def __init__(self, list_=None):
        if list_ is None:
            list_ = []
        self.__queue__ = list_

    def get_queue(self):
        return self.__queue__

    def set_queue(self, list_):
        self.__queue__ = list_

    def enqueue(self, n):
        #Stoppa in x sist i kön
        # FIFO
        self.__queue__.append(n)

    def dequeue(self):
        #-	X = dequeue(): plocka ut och returnera det som står först i kön.
        return self.__queue__.pop(0)

    def isEmpty(self):
        #-	isEmpty(): Undersök om kön är tom
        return self.size() == 0

    def size(self):
        #undersö storleken på kön
        return len(self.__queue__)


class Vertices:
    def __init__(self, n=0, m=0, c=None):
        # n is order of vertices
        # m is number of marbles
        # c is the children index list
        self.p = -1
        if c is None:
            c = []
        self.n = n
        self.m = m
        # inx is less by one:
        self.c = [x - 1 for x in c]

    def set_parent(self, x):
        if len(x):
            self.p = x[0]
        else:
            pass

    def is_leaf(self):
        if self.p != -1:  # not root
            return not (bool(len(self.c)))
        else:
            return False


def main():
    x = int(input())
    while x:
        tree = [[] for _ in range(x)]
        Parents = tree[:]
        for _ in range(x):
            mm = input().split()
            me = [int(a) for a in mm]
            m = Vertices(me[0] - 1, me[1], me[3:])
            for c in m.c:
                Parents[c].append(m.n)
            tree[m.n] = m
        que = ArrayQ()

        for vrt in tree:
            vrt.set_parent(Parents[vrt.n])
            tree[vrt.n] = vrt
            if vrt.is_leaf():
                que.enqueue(vrt)
        r = 0
        while que.size():
            leaf = que.dequeue()
            moves = leaf.m - 1
            tree[leaf.p].m += moves
            # add moves here
            r += abs(moves)
            tree[leaf.p].c.remove(leaf.n)
            if tree[leaf.p].is_leaf():
                que.enqueue(tree[leaf.p])
        print(r)
        x = int(input())


if __name__ == "__main__":
    main()