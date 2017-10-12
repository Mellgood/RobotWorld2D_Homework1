from model import World


class Robot:
    __name = None
    __world = None
    __posX = None
    __posY = None
    __map = None
    __view = None

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

        self.printView()

    def think(self):
        pass

    def move(self):
        pass

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