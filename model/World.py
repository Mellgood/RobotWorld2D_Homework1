from model.Map2D import Map2D
import random

from model.Robot import Robot


class World:
    __worldMap = None
    __robotList = {}

    def __init__(self, width, height):
        self.__worldMap = Map2D(width, height)

    def printMap(self):
        self.__worldMap.printMap()

    def tick(self):
        for i in self.__robotList:
            robot = self.__robotList.get(i)
            robot.tick()


    def getViewFrom(self, x, y):
        #note that while x is higher rightside (normal as human perception), y is higher downside!! so pay attention to it
        s = self.__worldMap.getAt(x + 1, y)
        n = self.__worldMap.getAt(x - 1, y)
        e = self.__worldMap.getAt(x, y + 1)
        w = self.__worldMap.getAt(x, y - 1)

        return {'N': n, 'S': s, 'E': e, 'W': w}

    def getRobotList(self):
        return self.__robotList

    def placeRandomObject(self, object, number):
        # need to handle Robots in a different way... (due to mandatory specs i can not design this part in a more adaptable way :( )
        if object == 'R':
            for i in range(number):
                name = object + str(i)

                position = self.placeRandomObject(name, 1)

                if(position):
                    robot = Robot(name, self, position.pop('x'), position.pop('y'))
                    self.__robotList.update({name: robot})

        else:
            for i in range(number):
                placed = False
                count = 0
                while (
                    not placed and count < 1000):  # if i do more than 99 attempts there is just a few free space. Maybe i should find a place for it performing a visit on the matrix... naah the probability is too far, it seems a good compromise to me :P
                    count = count + 1
                    y = random.randrange(self.__worldMap.getHeight())
                    x = random.randrange(self.__worldMap.getWidth())
                    if self.__worldMap.placeNewObjectAt(x, y, object) == 0:  # If placeNewObjectAt succeded i breack the cycle
                        placed = True

                # debug..
                if not placed:
                    print('### ERROR placing object ###')
                    if not count < 1000:
                        print('Cant place that object (', object, ') even after 1000 attempts!!')

                if (str(object))[0] == 'R':
                    return {'x':x, 'y':y}

