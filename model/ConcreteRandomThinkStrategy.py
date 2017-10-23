import random

from model.IThinkStrategy import IThinkStrategy


class ConcreteRandomThinkStrategy(IThinkStrategy):
    def getName(self):
        return __name__

    def getDirection(self, view: dict):
        possibleMoves = []
        cardinalDirections = ['N', 'S', 'E', 'O']
        for dir in cardinalDirections:
            if (not (str(view.get('N')) == '#') and (not (str(view.get('N'))[0] == 'R'))):
                pass

            if (not (str(view.get('N')) == '#') and (not (str(view.get('N'))[0] == 'R'))):
                possibleMoves.append('N')
            if (not (str(view.get('S')) == '#') and (not (str(view.get('S'))[0] == 'R'))):
                possibleMoves.append('S')
            if (not (str(view.get('E')) == '#') and (not (str(view.get('E'))[0] == 'R'))):
                possibleMoves.append('E')
            if (not (str(view.get('W')) == '#') and (not (str(view.get('W'))[0] == 'R'))):
                possibleMoves.append('W')

        if not possibleMoves:
            answer = None
        else:
            answer = random.choice(possibleMoves)

        return answer