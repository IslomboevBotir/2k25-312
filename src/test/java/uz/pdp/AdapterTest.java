package uz.pdp;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import uz.pdp.core.patterns.adapter.ExternalWeatherService;
import uz.pdp.core.patterns.adapter.WeatherServiceAdapter;

import static org.junit.jupiter.api.Assertions.assertEquals;

class AdapterTest {
    @Test
    @DisplayName("Test weather adapter correctly converts Fahrenheit to Celsius (Adapter Pattern)")
    void testAdapterConversion() {
        ExternalWeatherService externalService = new ExternalWeatherService(); // Returns 77°F
        WeatherServiceAdapter adapter = new WeatherServiceAdapter(externalService);
        
        double expectedCelsius = 25.0;
        double actualCelsius = adapter.getTemperatureCelsius();
        
        assertEquals(expectedCelsius, actualCelsius, 0.01, "Adapter should convert 77°F to 25°C.");
    }
}
