package uz.pdp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import uz.pdp.core.patterns.proxy.SecuritySystemProxy;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class ProxyTest {

    private SecuritySystemProxy proxy;

    @BeforeEach
    void setUp() {
        proxy = new SecuritySystemProxy("correct");
    }

    @Test
    @DisplayName("Test security proxy denies access with wrong password")
    void testProxyDeniesAccess() {
        assertTrue(proxy.getStatus().contains("ARMED"),
                "System should start in ARMED state.");

        proxy.disarmSystem("wrong");

        assertTrue(proxy.getStatus().contains("ARMED"),
                "System should remain ARMED after failed auth.");
    }

    @Test
    @DisplayName("Test security proxy grants access with correct password")
    void testProxyGrantsAccess() {
        assertTrue(proxy.getStatus().contains("ARMED"),
                "System should start in ARMED state.");

        proxy.disarmSystem("correct");

        assertTrue(proxy.getStatus().contains("ARMED"),
                "System should be DISARMED after correct password.");
    }
}
