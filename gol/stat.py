__author__ = 'MrTrustworthy'


class Stat:
    """
    Stat
    """

    def __init__(self, *args):

        if len(args) == 3:
            self.min = args[0]
            self.max = args[1]
            self.val = args[2]
        elif len(args) == 2:
            self.min = args[0]
            self.max = args[1]
            self.val = self.max
        elif len(args) == 1:
            self.min = 0
            self.max = args[0]
            self.val = self.max

    def sub(self, amount, strict=False):
        if strict and self.val < amount:
            raise ValueError("Not enough to subtract", amount)
        self.val -= amount

    def add(self, amount, force=False):
        self.val += amount
        if self.val > self.max and not force:
            self.val = self.max

    def is_below(self):
        return self.val < self.min


if __name__ == "__main__":
    s = Stat(2)
    print("stat:", s)
