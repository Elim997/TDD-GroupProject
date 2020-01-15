import unittest
from bubbleSort import *
from Bmi_code import *

class Testwork(unittest.TestCase):

    def test_is_empty(self):
        arr=[4,6,1,3,8]
        self.assertTrue(bubbleSort(arr)),"bubble is empty"

    def test_no_lost(self):
        arr=[4,6,1,3,8]
        temp = arr.copy()
        self.assertCountEqual(bubbleSort(arr), temp),"a argoment as lost"

    def test_if_sorted(self):
        arr=[4,6,1,3,8]
        temp = [1,3,4,6,8]
        self.assertListEqual(bubbleSort(arr), temp),"not sorted"

    def test_weight(self):
        height = 1.76
        weight = 71
        self.assertTrue(bmi(weight,height) >= 18.5 and bmi(weight,height) < 25),"Bmi Dot work right"  
        
if __name__ == '__main__':
    unittest.main()