"""

basic testing code using Python's "unittest" library

"""
import unittest

# A simple function we'll test
def fun(x):
    return x+1


# Defines the test class, which we'll run at the end (or can be called from command line)
class TestStringMethods(unittest.TestCase):
    
    #runs to set-up things needed for tests
    def setUp(self):
        self.evens_list = [0,2,4,6,8]

    # If you want to feed several parameters, you can run each as a test...
    # Good for tracking which ones failed
    def test_even(self):
        for i in range(0, 6, 2):
            with self.subTest(i=i):
                self.assertEqual(self.evens_list[i] % 2, 0) #Test that numbers in our list are even
        
    def test_fun(self):
        self.assertEqual(2,fun(1),'fun didnt add 1')
        
    # tells unittest to expect that this test will fail, and that's OK
    @unittest.expectedFailure
    def test_fun2(self):
        self.assertEqual(2,fun(2),'fun expected fail')
        
    #runs to destroy things that WERE needed for tests, but are no longer useful
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
    # or for jupyter notebook:
    #unittest.main(argv=['first-arg-is-ignored'], exit=False)
