package uz.pdp.core.patterns.factory;

import uz.pdp.subsystems.lighting.SingleLight;

public interface DeviceFactory {
    SingleLight createLight(int id);
}
