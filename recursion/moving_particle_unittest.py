__author__ = 'DIA'

import unittest

from moving_particle import animation


class AnimationTest(unittest.TestCase):
    def test_single_move(self):
        self.assertEqual(["..X....", "....X..", "......X", "......."], animation(2, "..R...."))

    def test_multiple_move(self):
        self.assertEqual(["XX..XXX", ".X.XX..", "X.....X", "......."], animation(3, "RR..LRL"))

    def test_single_dot(self):
        self.assertEqual(["XXXX.XXXX", "X..X.X..X", ".X.X.X.X.", ".X.....X.", "........."], animation(2, "LRLR.LRLR"))

    def test_multiple_move2(self):
        self.assertEqual(["XXXXXXXXXX", ".........."], animation(10, "RLRLRLRLRL"))

    def test_isolated_move(self):
        self.assertEqual(["..."], animation(1, "..."))

    def test_complex_move(self):
        self.assertEqual(["XXXX.XX.XXX.X.XXXX.", "..XXX..X..XX.X..XX.", ".X.XX.X.X..XX.XX.XX", "X.X.XX...X.XXXXX..X",
                          ".X..XXX...X..XX.X..", "X..X..XX.X.XX.XX.X.", "..X....XX..XX..XX.X", ".X.....XXXX..X..XX.",
                          "X.....X..XX...X..XX", ".....X..X.XX...X..X", "....X..X...XX...X..", "...X..X.....XX...X.",
                          "..X..X.......XX...X", ".X..X.........XX...", "X..X...........XX..", "..X.............XX.",
                          ".X...............XX", "X.................X", "..................."],
                         animation(1, "LRRL.LR.LRR.R.LRRL."))
