"""
The purpose of this program is to test the classify_triangles program

@author: Julio Lora
"""

from classify_triangles import *
import unittest


class TestTriangles(unittest.TestCase):

    def testEquilateral(self):
        self.assertEqual(classify_triangle(2,2,2),'Equilateral')

    def testScalene(self):
        self.assertEqual(classify_triangle(10,15,23),'Scalene')

    def testRight(self):
        self.assertEqual(classify_triangle(3,4,5),'Right')

    def testIsoceles(self):
        self.assertEqual(classify_triangle(6,6,8),'Isoceles')

    def testNotATriangle(self):
        self.assertEqual(classify_triangle(1,2,3),'NotATriangle')

    def testInput1(self):
        self.assertEqual(classify_triangle('Hi',6,8),'Invalid Input')

    def testInput2(self):
        self.assertEqual(classify_triangle(6,'Hi',8),'Invalid Input')

    def testInput3(self):
        self.assertEqual(classify_triangle(6,6,'Hi'),'Invalid Input')

    def testInput4(self):
        self.assertEqual(classify_triangle(-4,6,8),'Invalid Input')

if __name__ == '__main__':
    unittest.main()
