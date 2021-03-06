import operator

from pip.commands.list import tabulate
from prettytable import PrettyTable

from model.ConcreteGreedyThinkStrategy import ConcreteGreedyThinkStrategy
from model.ConcreteRandomThinkStrategy import ConcreteRandomThinkStrategy
from model.Map2D import Map2D
import random

from model.Robot import Robot
from model.ThinkContext import ThinkContext


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
        e = self.__worldMap.getAt(x + 1, y)
        w = self.__worldMap.getAt(x - 1, y)
        s = self.__worldMap.getAt(x, y + 1)
        n = self.__worldMap.getAt(x, y - 1)

        return {'N': n, 'S': s, 'E': e, 'W': w}

    def getRobotList(self):
        return self.__robotList

    def moveAndGetPoint(self, x0, y0, direction):
        points = 0
        x1 = x0
        y1 = y0
        if direction == 'W':
            x1 += -1
        if direction == 'E':
            x1 += 1
        if direction == 'S':
            y1 += 1
        if direction == 'N':
            y1 += -1

        if self.__worldMap.getAt(x1, y1) == 'F':
            points = 1 #1 point for the robot wich is eating the food!

        self.__worldMap.move (x0,y0,x1,y1)
        return points

    def printScoreboard(self, select):
        if str(select).upper() == 'NAME':
            for i in self.__robotList:
                robot = self.__robotList.get(i)
                print('Name  Score')
                print(robot.getRobotName(), '\t', robot.getPoints())
        if str(select).upper() == 'SCORE':
            scoreBoard = {}
            for i in self.__robotList:
                robot = self.__robotList.get(i)
                name = robot.getRobotName()
                score = robot.getPoints()
                scoreBoard.update({name: score})
            scoreBoard = sorted(scoreBoard.items(), key=operator.itemgetter(1), reverse=True)

            pos = 1
            t = PrettyTable(['Position', 'Name', 'Score', 'Think Strategy'])
            for i in scoreBoard:
                robot = self.__robotList.get(('R' + i[0][1]))
                #print(pos, ')\t\t',i[0], '\t\t', i[1], '\t\t', robot.getThinkContext().getConcreteStrategy().getName().split(".")[1])
                t.add_row([ pos, i[0], i[1], robot.getThinkContext().getConcreteStrategy().getName().split(".")[1] ])
                pos+=1
            print (t)




    def getNumberOfFoodToFind(self):
        food=0
        for x in range(self.__worldMap.getWidth()):
            for y in range(self.__worldMap.getHeight()):
                if self.__worldMap.getAt(x,y) == 'F':
                    food +=1
        return food


    def getScores(self):
        scoreBoard = {}
        robot =None
        for i in self.__robotList:
            robot = self.__robotList.get(i)
        scoreBoard.update({robot.getRobotName():robot.getPoints()})



    def placeRandomObject(self, object, number):
        # need to handle Robots in a different way... (due to mandatory specs i can not design this part in a more adaptable way :( )
        if object == 'R':
            for i in range(number):
                name = object + str(i)

                position = self.placeRandomObject(name, 1)

                if(position):
                    chosePolicy = random.choice([0,1])
                    if chosePolicy == 0:
                        thinkContext = ThinkContext(ConcreteRandomThinkStrategy())

                    if chosePolicy == 1:
                        thinkContext = ThinkContext(ConcreteGreedyThinkStrategy())
                    robot = Robot(name, self, position.pop('x'), position.pop('y'), thinkContext)
                    self.__robotList.update({name: robot})

        else:
            for i in range(number):
                placed = False
                count = 0
                while ( not placed and count < 1000 ):  # if i do more than 99 attempts there is just a few free space. Maybe i should find a place for it performing a visit on the matrix... naah the probability is too far, it seems a good compromise to me :P
                    count = count + 1
                    y = random.randrange(self.__worldMap.getHeight())
                    x = random.randrange(self.__worldMap.getWidth())
                    if self.__worldMap.placeNewObjectAt(x, y, object) == 0:  # If placeNewObjectAt succeded i breack the cycle
                        placed = True

                # debug..
                if not placed:
                    print('### ERROR placing object ###')
                    if not count < 1000:
                        print('Cant place that object (', object, ') even after 1000 attempts!! Check input specs')

                if (str(object))[0] == 'R':
                    return {'x':x, 'y':y}
