from core.controller import CityController

def display_menu():
    """Asosiy menyuni ko'rsatish"""
    print("\n" + "="*50)
    print("🏙️  SMARTCITY BOSHQARUV TIZIMI")
    print("="*50)
    print("1.  Yoritish tizimini boshqarish")
    print("2.  Transport tizimini boshqarish")
    print("3.  Xavfsizlik tizimini boshqarish")
    print("4.  Energiya sarfini kuzatish")
    print("5.  Tizim hisobotini yaratish")
    print("6.  Ob-havo sensorlarini tekshirish")
    print("7.  Favqulodda holat ogohlantirish")
    print("0.  Chiqish")
    print("="*50)

def lighting_menu(controller):
    print("\n--- Yoritish tizimini boshqarish ---")
    print("1. Barcha chiroqlarni yoqish")
    print("2. Barcha chiroqlarni o'chirish")
    print("0. Orqaga")
    
    choice = input("\nTanlovingizni kiriting: ")
    
    if choice == "1":
        controller.control_lighting("on")
    elif choice == "2":
        controller.control_lighting("off")

def traffic_menu(controller):
    print("\n--- Transport tizimini boshqarish ---")
    print("1. Oddiy rejimga o'tish")
    print("2. Eng gavjum vaqt rejimiga o'tish")
    print("3. Favqulodda rejimni yoqish")
    print("4. Transport holatini tekshirish")
    print("0. Orqaga")
    
    choice = input("\nTanlovingizni kiriting: ")
    
    if choice == "1":
        controller.manage_traffic("normal")
    elif choice == "2":
        controller.manage_traffic("rush_hour")
    elif choice == "3":
        controller.manage_traffic("emergency")
    elif choice == "4":
        controller.manage_traffic("status")

def security_menu(controller):
    print("\n--- Xavfsizlik tizimini boshqarish ---")
    print("1. Tizimni qulflash")
    print("2. Tizim qulfini ochish")
    print("3. Kameralar holatini tekshirish")
    print("4. Oxirgi ogohlantirishlarni ko'rish")
    print("0. Orqaga")
    
    choice = input("\nTanlovingizni kiriting: ")
    
    if choice == "1":
        controller.manage_security("arm")
    elif choice == "2":
        controller.manage_security("disarm")
    elif choice == "3":
        controller.manage_security("cameras")
    elif choice == "4":
        controller.manage_security("alerts")

def main():
    print("\n🌆 SmartCity tizimi ishga tushmoqda...")
    
    controller = CityController.get_instance()
    
    print("✅ Tizim muvaffaqiyatli ishga tushdi!")
    
    while True:
        display_menu()
        choice = input("\nTanlovingizni kiriting: ")
        
        if choice == "1":
            lighting_menu(controller)
        elif choice == "2":
            traffic_menu(controller)
        elif choice == "3":
            security_menu(controller)
        elif choice == "4":
            controller.monitor_energy()
        elif choice == "5":
            controller.generate_report()
        elif choice == "6":
            controller.check_sensors()
        elif choice == "7":
            message = input("Favqulodda xabarni kiriting: ")
            controller.emergency_alert(message)
        elif choice == "0":
            print("\n👋 SmartCity tizimi o'chmoqda...")
            print("Xayr! 🌆")
            break
        else:
            print("\n Noto'g'ri tanlov! Qaytadan qilib ko'ring.")
        
        input("\nDavom etish uchun Enter bosing...")

if __name__ == "__main__":
    main()