class BasicSecurity:
    def __init__(self):
        self.armed = True

    def perform_check(self, level):
        print(f'[Security] Performing {level} security check')
        return True

    def status(self):
        return {'armed': self.armed}
