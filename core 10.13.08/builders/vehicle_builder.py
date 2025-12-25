class Vehicle:
    def __init__(self):
        self.specs = {}
    def __repr__(self):
        return f"Vehicle({self.specs})"

class VehicleBuilder:
    def __init__(self):
        pass

    def create_bus(self, plate):
        v = Vehicle()
        self._add_chassis(v)
        self._add_engine(v)
        self._add_electronics(v)
        v.specs['plate'] = plate
        return v

    def _add_chassis(self, v):
        v.specs['chassis'] = 'standard_bus_chassis'

    def _add_engine(self, v):
        v.specs['engine'] = 'diesel_v6'

    def _add_electronics(self, v):
        v.specs['telemetry'] = True
