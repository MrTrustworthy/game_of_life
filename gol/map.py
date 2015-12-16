__author__ = 'MrTrustworthy'


class Map:
    def __init__(self, *args):

        if len(args) == 1:
            size_x, size_y = args[0]
        elif len(args) == 2:
            size_x = args[0]
            size_y = args[1]
        else:
            raise ValueError("Map needs a size (tuple or 2 integers) to initialize")


        self.size_x = size_x
        self.size_y = size_y
        self.objects = []

    def _split(self, size):
        pass
        # need circle-rect intersection check here
