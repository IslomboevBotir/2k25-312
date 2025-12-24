from modules.lighting.street_lighting import StreetLighting
from modules.lighting.office_lighting import OfficeLighting
from modules.transport.bus_depot import BusDepot
from modules.security.basic_security import BasicSecurity
from modules.energy.grid_manager import GridManager

class SubsystemFactory:
    def create_lighting_system(self, kind):
        # Factory Method: choose concrete Lighting
        if kind == 'street':
            return StreetLighting()
        else:
            return OfficeLighting()

    def create_transport_system(self, kind):
        if kind == 'bus_depot':
            return BusDepot()
        raise ValueError('unknown transport')

    def create_security_system(self):
        return BasicSecurity()

    def create_energy_system(self):
        return GridManager()
