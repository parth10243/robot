from robot.robotSimulator import RobotSimulator

VALID_COMMANDS = ["f", "b", "l", "r"]


def main():
    """Simulates the robot interactively"""

    input_choice = "0"
    while input_choice not in ["1","2"]:
        input_choice = input("Please enter 1 to input commands as string or 2 to input commands from a file.")

    if input_choice == "1":
        command_string = input("Please enter the comma-separated commands.")
        command_list = [command.strip() for command in command_string.lower().split(",")]
    else:
        command_filename = input("Please enter the file name.")
        try:
            command_file = open(command_filename, "r")
        except OSError as e:
            print("Please input a valid file name.")
            exit(1)
        command_list = command_file.read().rstrip("\n").lower().split(",")

    #Check if any command entered in invalid
    for command in command_list:
        if command[0] not in VALID_COMMANDS or not command[1:].isdigit():
            print("One of the commands entered in invalid. Please enter valid commands and try again.")
            exit(1)

    #Simulate robot
    robot = RobotSimulator()
    for command in command_list:
        if command[0] == "f":
            robot.move("forward", int(command[1:]))
        elif command[0] == "b":
            robot.move("backward", int(command[1:]))
        elif command[0] == "l":
            robot.turn("left", int(command[1:]))
        elif command[0] == "r":
            robot.turn("right", int(command[1:]))

    x, y, direction = robot.get_position()
    print("Final position of the robot is ({},{}) facing {}.".format(x, y, direction))

    distance = robot.get_shortest_distance()
    print("Shortest distance to the starting point is {}.".format(distance))


if __name__ == '__main__':
    main()