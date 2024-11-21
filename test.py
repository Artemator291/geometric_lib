import unittest
import rectangle
import circle
import square
import triangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_area_positive(self):
        self.assertEqual(rectangle.area(5, 10), 50)

    def test_rectangle_area_zero(self):
        self.assertEqual(rectangle.area(5, 0), 0)
        self.assertEqual(rectangle.area(0, 10), 0)

    def test_rectangle_area_big(self):
        self.assertEqual(rectangle.area(5, 1000), 5000)
        self.assertEqual(rectangle.area(100, 100), 10000)

    def test_rectangle_perimeter_positive(self):
        self.assertEqual(rectangle.perimeter(5, 10), 30)

    def test_rectangle_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(5, 0), 10)
        self.assertEqual(rectangle.perimeter(0, 10), 20)

    def test_rectangle_perimeter_big(self):
        self.assertEqual(rectangle.perimeter(50000, 2), 100004)
        self.assertEqual(rectangle.perimeter(25000, 25000), 100000)

class TestSquare(unittest.TestCase):
    def test_square_area_positive(self):
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(10), 100)

    def test_square_area_zero(self):
        self.assertEqual(square.area(0),0)

    def test_square_area_big(self):
        self.assertEqual(square.area(100), 10000)
        self.assertEqual(square.area(5000), 25000000)

    def test_square_perimeter_positive(self):
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(100), 400)

    def test_square_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_square_perimeter_big(self):
        self.assertEqual(square.perimeter(10000), 40000)
        self.assertEqual(square.perimeter(50000), 200000)

class TestCircle(unittest.TestCase):
    def test_circle_area_positive(self):
        self.assertEqual(circle.area(5), 78.53981633974483)
        self.assertEqual(circle.area(10), 314.1592653589793)

    def test_square_area_zero(self):
        self.assertEqual(circle.area(0),0)

    def test_square_area_big(self):
        self.assertEqual(circle.area(100), 31415.926535897932)
        self.assertEqual(circle.area(5000), 78539816.33974484)

    def test_square_perimeter_positive(self):
        self.assertEqual(circle.perimeter(5), 31.41592653589793)
        self.assertEqual(circle.perimeter(100), 628.3185307179587)

    def test_square_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_square_perimeter_big(self):
        self.assertEqual(circle.perimeter(10000), 62831.853071795864)
        self.assertEqual(circle.perimeter(50000), 314159.2653589793)

class TestTriangle(unittest.TestCase):
    def test_triangle_area_positive(self):
        self.assertEqual(triangle.area(5, 10), 25.0)
        self.assertEqual(triangle.area(10, 15), 75.0)

    def test_triangle_area_zero(self):
        self.assertEqual(triangle.area(0,10),0.0)
        self.assertEqual(triangle.area(10, 0), 0.0)
        self.assertEqual(triangle.area(0, 0), 0.0)

    def test_triangle_area_big(self):
        self.assertEqual(triangle.area(500,1000), 250000.0)
        self.assertEqual(triangle.area(999,9899), 4944550.5)

    def test_triangle_perimeter_positive(self):
        self.assertEqual(triangle.perimeter(5, 10 ,15), 30)
        self.assertEqual(triangle.perimeter(14,11,40), 65)

    def test_triangle_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)
        self.assertEqual(triangle.perimeter(10, 0, 2), 12)
        self.assertEqual(triangle.perimeter(0, 4, 12), 16)

    def test_triangle_perimeter_big(self):
        self.assertEqual(triangle.perimeter(10000, 500000, 1400000), 1910000)
        self.assertEqual(triangle.perimeter(9000000,9000000000,9000000), 9018000000)

if __name__ == '__main__':
    unittest.main()

