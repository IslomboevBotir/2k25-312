package uz.pdp.core.patterns.proxy;

import lombok.RequiredArgsConstructor;
import uz.pdp.subsystems.security.SecuritySystem;

public class SecuritySystemProxy implements ISecuritySystem {

    private final SecuritySystem realSystem;

    private final String adminPassword;

    public SecuritySystemProxy(String adminPassword) {
        this.realSystem = new SecuritySystem();
        this.adminPassword = adminPassword;
    }

    private boolean authenticate(String password) {
        return this.adminPassword.equals(password);
    }

    @Override
    public void armSystem() {
        System.out.println("Arming command received. Arming system.");
        realSystem.armSystem();
    }

    @Override
    public void disarmSystem(String password) {
        if (authenticate(password)) {
            System.out.println("Authenticated successful.");
            realSystem.disarmSystem(password);
        } else  {
            System.out.println("Authentication failed! Access denied.");
        }
    }

    @Override
    public void triggerAlarm(String location) {
        realSystem.triggerAlarm(location);
    }

    @Override
    public String getStatus() {
        return realSystem.getStatus();
    }
}
