from model.World import World

__height = 10
__width = 10
__wallNumber = 20
__foodNumber = 25
__robotNumber = 10

__wallSymbol = '#'
__foodSymbol = 'F' # I used 'F' instead of 'o' due to readability problems :)
__robotSymbol ='R' #Remember to add number to conform on R# format ( even R### format is supported from map atm)

def main():
    world = World(__height, __width)

    world.placeRandomObject(__wallSymbol,__wallNumber)
    world.placeRandomObject(__foodSymbol,__foodNumber)
    world.placeRandomObject(__robotSymbol, __robotNumber)


    world.printMap()

    print()
    print()

    foodEaten = 0
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
    world.printScoreboard('SCORE')




if __name__ == "__main__":
    main()