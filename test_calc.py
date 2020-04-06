import unittest
from unittest.mock import patch
import calc

class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Corre al inicio de la tanda de tests"""
        print('Initial Setup')

    @classmethod
    def tearDownClass(cls):
        """Corre al final de la tanda de tests"""
        print('Cleanin up...')

    def setUp(self):
        """Corre al principio de cada test"""
        print('Iniciando test')

    def tearDown(self):
        """Corre al final de cada test"""
        print('limpiando test')

    
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-2,-2),-4)
    
    def test_subtract(self):
        self.assertEqual(calc.substract(10,5),5)
        self.assertEqual(calc.substract(-1,1),-2)
        self.assertEqual(calc.substract(-2,-2),0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(-2,-2),4)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-2,-2),1)
        with self.assertRaises(ValueError):
            calc.divide(10,0)

if __name__ == "__main__":
    unittest.main()

    #TODO: Ver mocks