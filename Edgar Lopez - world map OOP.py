class Room(object):
    def __init__(self, name, north, west, south, east, description):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.south = south
        self.east = east

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
start = Room("Starting Room", None, "lookout", None, 'fire_pad', 'Where you start and activate the teleporter.')
Theater = Room("Theater", None, 'Trap', "Starting room", 'Is where you activate the teloporter.')
Fire_pad = Room("Fire_pad, Outside, None, None, None, Starting room", 'You could activate a trap.')
Outside = Room("Outside, Fence Room, None, Fire Pad, None ")
Fence_Room = Room("Fence_Room, Trap Room, None, Outside, Theater",'You can activate a electricity trap.')
Library = Room("Library, None, Theater, Living_Room, None", 'This is where you can flip a lever to make the mystery chest.')
Living_Room = Room("Living_Room, Librabry, None, Kodino, None", 'You could take a perk "Double Hands"')
Kodino = Room("Kodino, Living_Room, Look_out Room, None, None", 'You can drink a perk"Jerganaut"' )

current_node = start
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form
        command = directions
    if command in directions:
        try:

        except KeyError:
            print("You cannot go this way")
    else:
        print('Command not Recognized')
