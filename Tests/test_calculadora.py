import unittest
from calculadora import Calculadora

class test_calculadora(unittest.TestCase):

    def setUp(self):
        self.calc=Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(4,5),9)

    def test_restar(self):
        self.assertEqual(self.calc.restar(4,5),-1)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(4,2),2)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(4,2),8)