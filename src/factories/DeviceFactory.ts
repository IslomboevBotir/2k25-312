interface DeviceFactory {
  createDevice(): { name: string; status(): string };
}

class LightingFactory implements DeviceFactory {
  createDevice() {
    return { name: "Smart Street Lamp", status: () => "Lamp ON – 80% brightness" };
  }
}

class TransportFactory implements DeviceFactory {
  createDevice() {
    return { name: "Smart Traffic Light", status: () => "Traffic Light: GREEN" };
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
