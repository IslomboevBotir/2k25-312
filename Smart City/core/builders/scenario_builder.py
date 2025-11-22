class Scenario:
    def __init__(self, name, steps):
        self.name = name
        self.steps = steps

    def run(self):
        print(f"\nSsenariy ishga tushirilmoqda: {self.name}")
        for i, step in enumerate(self.steps, 1):
            print(f' Bosqich {i}...')
            step()

class ScenarioBuilder:
    def __init__(self):
        self._name = "Noma'lum"
        self._steps = []

    def set_name(self, name: str):
        self._name = name
        return self

    def add_step(self, func):
        self._steps.append(func)
        return self

    def build(self):
        return Scenario(self._name, self._steps)
