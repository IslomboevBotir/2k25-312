class SystemAccessProxy:
    def __init__(self, real_controller):
        self.real_controller = real_controller
        self.access_log = []
    
    def log_access(self, operation, user="system"):
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] User: {user} - Operation: {operation}"
        self.access_log.append(log_entry)
        print(f"🔐 Kirish logi: {log_entry}")
    
    def emergency_shutdown(self, user="admin"):
        self.log_access("emergency_shutdown", user)
        
        if user != "admin":
            print(" Kirish rad etildi: Faqat admin huquqi")
            return False
        
        print("🚨 Favqulodda to'xtatish amalga oshirilmoqda...")
        self.real_controller.traffic.set_emergency_mode()
        self.real_controller.lighting.turn_on_all()
        return True
    
    def get_access_log(self):
        return self.access_log