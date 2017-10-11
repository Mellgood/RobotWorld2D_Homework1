class Map2D:
    __map = None
    __width = None
    __height = None

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__generateFloor()

    def __generateFloor(self):
        self.__map = [['0' for i in range(self.__height)] for j in range(self.__width)]

    def placeNewObjectAt(self, x, y, newCel):
        '''
        If possible, places newCel at x,y position and returns 0. If not possible, it returns -1

        :param x: ordinate
        :param y: coordinate
        :param newCel: new obj string
        :return: 0: done, -1: not possible
        '''
        if self.__map[x][y] == '0':
            self.__map[x][y] = newCel
            return 0


        return -1

    def getAt(self,x,y):
        return self.__map[x][y]

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def printMap(self):
        '''
        I wanna format output for matrix [x][y] with x,y < 1000 so I allocate 3 spaces for 3 char (note that possible
        cell values are mandatory 0, R###, F, o, [future_new_symbol]) and one further space to separate from the next cell
        (on row). This way i have the same space between cells for 1, 2 or 3 string lengths.

        :return:
        '''
        for y in self.__map:
            row = ""
            for element in y:
                element = str(element)
                # now i have the element so i can give the right space to it
                if element.__len__() == 1:
                    element = element + "   "
                if element.__len__() == 2:
                    element = element + "  "
                if element.__len__() == 3:
                    element = element + " "
                row = row + element

            # The row is now ready to be printed
            print(row)