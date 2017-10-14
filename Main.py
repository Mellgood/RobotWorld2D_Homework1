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

    for i in range(10):
        print('____________________Round ', i+1,' begin__________________________')
        world.tick()
        print()
        print('map at the end of the round ',i+1, ':')
        world.printMap()
        print('____________________Round ',i+1 ,' end____________________________')




    world.printScoreboard()




if __name__ == "__main__":
    main()