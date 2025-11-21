package uz.pdp.subsystems.lighting;

public interface LightComponent {
    void turnOn();
    void turnOff();

    String getStatus();
}
