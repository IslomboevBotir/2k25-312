package uz.pdp.subsystems.transport;

public class TransportManager {
    private int activeVehicles = 500;

    public void adjustTrafficFlow() {
        System.out.println("Optimizing traffic signals for " + activeVehicles + " active vehicles.");
    }

    public String getStatus() {
        return "Transport System: " + activeVehicles + " vehicles monitored.";
    }
}
