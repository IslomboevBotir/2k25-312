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
