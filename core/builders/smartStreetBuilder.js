class SmartStreetBuilder {
  constructor() {
    this.lamps = 0;
    this.cameras = 0;
    this.solarPanels = 0;
  }

  addLamps(n) {
    this.lamps = n;
    return this;
  }

  addCameras(n) {
    this.cameras = n;
    return this;
  }

  addSolarPanels(n) {
    this.solarPanels = n;
    return this;
  }

  build() {
    return {
      info: () =>
        `Lights: ${this.lamps}, Cameras: ${this.cameras}, Solar Panels: ${this.solarPanels}`
    };
  }
}

module.exports = SmartStreetBuilder;
