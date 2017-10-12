from model.World import World

__height = 10
__width = 10
__wallNumber = 20
__foodNumber = 10
__robotNumber = 10

__wallSymbol = '#'
__foodSymbol = 'F' # I used F instead of o due to readability problems :)
__robotSymbol ='R' #Remember to add number to conform on R# format ( even R### format is supported from map atm)

def main():
    world = World(__height, __width)
    world.placeRandomObject(__wallSymbol,__wallNumber)
    world.placeRandomObject(__foodSymbol,__foodNumber)

    #sta cosa va fatta in world, in modo da mantenere li dei riferimenti ai robot creati ed instanziare un oggetto per ogni robot!!
    robotList = []
    for i in range(__robotNumber):
        name = __robotSymbol + str(i)
        robotList.append(name)
        world.placeRandomObject(name, 1)


    world.printMap()





if __name__ == "__main__":
    main()