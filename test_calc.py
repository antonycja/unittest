import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        """Test different different breaking cases"""
        self.assertEqual(calc.add(10, 5), 15) # Call the function being tested inside the assertEqual
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        
    def test_subtract(self):
        """Test different different breaking cases"""
        self.assertEqual(calc.subtract(10, 5), 5) # Call the function being tested inside the assertEqual
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)    
        
    def test_multiply(self):
        """Test different different breaking cases"""
        self.assertEqual(calc.multiply(10, 5), 50) # Call the function being tested inside the assertEqual
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        
    def test_divide(self):
        """Test different different breaking cases"""
        self.assertEqual(calc.divide(10, 5), 2) # Call the function being tested inside the assertEqual
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5) 
        
        with self.assertRaises(ValueError):  # Testing exceptions
            calc.divide(10,0)
            
        
        
        
    
if __name__ == "__main__":
    unittest.main()