from model.World import World

__height = 5
__width = 5
__wallNumber = 5
__foodNumber = 5
__robotNumber = 5

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
        world.printScoreboard()
        print('____________________Round ',turno ,' end____________________________')

        turno += 1
        foodEaten = __foodNumber - world.getNumberOfFoodToFind()




    print('END OF THE GAME')
    world.printScoreboard()




if __name__ == "__main__":
    main()