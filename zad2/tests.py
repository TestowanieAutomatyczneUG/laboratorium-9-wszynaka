from unittest import TestCase, main
from unittest.mock import *
from caar import CarImpl,Car

class test_Carimpl(TestCase):
    def test_FuelCheck(self):
        test = CarImpl()
        test.FuelCheck = Mock(name='FuelCheck')
        test.FuelCheck.return_value = False
        self.assertEqual(False, test.FuelCheck(), 'Mało paliwa')

    def test_chceckEngineTemperature(self):
        test = CarImpl()
        test.chceckEngineTemperature = Mock(name='chceckEngineTemperature ')
        test.chceckEngineTemperature.return_value = 120
        self.assertEqual(120,test.chceckEngineTemperature(), "Za duża temperatura")

    def test_setDestination(self):
        def side_effect(arg):
            return arg
        test = CarImpl()
        test.setDestination = Mock(name='setDestination')
        test.setDestination.side_effect = side_effect
        self.assertEqual("Gda",test.setDestination("Gda"))


if __name__ == '__main__':
    main()      
