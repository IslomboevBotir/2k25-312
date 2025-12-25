import unittest
from core.controller import CityController

class TestSmartCity(unittest.TestCase):
    def test_singleton_controller(self):
        a = CityController.get_instance()
        b = CityController.get_instance()
        self.assertIs(a,b)

    def test_light_factory(self):
        controller = CityController.get_instance()
        lights = controller.factory.create_lighting_system('street')
        self.assertEqual(lights.type, 'street')

    def test_builder_transport(self):
        controller = CityController.get_instance()
        bus = controller.builders['vehicle_builder'].create_bus('B-100')
        self.assertIn('engine', bus.specs)

if __name__ == '__main__':
    unittest.main()
