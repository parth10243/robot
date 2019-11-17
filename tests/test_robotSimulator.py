import unittest
from robot.robotSimulator import  RobotSimulator


class TestRobotSimulator(unittest.TestCase):

    def setUp(self):
        self.robot = RobotSimulator()

    def test_turn(self):
        self.assertEqual(self.robot.turn("right",0), "NORTH")
        self.assertEqual(self.robot.turn("right",1), "EAST")
        self.assertEqual(self.robot.turn("right",2), "WEST")
        self.assertEqual(self.robot.turn("right",3), "SOUTH")
        self.assertEqual(self.robot.turn("right", 2), "NORTH")

        self.assertEqual(self.robot.turn("left", 0), "NORTH")
        self.assertEqual(self.robot.turn("left", 1), "WEST")
        self.assertEqual(self.robot.turn("left", 2), "EAST")
        self.assertEqual(self.robot.turn("left", 3), "SOUTH")

    def test_move(self):
        self.assertEqual(self.robot.move("forward",4), (0, 4, "NORTH"))
        self.assertEqual(self.robot.move("backward", 4), (0, 0, "NORTH"))     #returns to origin after moving backwards
        self.robot.facing = 1
        self.assertEqual(self.robot.move("forward", 4), (4, 0, "EAST"))
        self.assertEqual(self.robot.move("backward", 4), (0, 0, "EAST"))
        self.robot.facing = 2
        self.assertEqual(self.robot.move("forward", 4), (0, -4, "SOUTH"))
        self.assertEqual(self.robot.move("backward", 4), (0, 0, "SOUTH"))
        self.robot.facing = 3
        self.assertEqual(self.robot.move("forward", 4), (-4, 0, "WEST"))
        self.assertEqual(self.robot.move("backward", 4), (0, 0, "WEST"))

    def test_get_position(self):
        result = (0, 0, "NORTH")
        self.assertEqual(self.robot.get_position(), result)

    def test_get_shortest_distance(self):
        result = 0
        self.assertEqual(self.robot.get_shortest_distance(), result)


if __name__ == '__main__':
    unittest.main()
