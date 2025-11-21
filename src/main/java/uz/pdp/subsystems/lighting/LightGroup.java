package uz.pdp.subsystems.lighting;

import lombok.RequiredArgsConstructor;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@RequiredArgsConstructor
public class LightGroup implements LightComponent{

    private final String name;

    private final List<LightComponent> lights = new ArrayList<>();

    public void add(LightComponent light) {
        lights.add(light);
    }

    public void remove(LightComponent light) {
        lights.remove(light);
    }

    @Override
    public void turnOn() {
        System.out.println("Turning ON light group: " + name);
        for (LightComponent light : lights) {
            light.turnOn();
        }
    }

    @Override
    public void turnOff() {
        System.out.println("Turning OFF light group: " + name);
        for (LightComponent light : lights) {
            light.turnOff();
        }
    }

    @Override
    public String getStatus() {
        return "Group '" + name + "':\n" +
                lights.stream()
                        .map(LightComponent::getStatus)
                        .collect(Collectors.joining("\n"));
    }
}
