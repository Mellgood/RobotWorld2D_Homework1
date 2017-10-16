import random


class ConcreteGreedyThinkStrategy:
    def getDirection(self, view: dict):

        isEndOfThink = False

        for direction, obj in view.items():
            #If i have food on my field of view, i have to go there to get a point!
            if obj == "F":
                self.__direction = direction
                isEndOfThink = True

        #if there is no food, i have to think better, so I will move in a random direction :P
        if not isEndOfThink:
            directionsSet=[]
            #I can move on a direction if and only if there is no wall or other robot there
            if (not (str(view.get('N')) == '#') and (not (str(view.get('N'))[0] == 'R'))):
                directionsSet.append('N')
            if (not (str(view.get('S')) == '#') and (not (str(view.get('S'))[0] == 'R'))):
                directionsSet.append('S')
            if (not (str(view.get('E')) == '#') and (not (str(view.get('E'))[0] == 'R'))):
                directionsSet.append('E')
            if (not (str(view.get('W')) == '#') and (not (str(view.get('W'))[0] == 'R'))):
                directionsSet.append('W')
            if not directionsSet:
                self.__direction = None
            else:
                self.__direction = random.choice(directionsSet) #at this point i only have best choices (all food directions or all 0 directions)

        return self.__direction