package uz.pdp.subsystems.lighting;

public class SingleLight extends LightDevice implements LightComponent {

    public SingleLight(int id, String type) {
        super(id, type);
    }

    @Override
    public void turnOn() {
        super.turnOn();
        System.out.println(type + " Light " + id + " turned ON.");
    }

    @Override
    public void turnOff() {
        super.turnOff();
        System.out.println(type + " Light " + id + " turned OFF.");
    }

    @Override
    public String getStatus() {
        return "  - " + type + " Light " + id + " is " + (isOn() ? "On" : "Off");
    }
}
