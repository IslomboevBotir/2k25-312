package uz.pdp;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import uz.pdp.core.SmartCityController;

import static org.junit.jupiter.api.Assertions.assertSame;

class SingletonTest {
    @Test
    @DisplayName("Test that SmartCityController returns the same instance (Singleton Pattern)")
    void testSingletonInstance() {
        SmartCityController instance1 = SmartCityController.getInstance();
        SmartCityController instance2 = SmartCityController.getInstance();
        assertSame(instance1, instance2, "Both calls to getInstance() should return the same object.");
    }
}
