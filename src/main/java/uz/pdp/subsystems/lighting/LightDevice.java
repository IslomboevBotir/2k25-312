package uz.pdp.subsystems.lighting;

import lombok.Getter;

@Getter
public abstract class LightDevice {

    protected final int id;

    protected boolean isOn = false;

    protected final String type;

    protected LightDevice(int id, String type) {
        this.id = id;
        this.type = type;
    }

    public void turnOn() {
        this.isOn = true;
    }

    public void turnOff() {
        this.isOn = false;
    }

}
