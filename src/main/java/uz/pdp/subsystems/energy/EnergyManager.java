package uz.pdp.subsystems.energy;

import lombok.RequiredArgsConstructor;
import uz.pdp.core.patterns.adapter.IWeatherProvider;

@RequiredArgsConstructor
public class EnergyManager {

    private final IWeatherProvider weatherProvider;

    public void optimizeEnergyUsage() {
        double temp = weatherProvider.getTemperatureCelsius();
        System.out.printf("Current temperature is %.2fC. Adjusting energy consumption...\n", temp);
        if (temp > 25.0) {
            System.out.println("-> High temperature detected. Increasing cooling system power.");
        } else if (temp < 10.0) {
            System.out.println("-> Low temperature detected. Increasing heating system power.");
        } else {
            System.out.println("-> Moderate temperature. Operating in power-saving mode.");
        }
    }
}
