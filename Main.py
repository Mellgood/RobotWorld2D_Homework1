import time

import copy

from model.World import World
__height = 10
__width = 10
__wallNumber = 10
__foodNumber = 25
__robotNumber = 10

__wallSymbol = '#'
__foodSymbol = 'F' # I used 'F' instead of 'o' due to readability problems :)
__robotSymbol ='R' #Remember to add number to conform on R# format ( even R### format is supported from map atm)

__worldCopyForBenchmark = World(__height, __width)


def main():
    world = World(__height, __width)
    __worldCopyForBenchmark = copy.deepcopy(world)


    world.placeRandomObject(__wallSymbol,__wallNumber)
    world.placeRandomObject(__foodSymbol,__foodNumber)
    world.placeRandomObject(__robotSymbol, __robotNumber)


    world.printMap()

    print()
    print()

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


def noPrint():
    world = __worldCopyForBenchmark

    world.placeRandomObject(__wallSymbol, __wallNumber)
    world.placeRandomObject(__foodSymbol, __foodNumber)
    world.placeRandomObject(__robotSymbol, __robotNumber)

    #world.printMap()

    foodEaten = __foodNumber - world.getNumberOfFoodToFind()
    turno = 1
    while foodEaten < __foodNumber and turno < __foodNumber * 100:  # after all these turns i stop the simulation to avoid loops
        # input('Press enter to continue: ')
        world.tick()
        turno += 1
        foodEaten = __foodNumber - world.getNumberOfFoodToFind()

    print('END OF THE GAME: ', foodEaten, ' F has been eaten and ', world.getNumberOfFoodToFind(),
          ' F are still on the map')
    world.printMap()
    world.printScoreboard('SCORE')
    print()



if __name__ == "__main__":
    start_time1 = time.time()
    main()
    exec_time1 = time.time() - start_time1
    print("--- Execution time: %s seconds ---" % (exec_time1))
    inStr = None
    while not (inStr == 'Y' or inStr == 'N'):
        inStr = input('A lot of time is wasted on printing maps every single turn. Do you want to restart the simulation without printing intermediate maps? [Y/N]')
        inStr = inStr.upper()

    if inStr == 'Y':
        start_time2 = time.time()
        noPrint()
        exec_time2 = time.time() - start_time2
        print("--- Execution time (no print): %s seconds ---" % exec_time2)
        print("It has taken ", exec_time1 - exec_time2, 'less seconds to perform the same task!!\nNote that due to impossibility to repeat robots behaviour, scoreboard and moves can be significatly different')
