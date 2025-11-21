# 🧩 Lab Work №1: SmartCity System

Ushbu loyiha `Lab Work №1` doirasida ishlab chiqilgan `Smart City` boshqaruv tizimining `console`ga asoslangan simulyatsiyasidir. Tizim yoritish, xavfsizlik va energiya boshqaruvi kabi turli shahar `subsystem`larini birlashtiradi va markaziy `console interface` orqali boshqariladi. Asosiy `architecture` mustahkamlik, kengaytiriluvchanlik va qo'llab-quvvatlanuvchanlikni ta'minlash uchun bir nechta fundamental `object-oriented design pattern`lar asosida qurilgan.

## 📘 Vazifa Tavsifi

`SmartCity System` — bu aqlli shahar boshqaruvi tizimining ishlashini simulyatsiya qiluvchi `console` dasturi. Tizim yoritish, transport, xavfsizlik, energiya tejash, monitoring va boshqa shahar infratuzilmasi funksiyalari uchun mas'ul bo'lgan turli `subsystem`larni o'z ichiga oladi. Har bir `subsystem` loyihaning `architecture` barqarorligi va kengaytiriluvchanligini ta'minlaydigan `design pattern`lar yordamida amalga oshirilgan.

---

## ⚙️ Asosiy Funksionallik

*   **Markazlashtirilgan Boshqaruv:** Barcha shahar `subsystem`larini yagona `controller` boshqaradi.
*   **Holat Hisoboti:** Istalgan vaqtda barcha shahar tizimlarining to'liq holati haqida hisobot olish.
*   **Avtomatlashtirilgan Rejimlar:** `"Night Mode"` (barcha chiroqlarni yoqish, xavfsizlikni `ARMED` holatiga o'tkazish) va `"Day Mode"` (chiroqlarni o'chirish) rejimlarini faollashtirish.
*   **Favqulodda Protokollar:** Shahar bo'ylab favqulodda signalni ishga tushirish, bu barcha chiroqlarni yoqadi va xavfsizlik signallarini faollashtiradi.
*   **Ierarxik Yoritish:** Alohida ko'cha chiroqlarini yoki butun tumanlarni yagona buyruq bilan boshqarish.
*   **Xavfsiz Kirish:** Xavfsizlik tizimi `Proxy` orqali himoyalangan, u `disarming` kabi nozik operatsiyalar uchun parol talab qiladi.
*   **Tashqi Servis Integratsiyasi:** Tashqi ob-havo `servis`i energiya sarfini optimallashtirishga yordam berish uchun `Adapter` orqali `integratsiya` qilingan.

---

## 🧩 Amalga Oshirilgan Dizayn Patternlar

Ushbu loyiha mustahkam va kengaytiriladigan `architecture`ni qurish uchun oltita `design pattern`ni muvaffaqiyatli amalga oshiradi. Har bir `pattern` aniq va muhim maqsadga xizmat qiladi.

### 1. Singleton (Creational)
*   **Maqsadi:** `SmartCityController` `class`idan butun dastur davomida faqat bitta `instance` mavjud bo'lishini ta'minlash. Bu markazlashtirilgan tizim uchun juda muhim, chunki u bir nechta ziddiyatli boshqaruv nuqtalarining oldini oladi.
*   **Amalga Oshirilishi:** `SmartCityController` `class`i `private constructor`ga va yagona, umumiy `instance`ni qaytaradigan `static getInstance()` `method`iga ega.

### 2. Facade (Structural)
*   **Maqsadi:** Murakkab `subsystem`larga (yoritish, xavfsizlik, energiya, transport) soddalashtirilgan, yuqori darajali `interface` taqdim etish. Tizim `client`lari (`Main` `class`i kabi) har bir `subsystem`ning tafsilotlarini bilish o'rniga, `controller.activateNightMode()` kabi oddiy `method`lar bilan ishlaydi.
*   **Amalga Oshirilishi:** `SmartCityController` `class`i `Facade` vazifasini bajaradi, turli `subsystem`lar o'rtasidagi o'zaro ta'sirni boshqaradi va foydalanuvchiga toza `API` taqdim etadi.

### 3. Factory Method (Creational)
*   **Maqsadi:** Tizimni o'zi yaratishi kerak bo'lgan obyektlarning aniq `class`laridan ajratish. `Controller` yorug'lik moslamalarini yaratishi kerak, lekin u `LED` yoki `Halogen` kabi aniq turga bog'lanib qolmasligi lozim. Bu `pattern` kelajakda `controller` kodini o'zgartirmasdan yangi turdagi qurilmalarni qo'shish imkonini beradi.
*   **Amalga Oshirilishi:** `DeviceFactory` `interface`i yaratish `method`ini e'lon qiladi va `LEDLightFactory` uning `concrete` implementatsiyasidir. `Controller` `SingleLight` obyektlarini yaratish uchun ushbu `factory`dan foydalanadi.

### 4. Composite (Structural)
*   **Maqsadi:** Obyektlarni qism-butun ierarxiyasini ifodalash uchun daraxtsimon tuzilmalarga birlashtirish. Bu `pattern` bizga alohida obyektlarni (bitta chiroq) va obyektlar kompozitsiyasini (chiroqlar guruhi, masalan, ko'cha yoki tuman) bir xilda ko'rib chiqish imkonini beradi.
*   **Amalga Oshirilishi:**
    *   `LightComponent` — umumiy `interface`.
    *   `SingleLight` — alohida qurilmani ifodalovchi "leaf" (barg) tuguni.
    *   `LightGroup` — boshqa `LightComponent` obyektlarini (alohida chiroqlar yoki boshqa guruhlar) o'z ichiga oladigan "composite" (murakkab) tugun. Bu butun shaharga bitta buyruq bilan `turnOn()` `method`ini chaqirish imkonini beradi.

### 5. Proxy (Structural)
*   **Maqsadi:** Boshqa obyektga kirishni nazorat qilish uchun uning o'rnini bosuvchi yoki "vakil" (placeholder) taqdim etish. Biz bu `pattern`ni `SecuritySystem`ni himoyalash uchun ishlatamiz. `SecuritySystemProxy` so'rovlarni qabul qiladi, autentifikatsiya tekshiruvini (parol uchun) amalga oshiradi va shundan keyingina chaqiruvni haqiqiy `SecuritySystem` obyektiga yo'naltiradi.
*   **Amalga Oshirilishi:**
    *   `ISecuritySystem` — umumiy `interface`.
    *   `SecuritySystem` — nozik `logic`aga ega "real subject".
    *   `SecuritySystemProxy` — "real subject"ga kirishni nazorat qiluvchi "proxy".

### 6. Adapter (Structural)
*   **Maqsadi:** Mos kelmaydigan `interface`larga ega bo'lgan obyektlarning birgalikda ishlashiga imkon berish. Bizning `EnergyManager` haroratni Selsiyda (`Celsius`) olishni kutadi, ammo bizda uni Farengeytda (`Fahrenheit`) taqdim etadigan faraziy `ExternalWeatherService` mavjud. `Adapter` tashqi `servis`ni "o'rab oladi" va ma'lumotlar formatini o'zgartiradi.
*   **Amalga Oshirilishi:**
    *   `IWeatherProvider` — bizning tizimimiz ishlatadigan "target" (maqsadli) `interface`.
    *   `ExternalWeatherService` — mos kelmaydigan `interface`ga ega "adaptee".
    *   `WeatherServiceAdapter` — `IWeatherProvider`ni `implement` qiladigan va chaqiruvlarni tarjima qiladigan `class`.

---

## 🧱 Loyiha Tuzilmasi

Loyiha standart `Java` konvensiyalariga rioya qilgan holda `modular` strukturaga ega.

```
.
├── build.gradle
├── settings.gradle
└── src
    ├── main
    │   └── java
    │       └── uz/pdp
    │           ├── Main.java                 # Dasturga kirish nuqtasi
    │           ├── core
    │           │   ├── SmartCityController.java  # Facade, Singleton
    │           │   └── patterns
    │           │       ├── adapter/            # Adapter Pattern
    │           │       ├── factory/            # Factory Method Pattern
    │           │       └── proxy/              # Proxy Pattern
    │           └── subsystems
    │               ├── energy/               # Energiya Boshqaruvchisi
    │               ├── lighting/             # Yoritish Tizimi (Composite)
    │               ├── security/             # Xavfsizlik Tizimi
    │               └── transport/            # Transport Boshqaruvchisi
    └── test
        └── java
            └── uz/pdp
                ├── AdapterTest.java
                ├── CompositeTest.java
                ├── FactoryTest.java
                ├── ProxyTest.java
                └── SingletonTest.java
```

---

## 🛠️ Ishlatilgan Texnologiyalar

*   **Dasturlash tili:** Java 21
*   **Build vositasi:** Gradle
*   **Testlash:** JUnit 5
*   **Qo'shimcha vositalar:** Lombok

---

## 🚀 O'rnatish va Foydalanish

### Talablar

*   Java Development Kit (JDK) 21 yoki undan yuqori versiyasi.

### Loyihani `Build` qilish

Terminalda loyihaning asosiy papkasiga o'ting va `Gradle`ning `build` buyrug'ini bajaring. Bu kodni `compile` qiladi va barcha `unit test`larni ishga tushiradi.

```bash
# macOS/Linux uchun
./gradlew clean build

# Windows uchun
gradlew.bat clean build
```

### Dasturni Ishga Tushirish

`Console`ga asoslangan boshqaruv tizimini ishga tushirish uchun `Gradle`ning `run` buyrug'idan foydalaning.

```bash
# macOS/Linux uchun
./gradlew run

# Windows uchun
gradlew.bat run
```

### `Unit Test`larni Ishga Tushirish

Faqat `unit test`larni bajarish uchun `Gradle`ning `test` buyrug'idan foydalaning.

```bash
# macOS/Linux uchun
./gradlew test

# Windows uchun
gradlew.bat test
```