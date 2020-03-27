import unittest
import main

class Test_main(unittest.TestCase):
   def test_guess_funct(self):
        result = main.run_guess(5, 5)
        self.assertTrue(result )

   def test_guess_funct2(self):
       result = main.run_guess(5, 0)
       self.assertFalse(result)

   def test_guess_funct3(self):
       result = main.run_guess(11, 5)
       self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

