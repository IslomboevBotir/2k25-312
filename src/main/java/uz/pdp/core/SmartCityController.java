package uz.pdp.core;

import uz.pdp.core.patterns.adapter.ExternalWeatherService;
import uz.pdp.core.patterns.adapter.IWeatherProvider;
import uz.pdp.core.patterns.adapter.WeatherServiceAdapter;
import uz.pdp.core.patterns.factory.DeviceFactory;
import uz.pdp.core.patterns.factory.LEDLightFactory;
import uz.pdp.core.patterns.proxy.SecuritySystemProxy;
import uz.pdp.subsystems.energy.EnergyManager;
import uz.pdp.subsystems.lighting.LightComponent;
import uz.pdp.subsystems.lighting.LightGroup;
import uz.pdp.subsystems.transport.TransportManager;

public class SmartCityController {

    private static final SmartCityController INSTANCE = new SmartCityController();

    public static SmartCityController getInstance() {
        return INSTANCE;
    }



    private final LightComponent mainStreetLights;
    private final LightComponent parkLights;
    private final LightComponent cityLightingSystem;
    private final SecuritySystemProxy securitySystem;
    private final EnergyManager energyManager;
    private final TransportManager transportManager;


    private SmartCityController() {
        this.securitySystem = new SecuritySystemProxy("admin123");
        this.transportManager = new TransportManager();

        IWeatherProvider weatherProvider = new WeatherServiceAdapter(new ExternalWeatherService());
        this.energyManager = new EnergyManager(weatherProvider);


        DeviceFactory ledFactory = new LEDLightFactory();

        LightGroup mainStreet = new LightGroup("Main Street");
        mainStreet.add(ledFactory.createLight(101));
        mainStreet.add(ledFactory.createLight(102));
        this.mainStreetLights = mainStreet;

        LightGroup park = new LightGroup("Central Park");
        park.add(ledFactory.createLight(201));
        this.parkLights = park;

        LightGroup city = new LightGroup("Entire City");
        city.add(mainStreetLights);
        city.add(parkLights);
        this.cityLightingSystem = city;
    }


    public void reportFullStatus() {
        System.out.println("\n--- SmartCity System Status Report ---");
        System.out.println(cityLightingSystem.getStatus());
        System.out.println(securitySystem.getStatus());
        System.out.println(transportManager.getStatus());
        energyManager.optimizeEnergyUsage();
        System.out.println("-------------------------------------\n");
    }

    public void activateNightMode() {
        System.out.println("\nActivating Night Mode...");
        cityLightingSystem.turnOn();
        securitySystem.armSystem();
        System.out.println("Night Mode activated.\n");
    }

    public void activateDayMode() {
        System.out.println("\nActivating Day Mode...");
        cityLightingSystem.turnOff();
        transportManager.adjustTrafficFlow();
        System.out.println("Day Mode activated.\n");
    }

    public void triggerEmergency(String location) {
        System.out.println("\n!!! EMERGENCY PROTOCOL INITIATED !!!");
        cityLightingSystem.turnOn();
        securitySystem.triggerAlarm(location);
        System.out.println("Emergency services have been notified.");
        System.out.println("!!! EMERGENCY PROTOCOL COMPLETE !!!\n");
    }

    public void disarmSecurity(String password) {
        securitySystem.disarmSystem(password);
    }
}
