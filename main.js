const readline = require("readline");

// --- Singleton + Facade ---
const CityController = require("./core/singleton/cityController");

// --- Builder ---
const SmartStreetBuilder = require("./core/builders/smartStreetBuilder");

// --- Proxy pattern ---
const createEnergyProxy = require("./core/proxy/energyProxy");

// --- Subsystems ---
const lightingSystem = require("./modules/lighting/lightingSystem");
const transportSystem = require("./modules/transport/transportSystem");

// --- Logging (Decorator) ---
const withLogging = (fn) => {
  return function (...args) {
    console.log(`[LOG] ${fn.name || "Function"} ishga tushdi`);
    return fn.apply(this, args);
  };
};

// --- Controllerni yaratish ---
const controller = CityController.getInstance();

// --- Subsystemlarni ro‘yxatdan o‘tkazish ---
controller.register("lighting", {
  turnOnAll: withLogging(lightingSystem.turnOnAll)
});

controller.register("transport", {
  emergencyStop: withLogging(transportSystem.emergencyStop)
});

// Boshlang‘ich energy system (guest)
let currentEnergySystem = createEnergyProxy("guest");
controller.register("energy", currentEnergySystem);

// --- Smart Street yaratish ---
const mainStreet = new SmartStreetBuilder()
  .addLamps(35)
  .addCameras(12)
  .addSolarPanels(20)
  .build();

// --- Konsol interaktiv menyu ---
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function showMenu() {
  console.log("\n" + "=".repeat(45));
  console.log("        SMART CITY BOSHQARUV PANELI");
  console.log("=".repeat(45));
  console.log("1. Barcha chiroqlarni yoqish");
  console.log("2. Favqulodda transportni to‘xtatish");
  console.log("3. Energiya hisoboti");
  console.log("4. Admin rejimga o‘tish");
  console.log("5. Smart ko‘cha ma'lumotlari");
  console.log("6. Energiya rejimini o‘zgartirish (eco / max)");
  console.log("0. Chiqish");
  console.log("-".repeat(45));

  rl.question("Tanlovingiz: ", handleChoice);
}

function handleChoice(choice) {
  switch (choice) {
    case "1":
      controller.turnOnAllLights();
      break;

    case "2":
      controller.emergencyStopTraffic();
      break;

    case "3":
      console.log(controller.getEnergyReport());
      break;

    case "4":
      // Admin rejim
      currentEnergySystem = createEnergyProxy("admin");
      controller.register("energy", currentEnergySystem);
      console.log("ADMIN rejimi yoqildi!");
      break;

    case "5":
      console.log(mainStreet.info());
      break;

    case "6":
      rl.question("Yangi rejim (eco / max): ", (mode) => {
        controller.setEnergyMode(mode);
        showMenu();
      });
      return;

    case "0":
      console.log("\nSmartCity o‘chirildi. Xayr!");
      rl.close();
      return;

    default:
      console.log("Noto‘g‘ri tanlov!");
  }

  setTimeout(showMenu, 700);
}

// --- Dastur ishga tushishi ---
console.clear();
console.log("SmartCity tizimi ishga tushdi!\n");

console.log("Ishlatilgan Design Patternlar:");
console.log("• Singleton");
console.log("• Facade");
console.log("• Builder");
console.log("• Decorator");
console.log("• Proxy");

showMenu();
