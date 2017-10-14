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

    print('____________________Round 1 begin__________________________')
    world.tick()
    print()
    print('map at the end of the round:')
    world.printMap()
    print('____________________Round 1 end__________________________')

    print('____________________Round 2 begin__________________________')
    world.tick()
    print()
    print('map at the end of the round:')
    world.printMap()
    print('____________________Round 2 end__________________________')

    print('____________________Round 3 begin__________________________')
    world.tick()
    print()
    print('map at the end of the round:')
    world.printMap()
    print('____________________Round 3 end__________________________')




if __name__ == "__main__":
    main()