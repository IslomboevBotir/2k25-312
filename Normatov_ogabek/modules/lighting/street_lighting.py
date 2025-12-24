class StreetLighting:
    def __init__(self):
        self.type = 'street'
        self.on = False

    def toggle_all(self):
        self.on = not self.on
        print(f'[Lighting] Street lights turned {"on" if self.on else "off"}')

    def status(self):
        return {'type':self.type, 'on': self.on}
