from arrayQfile import ArrayQ
from molgrafik import Ruta


class Node():
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class LinkedQ(ArrayQ):

    def __init__(self, list_=[]):
        super(LinkedQ, self).__init__(list_)
        last_node = 0
        self.NodesList = []
        for node_e in list_:
            node = Node(node_e)
            if last_node:
                last_node.next = node
                self.NodesList.append(last_node)
            # super(LinkedQ,self).enqueue(node.value)
            last_node = node
        if last_node != 0:
            self.NodesList.append(last_node)
            self.first = self.NodesList[0]
            self.last = self.NodesList[-1]

        self.draw_mol = Ruta()
        self.removed = ''

    def enqueue(self, n):
        super(LinkedQ, self).enqueue(n)
        n_ = Node(n)
        # print(self.NodesList)
        # maybe empty
        if self.NodesList: self.NodesList[-1].next = n_
        self.NodesList.append(n_)
        self.last = n_

    def dequeue(self):
        R = super(LinkedQ, self).dequeue()
        self.removed += R  # for strings now

        if len(self.NodesList) > 1:
            self.first = self.NodesList[1]
        else:
            self.first = None;
            self.last = None
        # print("***********",n)
        if len(self.NodesList) != 0:
            n = self.NodesList.pop(0)
        return n

    def peek(self):
        if self.first:
            return self.first
        else:
            return None
