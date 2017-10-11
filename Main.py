from model.World import World

__height = 5
__width = 7
__wallNumber = 10

def main():
    world = World(__height, __width)
    world.placeRandomWalls(__wallNumber)


    world.printMap()





if __name__ == "__main__":
    main()