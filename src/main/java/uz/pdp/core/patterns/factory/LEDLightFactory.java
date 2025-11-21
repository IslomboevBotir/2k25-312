package uz.pdp.core.patterns.factory;

import uz.pdp.subsystems.lighting.SingleLight;

public class LEDLightFactory implements DeviceFactory {
    @Override
    public SingleLight createLight(int id) {
        return new SingleLight(id, "LED");
    }
}
