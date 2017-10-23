import abc


class ThinkContext:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def getMoveDirection(self, view):
        return self._strategy.getDirection(view)

    def getStrategy(self):
        return self._strategy