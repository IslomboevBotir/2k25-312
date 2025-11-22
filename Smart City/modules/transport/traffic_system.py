class TrafficLight:
    
    def __init__(self, light_id, intersection):
        self.id = light_id
        self.intersection = intersection
        self.current_color = "RED"
        self.timer = 30
    
    def change_color(self, color):
        self.current_color = color
    
    def set_timer(self, seconds):
        self.timer = seconds


class TrafficSystem:
    
    def __init__(self, system_type):
        self.system_type = system_type
        self.traffic_lights = self._initialize_lights()
        self.current_mode = "normal"
        print(f"🚦 {system_type.capitalize()} transport tizimi ishga tushdi")
    
    def _initialize_lights(self):
        intersections = [
            "Markaziy chorraха", "Universitet chorrahasi", "Aeroport yo'li",
            "Shimoliy yo'nalish", "Janubiy yo'nalish", "Sharqiy yo'nalish",
            "G'arbiy yo'nalish", "Savdo markazi yaqini"
        ]
        return [TrafficLight(i+1, inter) for i, inter in enumerate(intersections)]
    
    def set_normal_mode(self):
        self.current_mode = "normal"
        for light in self.traffic_lights:
            light.set_timer(30)
        print("Oddiy rejim yoqildi - standart vaqt sozlamalari")
    
    def set_rush_hour_mode(self):
        self.current_mode = "rush_hour"
        for light in self.traffic_lights:
            light.set_timer(45)
        print("Rush hour rejimi - asosiy yo'nalishlarga ko'proq vaqt")
    
    def set_emergency_mode(self):
        self.current_mode = "emergency"
        for light in self.traffic_lights:
            light.change_color("GREEN")
            light.set_timer(10)
        print("Favqulodda rejim - barcha svetoforlar yashil!")
    
    def display_status(self):
        print(f"  Svetoforlar soni: {len(self.traffic_lights)}")
        print(f"  Joriy rejim: {self.current_mode}")
        print(f"  Tizim turi: {self.system_type}")


class TrafficSystemFactory:
    
    @staticmethod
    def create_traffic_system(city_type):
        if city_type == "urban":
            return TrafficSystem("urban")
        elif city_type == "suburban":
            return TrafficSystem("suburban")
        elif city_type == "highway":
            return TrafficSystem("highway")
        else:
            return TrafficSystem("urban")