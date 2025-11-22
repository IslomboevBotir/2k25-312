from modules.lighting.lighting_system import LightingModule
from modules.transport.traffic_system import TransportModule
from modules.security.security_system import SecurityModule
from modules.energy.energy_monitor import EnergyModule

class ModuleFactory:
    @staticmethod
    def create_module(kind: str):
        if kind == 'lighting':
            return LightingModule()
        elif kind == 'transport':
            return TransportModule()
        elif kind == 'security':
            return SecurityModule()
        elif kind == 'energy':
            return EnergyModule()
        else:
            raise ValueError("Noma'lum modul turi: " + str(kind))
