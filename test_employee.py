import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        """-setUp run everytime before the rest of the test are run
        -It must be in camelCase
        -It's a way of defining constants once
        """
        self.emp_1 = Employee("Anton", "Maposa", 500000)
        self.emp_2 = Employee("Moses", "Kapapa", 20000)
        
    def tearDown(self):
        """
        -tearDown runs at the end    
        -It must be in camelCase
        """
        pass
    
    def test_email(self):
        self.assertEqual(self.emp_1.email, "Anton.Maposa@email.com")
        self.assertEqual(self.emp_2.email, "Moses.Kapapa@email.com")
        
    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "Anton Maposa")
        self.assertEqual(self.emp_2.fullname, "Moses Kapapa")
        
    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 525000)
        self.assertEqual(self.emp_2.pay, 21000)
        
        
if __name__ == "__main__":
    unittest.main()
        
        