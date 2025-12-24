class BusDepot:
    def __init__(self):
        self.type = 'bus_depot'
        self.buses = []

    def add_bus(self, bus):
        self.buses.append(bus)

    def status(self):
        return {'type': self.type, 'fleet': len(self.buses)}
