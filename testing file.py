import unittest
import cal

class test_cal(unittest.TestCase):
    def test_add(self):
        Aresult1=cal.add(1,2)
        self.assertEqual(Aresult1, 3)
        Aresult2=cal.add(-1,2)
        self.assertEqual(Aresult2, 1)
        Aresult3=cal.add(-1,-2)
        self.assertEqual(Aresult3, -3)

    def test_sub(self):
        Aresult1=cal.sub(2,1)
        self.assertEqual(Aresult1, 1)
        Aresult2=cal.sub(-2,1)
        self.assertEqual(Aresult2, -3)
        Aresult3=cal.sub(-2,-1)
        self.assertEqual(Aresult3, -1)

if __name__ == "__main__":
    unittest.main()
    

                                                                