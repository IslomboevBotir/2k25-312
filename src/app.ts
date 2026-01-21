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
