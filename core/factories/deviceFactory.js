class LightingFactory {
  createDevice() {
    return {
      name: "Smart Light",
      status: () => "ON – 90% brightness"
    };
  }
}

class TransportFactory {
  createDevice() {
    return {
      name: "Smart Traffic Light",
      status: () => "GREEN – movement allowed"
    };
  }
}

const DeviceFactoryProvider = {
  getFactory(type) {
    if (type === "lighting") return new LightingFactory();
    if (type === "transport") return new TransportFactory();
    return null;
  }
};

module.exports = DeviceFactoryProvider;
