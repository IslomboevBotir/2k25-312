"""
SmartCity Sistema testlari
Barcha komponentlarni tekshirish uchun unittest
"""

import unittest
from core.controller import CityController
from modules.lighting.lighting_system import LightingSystem
from modules.transport.traffic_system import TrafficSystemFactory
from modules.security.security_system import SecuritySystemBuilder

class TestSingletonPattern(unittest.TestCase):
    """Singleton pattern testlari"""
    
    def test_singleton_instance(self):
        """Faqat bitta instance yaratilishi kerak"""
        controller1 = CityController.get_instance()
        controller2 = CityController.get_instance()
        self.assertIs(controller1, controller2)
        print("✅ Singleton test o'tdi")

class TestLightingSystem(unittest.TestCase):
    """Yoritish tizimi testlari"""
    
    def setUp(self):
        self.lighting = LightingSystem()
    
    def test_turn_on_lights(self):
        """Chiroqlar yonishini tekshirish"""
        self.lighting.turn_on_all()
        for light in self.lighting.lights:
            self.assertTrue(light.is_on)
        print("✅ Yoritish testi o'tdi")

class TestFactoryPattern(unittest.TestCase):
    """Factory Method pattern testlari"""
    
    def test_traffic_system_creation(self):
        """Transport tizimi yaratilishini tekshirish"""
        traffic = TrafficSystemFactory.create_traffic_system("urban")
        self.assertIsNotNone(traffic)
        print("✅ Factory test o'tdi")

class TestBuilderPattern(unittest.TestCase):
    """Builder pattern testlari"""
    
    def test_security_system_builder(self):
        """Xavfsizlik tizimi qurilishini tekshirish"""
        builder = SecuritySystemBuilder()
        security = (builder
                   .add_cameras(5)
                   .add_sensors(10)
                   .build())
        self.assertEqual(security.cameras_count, 5)
        self.assertEqual(security.sensors_count, 10)
        print("✅ Builder test o'tdi")

def run_tests():
    """Barcha testlarni ishga tushirish"""
    print("\n" + "="*50)
    print("🧪 SMARTCITY TESTLARI")
    print("="*50)
    
    # Test suite yaratish
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Testlarni qo'shish
    suite.addTests(loader.loadTestsFromTestCase(TestSingletonPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestLightingSystem))
    suite.addTests(loader.loadTestsFromTestCase(TestFactoryPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestBuilderPattern))
    
    # Testlarni ishga tushirish
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "="*50)
    if result.wasSuccessful():
        print("✅ Barcha testlar muvaffaqiyatli o'tdi!")
    else:
        print("❌ Ba'zi testlar muvaffaqiyatsiz tugadi")
    print("="*50)

if __name__ == "__main__":
    run_tests()