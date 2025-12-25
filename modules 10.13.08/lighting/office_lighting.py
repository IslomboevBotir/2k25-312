class OfficeLighting:
    def __init__(self):
        self.type = 'office'
        self.on = True

    def toggle_all(self):
        self.on = not self.on
        print(f'[Lighting] Office lights turned {"on" if self.on else "off"}')

    def status(self):
        return {'type':self.type, 'on': self.on}
