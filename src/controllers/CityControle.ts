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
