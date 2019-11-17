from robot.robotSimulator import RobotSimulator

def main():
    """Simulates the robot interactively"""
    commandString = input("Please enter the comma-separated commands")
    # print("You entered: ", commandString)

    commandList = [command.strip() for command in commandString.lower().split(",")]
    # print(commandList)

    #Check if any command entered in invalid
    for command in commandList:
        if command[0] not in ["f", "b", "l", "r"] or not command[1:].isdigit():
            print("One of the commands entered in invalid. Please enter valid commands and try again.")
            exit(1)

    #Simulate robot
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