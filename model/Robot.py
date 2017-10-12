import random


class Robot:
    __name = None
    __world = None
    __posX = None
    __posY = None
    __map = None
    __view = None
    __direction = None

    def __init__(self, name, world, x, y):
        self.__name = name
        self.__view = {'N': None, 'S': None, 'E': None, 'O': None}
        self.__posY = y
        self.__posX = x
        self.__world = world

    def tick(self):
        self.sense()
        self.think()
        self.move()


    def sense(self):
        newView = self.__world.getViewFrom(self.__posX, self.__posY)
        self.__view.update(newView)

        #self.printView()

    def think(self):
        isEndOfThink = False

        for direction, obj in self.__view.items():
            #If i have food on my field of view, i have to go there to get a point!
            if obj == "F":
                self.__direction = direction
                isEndOfThink = True

        if not isEndOfThink:
            directionsSet=[]
            if not self.__view.get('N') == '#' and not str(self.__view.get('N'))[0] == 'R':
                directionsSet.append('N')
            if not self.__view.get('S') == '#' and not str(self.__view.get('S'))[0] == 'R':
                directionsSet.append('S')
            if not self.__view.get('E') == '#' and not str(self.__view.get('E'))[0] == 'R':
                directionsSet.append('E')
            if not self.__view.get('W') == '#' and not str(self.__view.get('W'))[0] == 'R':
                directionsSet == 'W'
            if not directionsSet:
                print(self.__name, ": Damn... I'm stucked here!! I can not move")
                self.__direction = None
            else:
                self.__direction = random.choice(directionsSet)


    def move(self):
        if self.__direction:
            print('Moving ', self.__direction)

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