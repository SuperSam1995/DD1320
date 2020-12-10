from array import array


class ArrayQ():

    def __init__(self, data_type='i', list_=[]):
        self.__queue__ = array(data_type, list_)

    def get_queue(self):
        return self.__queue__

    def set_queue(self, list_):
        self.__queue__ = array(self.__queue__.typecode, list_)

    def enqueue(self, n):
        # FIFO
        self.__queue__.append(n)

    def dequeue(self):
        return self.__queue__.pop(0)

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.__queue__)


class ListQ():

    def __init__(self, list_=[]):
        self.__queue__ = list_

    def get_queue(self):
        return self.__queue__

    def set_queue(self, list_):
        self.__queue__ = list_

    def enqueue(self, n):
        # FIFO
        self.__queue__.append(n)

    def dequeue(self):
        return self.__queue__.pop(0)

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.__queue__)