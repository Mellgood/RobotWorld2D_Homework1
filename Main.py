import time

import copy

from model.World import World
__height = 11
__width = 15
__wallNumber = 11
__foodNumber = 20
__robotNumber = 7

__wallSymbol = '#'
__foodSymbol = 'F' # I used 'F' instead of 'o' due to readability problems :)
__robotSymbol ='R' #Remember to add number to conform on R# format ( even R### format is supported from map atm)


def main():
    world = World(__width, __height)

    #zeroes on the map feels so loonely... let's populate the map ;)
    world.placeRandomObject(__wallSymbol,__wallNumber)
    world.placeRandomObject(__foodSymbol,__foodNumber)
    world.placeRandomObject(__robotSymbol, __robotNumber)

    #now i want to print the initial populated map
    world.printMap()

    print('\n\n')

    #starting game loop :)
    foodEaten = __foodNumber - world.getNumberOfFoodToFind()
    turno=1
    while foodEaten < __foodNumber and turno < __foodNumber*100: #after all these turns i stop the simulation to avoid loops
        #input('Press enter to continue: ')
        print('____________________Round ', turno,' begin__________________________')
        world.tick()
        print()
        print('map at the end of the round ',turno, ':')
        world.printMap()
        print()
        world.printScoreboard('SCORE')
        print('____________________Round ',turno ,' end____________________________')

        turno += 1
        foodEaten = __foodNumber - world.getNumberOfFoodToFind()




    print('END OF THE GAME: ', foodEaten, ' F has been eaten and ', world.getNumberOfFoodToFind(), ' F are still on the map')
    #world.printScoreboard('SCORE')
    print()


if __name__ == "__main__":
    start_time1 = time.time()
    main()
    exec_time1 = time.time() - start_time1
    print("--- Execution time: %s seconds ---" % (exec_time1))