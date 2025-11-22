import random
from datetime import datetime

class SecuritySystem:
    
    def __init__(self):
        self.cameras_count = 0
        self.sensors_count = 0
        self.alarms_count = 0
        self.central_station = ""
        self.is_armed = False
        self.alerts = []
    
    def arm_system(self):
        self.is_armed = True
        print(" Xavfsizlik tizimi qulflandi (ARMED)")
        self._generate_alert("Tizim qulflandi")
    
    def disarm_system(self):
        self.is_armed = False
        print(" Xavfsizlik tizimi ochildi (DISARMED)")
        self._generate_alert("Tizim ochildi")
    
    def check_cameras(self):
        working = random.randint(self.cameras_count - 2, self.cameras_count)
        print(f" Kameralar: {working}/{self.cameras_count} ishlayapti")
        if working < self.cameras_count:
            print(f"  {self.cameras_count - working} ta kamera texnik xizmat talab qiladi")
    
    def show_alerts(self):
        print("\n Oxirgi ogohlantirishlar:")
        if not self.alerts:
            print("  Ogohlantirishlar yo'q")
        else:
            for alert in self.alerts[-5:]:
                print(f"  - {alert}")
    
    def _generate_alert(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alert = f"[{timestamp}] {message}"
        self.alerts.append(alert)
    
    def display_status(self):
        print(f"  Kameralar: {self.cameras_count}")
        print(f"  Sensorlar: {self.sensors_count}")
        print(f"  Signalizatsiyalar: {self.alarms_count}")
        print(f"  Markaziy stansiya: {self.central_station}")
        print(f"  Holat: {'QULFLANGAN' if self.is_armed else 'OCHIQ'}")


class SecuritySystemBuilder:
    
    def __init__(self):
        self.security = SecuritySystem()
    
    def add_cameras(self, count):
        self.security.cameras_count = count
        return self
    
    def add_sensors(self, count):
        self.security.sensors_count = count
        return self
    
    def add_alarms(self, count):
        self.security.alarms_count = count
        return self
    
    def set_central_station(self, location):
        self.security.central_station = location
        return self
    
    def build(self):
        print(f" Xavfsizlik tizimi qurildi: {self.security.cameras_count} kamera, "
              f"{self.security.sensors_count} sensor")
        return self.security