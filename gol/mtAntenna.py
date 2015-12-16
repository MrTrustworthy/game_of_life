__author__ = 'MrTrustworthy'

import inspect


class Antenna:
    def __init__(self):
        self.listeners = {}

    def add_listener(self, channel, callback):

        if len(inspect.signature(callback).parameters) == 0:
            raise TypeError("Callback Function needs at least 1 parameter")

        if channel not in self.listeners.keys():
            self.listeners[channel] = []

        self.listeners[channel].append(callback)

    def remove_listener(self, channel, callback):
        if channel in self.listeners.keys():
            if callback in self.listeners[channel]:
                self.listeners[channel].remove(callback)
                if len(self.listeners[channel]) == 0:
                    del self.listeners[channel]

    def dispatch_message(self, channel, info=None, fail_when_empty=False):

        if channel not in self.listeners.keys():
            if fail_when_empty:
                raise KeyError("No listener on this channel")
            else:
                return

        for callback in self.listeners[channel]:
            callback(info)
