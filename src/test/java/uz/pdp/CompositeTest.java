package uz.pdp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import uz.pdp.subsystems.lighting.LightGroup;
import uz.pdp.subsystems.lighting.SingleLight;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class CompositeTest {
    private SingleLight light1;
    private SingleLight light2;
    private LightGroup group;

    @BeforeEach
    void setUp() {
        light1 = new SingleLight(1, "TEST");
        light2 = new SingleLight(2, "TEST");
        group = new LightGroup("Test Group");
        group.add(light1);
        group.add(light2);
    }

    @Test
    @DisplayName("Test turning on a group turns on all individual lights (Composite Pattern)")
    void testTurnOnGroup() {
        group.turnOn();
        assertTrue(light1.isOn(), "Light 1 should be on.");
        assertTrue(light2.isOn(), "Light 2 should be on.");
    }

    @Test
    @DisplayName("Test turning off a group turns off all individual lights (Composite Pattern)")
    void testTurnOffGroup() {
        group.turnOn(); // First turn them on
        group.turnOff();
        assertFalse(light1.isOn(), "Light 1 should be off.");
        assertFalse(light2.isOn(), "Light 2 should be off.");
    }
}