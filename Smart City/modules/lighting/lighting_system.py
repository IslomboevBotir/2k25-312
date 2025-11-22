class StreetLight:
    
    def __init__(self, light_id, location):
        self.id = light_id
        self.location = location
        self.is_on = False
        self.brightness = 0
    
    def turn_on(self):
        self.is_on = True
        self.brightness = 100
        
    def turn_off(self):
        self.is_on = False
        self.brightness = 0
    
    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            self.is_on = level > 0


class LightingSystem:
    
    def __init__(self):
        self.lights = self._initialize_lights()
        self.auto_mode = False
        print(f"💡 Yoritish tizimi {len(self.lights)} ta chiroq bilan ishga tushdi")
    
    def _initialize_lights(self):
        locations = [
            "Asosiy ko'cha", "Park yo'li", "Broadway", "5-chi prospekt",
            "Markaziy maydon","Universitet hududi", "Turar-joy hududi", "Savdo markazi"
        ]
        return [StreetLight(i+1, loc) for i, loc in enumerate(locations)]
    
    def turn_on_all(self):
        for light in self.lights:
            light.turn_on()
        print("✅ Barcha ko'cha chiroqlari YOQILDI")
        self.auto_mode = False
    
    def turn_off_all(self):
        for light in self.lights:
            light.turn_off()
        print("✅ Barcha ko'cha chiroqlari O'CHIRILDI")
        self.auto_mode = False
        
    def display_status(self):
        on_count = sum(1 for light in self.lights if light.is_on)
        avg_brightness = sum(light.brightness for light in self.lights) / len(self.lights)
        
        print(f"  Yongan chiroqlar: {on_count}/{len(self.lights)}")
        print(f"  O'rtacha yorug'lik: {avg_brightness:.1f}%")
        print(f"  Avto rejim: {'Yoqilgan' if self.auto_mode else 'O`chirilgan'}")