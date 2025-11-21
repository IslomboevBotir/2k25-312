package uz.pdp.core.patterns.proxy;

public interface ISecuritySystem {
    void armSystem();
    void disarmSystem(String password);
    void triggerAlarm(String location);
    String getStatus();
}
