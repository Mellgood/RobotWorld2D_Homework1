import random

from model import IThinkStrategy, ThinkContext


class Robot:
    __name = None
    __world = None
    __posX = None
    __posY = None
    __map = None
    __view = None
    __direction = None
    __points = 0
    __thinkStrategy = None

    def __init__(self, name, world, x, y, thinkStrategy:ThinkContext):
        self.__name = name
        self.__view = {'N': None, 'S': None, 'E': None, 'O': None}
        self.__posY = y
        self.__posX = x
        self.__world = world
        self.__thinkStrategy = thinkStrategy

    def setThinkStrategy(self, thinkStrategy:ThinkContext):
        self.__thinkStrategy = thinkStrategy

    def tick(self):
        self.sense()
        self.think()
        self.move()

    def getPoints(self):
        return self.__points

    def getRobotName(self):
        return self.__name

    def sense(self):
        newView = self.__world.getViewFrom(self.__posX, self.__posY)
        self.__view.update(newView)

        #self.printView()

    def think(self):
        self.__direction = self.__thinkStrategy.getMoveDirection(self.__view)
        #print(self.__direction)
        #input('ok')

    def move(self):
        if self.__direction:
            #print(self.__name,' Moving ', self.__direction , 'from x y: ' , self.__posX, ' ', self.__posY)
            points = self.__world.moveAndGetPoint(self.__posX, self.__posY, self.__direction)
            self.__points += points

            if self.__direction == 'N':
                self.__posY += -1
            if self.__direction == 'S':
                self.__posY += 1
            if self.__direction == 'E':
                self.__posX += 1
            if self.__direction == 'W':
                self.__posX += -1

    def printView(self):
        print('    ', self.__view.get('N'))

        w = str(self.__view.get('W'))
        e = str(self.__view.get('E'))
        if w.__len__() == 1:
            w = w + "   "
        if w.__len__() == 2:
            w = w + "  "
        if w.__len__() == 3:
            w = w + " "

        if e.__len__() == 1:
            e = e + "   "
        if e.__len__() == 2:
            e = e + "  "
        if e.__len__() == 3:
            e = e + " "

        print(w, self.__name, ' ', e)
        print('    ', self.__view.get('S'))