__author__ = 'MrTrustworthy'

import uuid
import random


class Amap:
    def __init__(self, size=(10, 10)):
        self.size = size

    def __repr__(self):
        return "#Map" + str(self.size)

    def __str__(self):
        return self.__repr__()






if __name__ == "__main__":
    g = Amap()
    print(g)
