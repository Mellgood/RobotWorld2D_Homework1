import abc

class IThinkStrategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms. Robot
    uses this interface to call the algorithm defined by a
    ConcreteThinkStrategy.
    """
    @abc.abstractmethod
    def getDirection(self, view):
        pass