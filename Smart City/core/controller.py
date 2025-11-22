"""
Shahar Controlleri - Markaziy boshqaruv tizimi
Implementatsiya: 
- Singleton Pattern: Faqat bitta controller instance
- Facade Pattern: Barcha quyi tizimlarga soddalashtirilgan interfeys
"""

from modules.lighting.lighting_system import LightingSystem
from modules.transport.traffic_system import TrafficSystemFactory
from modules.security.security_system import SecuritySystemBuilder
from modules.energy.energy_monitor import EnergyMonitor
from core.adapters.weather_adapter import WeatherAdapter
from core.proxy.system_proxy import SystemAccessProxy

class CityController:
    """
    SINGLETON PATTERN: Shahar controllerining yagona instance
    FACADE PATTERN: Barcha shahar quyi tizimlariga yagona interfeys
    """
    _instance = None
    
    def __new__(cls):
        """Singleton implementatsiyasi - faqat bitta instance"""
        if cls._instance is None:
            cls._instance = super(CityController, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Barcha quyi tizimlarni faqat bir marta initsializatsiya qilish"""
        if self._initialized:
            return
            
        print("🔧 Shahar quyi tizimlari sozlanmoqda...")
        
        # Quyi tizimlarni initsializatsiya qilish
        self.lighting = LightingSystem()
        
        # Factory Method Pattern - transport tizimini yaratish
        self.traffic = TrafficSystemFactory.create_traffic_system("urban")
        
        # Builder Pattern - xavfsizlik tizimini qurish
        builder = SecuritySystemBuilder()
        self.security = (builder
                        .add_cameras(10)
                        .add_sensors(25)
                        .add_alarms(5)
                        .set_central_station("Markaziy boshqaruv")
                        .build())
        
        # Energiya monitoringi
        self.energy = EnergyMonitor()
        
        # Adapter Pattern - tashqi ob-havo servisini integratsiya qilish
        self.weather = WeatherAdapter()
        
        # Proxy Pattern - muhim tizimlarga nazorat qilingan kirish
        self.secure_access = SystemAccessProxy(self)
        
        self._initialized = True
        print("✅ Barcha quyi tizimlar tayyor!")
    
    @classmethod
    def get_instance(cls):
        """Controllerning singleton instance qaytar"""
        return cls()
    
    def control_lighting(self, action, value=None):
        """Yoritishni boshqarish uchun facade metod"""
        if action == "on":
            self.lighting.turn_on_all()
        elif action == "off":
            self.lighting.turn_off_all()
        elif action == "brightness" and value is not None:
            self.lighting.set_brightness(value)
        elif action == "auto":
            self.lighting.enable_auto_mode()
    
    def manage_traffic(self, mode):
        """Transportni boshqarish uchun facade metod"""
        if mode == "normal":
            self.traffic.set_normal_mode()
        elif mode == "rush_hour":
            self.traffic.set_rush_hour_mode()
        elif mode == "emergency":
            self.traffic.set_emergency_mode()
        elif mode == "status":
            self.traffic.display_status()
    
    def manage_security(self, action):
        """Xavfsizlikni boshqarish uchun facade metod"""
        if action == "arm":
            self.security.arm_system()
        elif action == "disarm":
            self.security.disarm_system()
        elif action == "cameras":
            self.security.check_cameras()
        elif action == "alerts":
            self.security.show_alerts()
    
    def monitor_energy(self):
        """Barcha tizimlar bo'ylab energiya sarfini kuzatish"""
        print("\n⚡ Energiya sarfi hisoboti:")
        total = self.energy.get_total_consumption()
        breakdown = self.energy.get_consumption_breakdown()
        
        for system, consumption in breakdown.items():
            print(f"  {system}: {consumption} kWh")
        print(f"  JAMI: {total} kWh")
        
        # Samaradorlikni tekshirish
        if total > 1000:
            print("⚠️  Yuqori sarflash aniqlandi! Energiya tejash rejimini ko'rib chiqing.")
        else:
            print("✅ Energiya sarfi normal oralig'ida.")
    
    def check_sensors(self):
        """Ob-havo va atrof-muhit sensorlarini tekshirish"""
        print("\n🌡️  Atrof-muhit monitoringi:")
        weather_data = self.weather.get_weather_data()
        print(f"  Harorat: {weather_data['temperature']}°C")
        print(f"  Namlik: {weather_data['humidity']}%")
        print(f"  Holat: {weather_data['conditions']}")
        
        # Ob-havoga qarab tizimlarni avtomatik sozlash
        if weather_data['temperature'] < 10:
            print("  🔥 Isitish tizimlari yoqilmoqda...")
        elif weather_data['temperature'] > 30:
            print("  ❄️  Sovutish tizimlari yoqilmoqda...")
    
    def emergency_alert(self, message):
        """Barcha quyi tizimlarga favqulodda ogohlantirishni uzatish"""
        print(f"\n🚨 FAVQULODDA HOLAT: {message}")
        self.traffic.set_emergency_mode()
        self.security.arm_system()
        self.lighting.turn_on_all()
        print("✅ Barcha tizimlar favqulodda rejimga o'tkazildi!")
    
    def generate_report(self):
        """Shaharning to'liq holat hisobotini yaratish"""
        print("\n" + "="*60)
        print("📊 SMARTCITY HOLAT HISOBOTI")
        print("="*60)
        
        print("\n💡 Yoritish tizimi:")
        self.lighting.display_status()
        
        print("\n🚦 Transport tizimi:")
        self.traffic.display_status()
        
        print("\n🔒 Xavfsizlik tizimi:")
        self.security.display_status()
        
        print("\n⚡ Energiya monitori:")
        self.monitor_energy()
        
        print("\n" + "="*60)