class RealEnergySystem {
  constructor() {
    this.mode = "normal";
  }

  getReport() {
    return `Energy mode: ${this.mode} | Usage: 312 kWh`;
  }

  setMode(mode) {
    this.mode = mode;
    console.log(`Energy mode changed to ${mode}`);
  }
}

function createEnergyProxy(role = "guest") {
  const real = new RealEnergySystem();

  return new Proxy(real, {
    get(target, prop) {
      if (prop === "setMode" && role !== "admin") {
        return () => console.log("ERROR: Admin only!");
      }
      return target[prop];
    }
  });
}

module.exports = createEnergyProxy;
