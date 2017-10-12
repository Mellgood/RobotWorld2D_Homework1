from model.Map2D import Map2D
import random

class World:
    __worldMap = None

    def __init__(self, width, height):
        self.__worldMap = Map2D(width, height)

    def printMap(self):
        self.__worldMap.printMap()

    def placeRandomObject(self, object, number):
        for i in range(number):
            placed = False
            count = 0
            while (not placed and count < 1000): # if i do more than 99 attempts there is just a few free space. Maybe i should find a place for it performing a visit on the matrix... naah the probability is too far, it seems a good compromise to me :P
                count = count + 1
                y = random.randrange(self.__worldMap.getHeight())
                x = random.randrange(self.__worldMap.getWidth())
                if self.__worldMap.placeNewObjectAt(x,y,object) == 0: #If placeNewObjectAt succeded i breack the cycle
                    placed = True

            #debug..
            if not placed:
                print('### ERROR placing object ###')
                if not count<1000:
                    print('Cant place that object (', object, ') even after 1000 attempts!!')