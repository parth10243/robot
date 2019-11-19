# Robot

Robot is a command-line interface application which simulates a robot which is moved around based on the input commands provided by the user and then returns the shortest distance back to the starting point. The robot accepts command in the format <command><number>. The four available commands are
  1. `F` - move forward 1 unit
  2. `B` - move backward 1 unit
  3. `R` - turn right 90 degrees
  4. `L` - turn left 90 degrees
  
The number followed by the command determines the number of times the command is performed. For example 'F2' will make the robot move forward twice and 'R2' will make the robot turn to its right twice. The robot can only turn 90 degrees at a time, so it cannot go directly back home, it must move in one of the four directions.
The robot starts from (0,0) and is facing North intially. And the grid is shown below

<img src ="img/robot%20grid.png">

## Install
To install the application, download the project and navigate to root directory of robot and run `pip3 install .`
To uninstall the application, run `pip3 uninstall robot` from the root directory of robot.
If you want to further develop the project use `pip install -e` command. -e arument installs the package as a edditable package so you wouldn't have to re-install the package again every time you make changes to code.

## Execute
After installing the CLI application, you can execute it by simply running `robot`.
On doing so, the application would give you option to provide command string either by typing it on command line or by providing the file name which contains command string.
<img src ="img/input%20string.png">
<img src ="img/input%20file.png">

    
## Testing
Unit testing was performed to check each unit component of RobotSimulator module. The test file for the same can be found in tests package in the project. The package also contains command.txt which a text file containing command string. To view the result of the testing, simply navigate to tests package and run `python3 test_robotSimulator.py ` 
