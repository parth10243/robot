from robot.robotSimulator import RobotSimulator

def main():
    """Simulates the robot interactively"""
    commandString = input("Please enter the comma-separated commands")
    # print("You entered: ", commandString)

    commandList = [command.strip() for command in commandString.lower().split(",")]
    # print(commandList)
    robot = RobotSimulator()
    for command in commandList:
        if command[0] == "f":
            robot.move("forward", int(command[1]))
        elif command[0] == "b":
            robot.move("backward", int(command[1]))
        elif command[0] == "l":
            robot.turn("left", int(command[1]))
        elif command[0] == "r":
            robot.turn("right", int(command[1]))

    robot.getPosition()

if __name__ == '__main__':
    main()