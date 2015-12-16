__author__ = 'MrTrustworthy'

import uuid
from gol.x_utils import Position


class GameObject(object):

    def __init__(self, position, *args):

        if len(args) > 0:
            raise TypeError("GameObject constructor needs a Tuple as position")

        self.id = uuid.uuid4()
        self.position = Position(position)