package uz.pdp;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import uz.pdp.core.patterns.factory.DeviceFactory;
import uz.pdp.core.patterns.factory.LEDLightFactory;
import uz.pdp.subsystems.lighting.SingleLight;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

class FactoryTest {
    @Test
    @DisplayName("Test LED factory creates an LED light (Factory Method Pattern)")
    void testLEDLightFactory() {
        DeviceFactory ledFactory = new LEDLightFactory();
        SingleLight light = ledFactory.createLight(999);
        
        assertNotNull(light, "Factory should create a non-null object.");
        assertEquals("LED", light.getType(), "The light created should be of type LED.");
        assertEquals(999, light.getId(), "The light ID should be set correctly.");
    }
}