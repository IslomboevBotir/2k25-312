from .singleton import singleton
from core.factories.abstract_factory import SubsystemFactory
from core.builders.vehicle_builder import VehicleBuilder
from core.adapters.weather_adapter import WeatherAdapter
from core.proxy.security_proxy import SecurityProxy

@singleton
class CityController:
    def __init__(self):
        # initialize subsystems with Abstract Factory
        self.factory = SubsystemFactory()
        self.lighting = self.factory.create_lighting_system('street')
        self.transport = self.factory.create_transport_system('bus_depot')
        self.security = SecurityProxy(self.factory.create_security_system())
        self.energy = self.factory.create_energy_system()

        # builders registry
        self.builders = {'vehicle_builder': VehicleBuilder()}

        # adapter
        self.weather = WeatherAdapter()

    def start_console(self):
        print('Welcome to SmartCity Console')
        print('Type: status / toggle_light / create_vehicle / check_security / auth / exit')
        while True:
            cmd = input('> ').strip().lower()
            if cmd == 'status':
                self._show_status()
            elif cmd == 'toggle_light':
                self.lighting.toggle_all()
            elif cmd == 'create_vehicle':
                v = self.builders['vehicle_builder'].create_bus('B-100')
                print('Created vehicle:', v)
                self.transport.add_bus(v)
            elif cmd == 'check_security':
                self.security.perform_check('daily')
            elif cmd == 'auth':
                token = input('Enter token: ').strip()
                self.security.authenticate(token)
                print('Authenticated' if token else 'No token provided')
            elif cmd == 'exit':
                print('Shutting down...')
                break
            else:
                print('Unknown command')

    def _show_status(self):
        print('Lighting:', self.lighting.status())
        print('Transport:', self.transport.status())
        print('Security:', self.security.status())
        print('Energy:', self.energy.status())
