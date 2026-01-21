// SmartCity – 6 ta pattern bir faylda (talabga to'liq mos)

// 1. Singleton + 2. Facade
class CityController {
  private static instance: CityController;
  private subsystems: Map<string, any> = new Map();

  private constructor() {}

  static getInstance(): CityController {
    if (!CityController.instance) {
      CityController.instance = new CityController();
    }
    return CityController.instance;
  }

  register(name: string, subsystem: any) {
    this.subsystems.set(name, subsystem);
  }

  // Facade metodlari
  turnOnAllLights() {
    this.subsystems.get('lighting')?.turnOnAll();
  }
  emergencyStopTraffic() {
    this.subsystems.get('transport')?.emergencyStop();
  }
  getEnergyReport() {
    return this.subsystems.get('energy')?.getReport();
  }
  adminSetEnergyMode(mode: string) {
    this.subsystems.get('energy')?.setMode(mode);
  }
}

// 3. Abstract Factory + Factory Method
interface DeviceFactory {
  createDevice(): { name: string; status(): string };
}

class LightingFactory implements DeviceFactory {
  createDevice() {
    return {
      name: "Smart Street Lamp",
      status: () => "Lamp ON – 80% brightness"
    };
  }
}

class TransportFactory implements DeviceFactory {
  createDevice() {
    return {
      name: "Smart Traffic Light",
      status: () => "Traffic Light: GREEN"
    };
  }
}

class DeviceFactoryProvider {
  static getFactory(type: 'lighting' | 'transport'): DeviceFactory {
    switch (type) {
      case 'lighting': return new LightingFactory();
      case 'transport': return new TransportFactory();
    }
  }
}

// 4. Builder pattern
class SmartStreetBuilder {
  private lamps: number = 0;
  private cameras: number = 0;
  private solarPanels: number = 0;

  addLamps(count: number) { this.lamps = count; return this; }
  addCameras(count: number) { this.cameras = count; return this; }
  addSolarPanels(count: number) { this.solarPanels = count; return this; }

  build() {
    return {
      description: "Smart Street",
      details: () => `Lamps: ${this.lamps} | Cameras: ${this.cameras} | Solar: ${this.solarPanels}`
    };
  }
}

// 5. Decorator pattern (logging qo'shish)
function withLogging<T extends (...args: any[]) => any>(fn: T): T {
  return ((...args: any[]) => {
    console.log(`[LOG] ${fn.name} chaqirildi →`, args);
    return fn(...args);
  }) as T;
}

// 6. Proxy pattern (faqat admin o'zgartira oladi)
interface EnergySystem {
  getReport(): string;
  setMode(mode: string): void;
}

class RealEnergySystem implements EnergySystem {
  private mode = "normal";
  getReport() {
    return `Energy mode: ${this.mode} | Consumption: 245 kWh`;
  }
  setMode(mode: string) {
    this.mode = mode;
    console.log(`Energy mode changed to: ${mode}`);
  }
}

function createSecureEnergyProxy(userRole: 'admin' | 'guest' = 'guest'): EnergySystem {
  const real = new RealEnergySystem();
  return new Proxy(real, {
    get(target, prop: keyof EnergySystem) {
      if (prop === 'setMode' && userRole !== 'admin') {
        return () => console.log("XATO: Faqat admin o'zgartira oladi!");
      }
      return target[prop];
    }
  });
}

// === ASOSIY DASTUR ===
async function main() {
  console.clear();
  console.log("SmartCity Tizimi – 6 ta Pattern\n");

  const controller = CityController.getInstance();

  // Zavodlar orqali qurilmalar yaratamiz
  const lamp = DeviceFactoryProvider.getFactory('lighting').createDevice();
  const traffic = DeviceFactoryProvider.getFactory('transport').createDevice();

  // Builder orqali ko'cha qurish
  const street = new SmartStreetBuilder()
    .addLamps(20)
    .addCameras(8)
    .addSolarPanels(15)
    .build();

  // Proxy orqali energiya tizimi
  const energyGuest = createSecureEnergyProxy('guest');
  const energyAdmin = createSecureEnergyProxy('admin');

  // Subsystemlarni ro'yxatga olish
  controller.register('lighting', {
    turnOnAll: withLogging(() => console.log("Barcha chiroqlar yoqildi"))
  });
  controller.register('transport', {
    emergencyStop: withLogging(() => console.log("Transport to'xtatildi!"))
  });
  controller.register('energy', energyGuest); // default guest

  let isAdmin = false;

  while (true) {
    console.log("\n1. Yoritish yoqish");
    console.log("2. Favqulodda transport to'xtatish");
    console.log("3. Energiya hisoboti");
    console.log("4. Admin panel (kirish)");
    console.log("5. Smart ko'cha ma'lumotlari");
    console.log("0. Chiqish");
    const choice = prompt("Tanlang: ")?.trim();

    if (choice === "1") controller.turnOnAllLights();
    if (choice === "2") controller.emergencyStopTraffic();
    if (choice === "3") console.log(controller.getEnergyReport());
    if (choice === "4") {
      isAdmin = true;
      controller.register('energy', energyAdmin);
      console.log("Admin rejimi yoqildi");
    }
    if (choice === "5") console.log(street.details());
    if (choice === "0") {
      console.log("Xayr!");
      break;
    }
  }
}

// Node.js uchun oddiy prompt
function prompt(question: string): string | null {
  const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  let result: string | null = null;
  readline.question(question, (ans: string) => {
    result = ans;
    readline.close();
  });
  require('deasync').loopWhile(() => result === null);
  return result;
}

main();
