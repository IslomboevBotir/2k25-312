# 🏙️ SmartCity Sistema

Aqlli shahar boshqaruv tizimi - Python dasturi

## 📋 Loyiha haqida

SmartCity Sistema shaharning turli infratuzilma tizimlarini boshqarish uchun konsol dasturidir. Bu loyiha 6 ta design pattern yordamida qurilgan va OOP tamoyillariga amal qiladi.

## 🧩 Ishlatilgan Design Patternlar

### 1. **Singleton Pattern**
- **Fayl**: `core/controller.py`
- **Maqsad**: CityController klasidan faqat bitta instance yaratilishini ta'minlash
- **Sabab**: Shahar boshqaruv tizimi yagona bo'lishi kerak

### 2. **Facade Pattern**
- **Fayl**: `core/controller.py`
- **Maqsad**: Barcha murakkab quyi tizimlarga sodda interfeys berish
- **Sabab**: Foydalanuvchi uchun sodda va tushunarli boshqaruv

### 3. **Factory Method Pattern**
- **Fayl**: `modules/transport/traffic_system.py`
- **Maqsad**: Turli xil transport tizimlarini yaratish
- **Sabab**: Shahar turiga qarab turli transport tizimlari kerak

### 4. **Builder Pattern**
- **Fayl**: `modules/security/security_system.py`
- **Maqsad**: Murakkab xavfsizlik tizimini bosqichma-bosqich qurish
- **Sabab**: Xavfsizlik tizimi ko'p komponentlardan iborat

### 5. **Adapter Pattern**
- **Fayl**: `core/adapters/weather_adapter.py`
- **Maqsad**: Tashqi ob-havo servisini tizimga moslashtirish
- **Sabab**: Turli formatdagi ma'lumotlarni birlashtirilgan formatga o'tkazish

### 6. **Proxy Pattern**
- **Fayl**: `core/proxy/system_proxy.py`
- **Maqsad**: Muhim tizim resurslariga nazorat qilingan kirish
- **Sabab**: Xavfsizlik va loglash uchun

## 📁 Loyiha tuzilishi
```
SmartCity/
├── main.py
├── test.py
├── README.md
├── core/
│   ├── __init__.py
│   ├── controller.py
│   ├── adapters/
│   │   ├── __init__.py
│   │   └── weather_adapter.py
│   └── proxy/
│       ├── __init__.py
│       └── system_proxy.py
└── modules/
    ├── __init__.py
    ├── lighting/
    │   ├── __init__.py
    │   └── lighting_system.py
    ├── transport/
    │   ├── __init__.py
    │   └── traffic_system.py
    ├── security/
    │   ├── __init__.py
    │   └── security_system.py
    └── energy/
        ├── __init__.py
        └── energy_monitor.py
```