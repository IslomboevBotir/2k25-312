package uz.pdp.core.patterns.adapter;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class WeatherServiceAdapter implements IWeatherProvider {

    private final ExternalWeatherService externalService;

    @Override
    public double getTemperatureCelsius() {
        double tempFahrenheit = externalService.fetchTemperatureFahrenheit();
        // Convert Fahrenheit to Celsius
        return (tempFahrenheit - 32) * 5.0 / 9.0;
    }
}
