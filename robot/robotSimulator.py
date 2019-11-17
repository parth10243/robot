DIRECTION = ["NORTH", "EAST", "SOUTH", "WEST"]

class RobotSimulator():
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
            self.facing = self.facing + (number % 4)
        if command == "left":
            self.facing = self.facing - (number % 4)

    def move (self, command, number):
        """Move the robot either forward or backward based on the command

        Keyword arguments:
        command -- the command given to robot either forward or backward
        number -- the number of times move is to be performed
        """
        if command == "forward":
            if DIRECTION[self.facing] == "NORTH":
                self.y += number
            elif DIRECTION[self.facing] == "SOUTH":
                self.y -= number
            elif DIRECTION[self.facing] == "EAST":
                self.x += number
            elif DIRECTION[self.facing] == "WEST":
                self.x -= number

        if command == "backward":
            if DIRECTION[self.facing] == "NORTH":
                self.y -= number
            elif DIRECTION[self.facing] == "SOUTH":
                self.y += number
            elif DIRECTION[self.facing] == "EAST":
                self.x -= number
            elif DIRECTION[self.facing] == "WEST":
                self.x += number

    def getPosition(self):
        """Prints the position of robot along the directing in which it is facing"""
        print("Final position of the robot is ({},{}) facing {}.".format(self.x, self.y, DIRECTION[self.facing]))
