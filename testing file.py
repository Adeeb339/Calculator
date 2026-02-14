import unittest
import cal

class test_cal(unittest.TestCase):
    def test_add(self):
        result1=cal.add(1,2)
        self.assertEqual(result1, 3)
        result2=cal.add(-1,2)
        self.assertEqual(result2, 1)
        result3=cal.add(-1,-2)
        self.assertEqual(result3, -3)

    def test_sub(self):
        result1=cal.sub(2,1)
        self.assertEqual(result1, 1)
        result2=cal.sub(-2,1)
        self.assertEqual(result2, -3)
        result3=cal.sub(-2,-1)
        self.assertEqual(result3, -1)

    def test_mult(self):
        result1=cal.mult(2,1)
        self.assertEqual(result1, 2)
        result2=cal.mult(-2,1)
        self.assertEqual(result2, -2)
        result3=cal.mult(-2,-1)
        self.assertEqual(result3, 2)
    
    def test_div(self):
        result1=cal.div(2,2)
        self.assertEqual(result1, 1)
        result2=cal.div(-2,2)
        self.assertEqual(result2, -1)
        result3=cal.div(-2,-2)
        self.assertEqual(result3, 1)

if __name__ == "__main__":
    unittest.main()
    

                                                                