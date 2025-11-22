import random

class EnergyMonitor:
    
    def __init__(self):
        self.systems = {
            "Yoritish": 0,
            "Transport": 0,
            "Xavfsizlik": 0,
            "Boshqalar": 0
        }
        self._update_consumption()
        print("⚡ Energiya monitoring tizimi ishga tushdi")
    
    def _update_consumption(self):
        self.systems["Yoritish"] = random.randint(200, 400)
        self.systems["Transport"] = random.randint(150, 300)
        self.systems["Xavfsizlik"] = random.randint(100, 200)
        self.systems["Boshqalar"] = random.randint(50, 150)
    
    def get_total_consumption(self):
        self._update_consumption()
        return sum(self.systems.values())
    
    def get_consumption_breakdown(self):
        return self.systems
    
    def optimize_consumption(self):
        print("\n🔋 Energiya tejash rejimi yoqilmoqda...")
        for system in self.systems:
            reduction = random.randint(10, 20)
            old_value = self.systems[system]
            self.systems[system] = int(old_value * (1 - reduction/100))
            print(f"  {system}: {old_value} -> {self.systems[system]} kWh ({reduction}% tejaldi)")
    
    def display_report(self):
        print("\n⚡ Energiya sarfi hisoboti:")
        total = self.get_total_consumption()
        for system, consumption in self.systems.items():
            percentage = (consumption / total) * 100
            print(f"  {system}: {consumption} kWh ({percentage:.1f}%)")
        print(f"  JAMI: {total} kWh")