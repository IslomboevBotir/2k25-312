package uz.pdp.subsystems.security;

import lombok.Getter;
import uz.pdp.core.patterns.proxy.ISecuritySystem;

@Getter
public class SecuritySystem implements ISecuritySystem {

    private boolean isArmed = true;

    @Override
    public void armSystem() {
        if (!isArmed) {
            isArmed = true;
            System.out.println("Security system has been ARMED.");
        } else {
            System.out.println("Info: Security system is already armed.");
        }
    }

    @Override
    public void disarmSystem(String password) {
        if (isArmed) {
            isArmed = false;
            System.out.println("Security system has been DISARMED.");
            System.out.println("DEBUG: The 'isArmed' variable is now: " + this.isArmed);
        } else {
            System.out.println("Info: Security system is already disarmed.");
        }
    }

    @Override
    public void triggerAlarm(String location) {
        System.out.println("!!! SECURITY ALERT !!! Alarm triggered at: " + location);
    }

    @Override
    public String getStatus() {
        return "Security System is " + (isArmed ? "ARMED" : "DISARMED");
    }
}
