import unittest
from activityselectlab import activity_select,rec_act_sel

class ActivityTestCase(unittest.TestCase):
    def testActivitySelect(self):
        
        activity=[]
        start=[1,3,0,5,3,5,6,8,8,2,12]
        finish=[4,5,6,7,9,9,10,11,12,14,16]
        
        self.assertEqual(activity_select(start,finish,11),[1,4,8,11])
        rec_act_sel(start, finish,-1,11,activity)
        self.assertEqual(activity,[1,4,8,11])

if __name__ == '__main__':
    unittest.main()
