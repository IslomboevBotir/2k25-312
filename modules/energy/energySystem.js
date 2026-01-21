class EnergySystem {
  constructor() {
    this.mode = "normal"; // default rejim
    this.usage = 312; // kWh – misol uchun
  }

  // Energiya hisoboti
  getReport() {
    return `Energy mode: ${this.mode} | Usage: ${this.usage} kWh`;
  }

  // Rejimni o‘zgartirish
  setMode(mode) {
    this.mode = mode;
    console.log(`Energy mode changed to "${mode}"`);
  }
}

// Modul sifatida eksport qilamiz
module.exports = EnergySystem;
