class CityController {
  constructor() {
    if (CityController.instance) {
      return CityController.instance;
    }
    this.subsystems = new Map();
    CityController.instance = this;
  }

  static getInstance() {
    if (!CityController.instance) {
      CityController.instance = new CityController();
    }
    return CityController.instance;
  }

  register(name, subsystem) {
    this.subsystems.set(name, subsystem);
  }

  turnOnAllLights() {
    this.subsystems.get("lighting")?.turnOnAll();
  }

  emergencyStopTraffic() {
    this.subsystems.get("transport")?.emergencyStop();
  }

  getEnergyReport() {
    return this.subsystems.get("energy")?.getReport();
  }

  setEnergyMode(mode) {
    this.subsystems.get("energy")?.setMode(mode);
  }
}

module.exports = CityController;
