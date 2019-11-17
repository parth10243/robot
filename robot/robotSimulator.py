DIRECTION = ["NORTH", "EAST", "SOUTH", "WEST"]
MOVEMENT = {
    'NORTH': {
        'forward': 1,
        'backward': -1
    },
    'EAST': {
        'forward': 1,
        'backward': -1
    },
    'SOUTH': {
        'forward': -1,
        'backward': 1
    },
    'WEST': {
        'forward': -1,
        'backward': 1
    },
}


class RobotSimulator:
    """Simulate a robot with starting point (0,0) and faces North"""

    x = None
    y = None
    facing = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = 0

    def turn(self, command, number):
        """Turn the robot either left or right based on the command

        Keyword arguments:
        command -- the command given to robot either right or left
        number -- the number of times turn is to be performed
        """

        if command == "right":
            self.facing = (self.facing + number) % 4
        if command == "left":
            self.facing = (self.facing - number) % 4
        return DIRECTION[self.facing]

    def move(self, command, number):
        """Move the robot either forward or backward based on the command

        Keyword arguments:
        command -- the command given to robot either forward or backward
        number -- the number of times move is to be performed
        """

        direction_multiplier = MOVEMENT[DIRECTION[self.facing]][command]                              #+1 or -1 based on the current direction of robot and command given
        if DIRECTION[self.facing] in ["NORTH","SOUTH"]:
            self.y += (direction_multiplier * number)
        elif DIRECTION[self.facing] in ["EAST","WEST"]:
            self.x += (direction_multiplier * number)

        return self.x, self.y, DIRECTION[self.facing]

    def get_position(self):
        """Returns the position of robot along the direction in which it is facing"""
        return self.x, self.y, DIRECTION[self.facing]

    def get_shortest_distance(self):
        """Returns the shortest distance back to the starting point"""
        return (abs(self.x) + abs(self.y))
