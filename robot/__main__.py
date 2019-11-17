from robot.robotSimulator import RobotSimulator

VALID_COMMANDS = ["f", "b", "l", "r"]


def main():
    """Simulates the robot interactively"""
    command_string = input("Please enter the comma-separated commands")
    # print("You entered: ", commandString)

    command_list = [command.strip() for command in command_string.lower().split(",")]
    # print(commandList)

    #Check if any command entered in invalid
    for command in command_list:
        if command[0] not in VALID_COMMANDS or not command[1:].isdigit():
            print("One of the commands entered in invalid. Please enter valid commands and try again.")
            exit(1)

    #Simulate robot
    robot = RobotSimulator()
    for command in command_list:
        if command[0] == "f":
            robot.move("forward", int(command[1]))
        elif command[0] == "b":
            robot.move("backward", int(command[1]))
        elif command[0] == "l":
            robot.turn("left", int(command[1]))
        elif command[0] == "r":
            robot.turn("right", int(command[1]))

    robot.get_position()
    robot.get_shortest_distance()


if __name__ == '__main__':
    main()