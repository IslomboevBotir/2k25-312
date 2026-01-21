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
