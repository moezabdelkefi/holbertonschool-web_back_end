class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const clone = Object.assign(
      Object.create(Object.getPrototypeOf(this)),
      this,
    );
    clone[Symbol('brand')] = this._brand;
    clone[Symbol('motor')] = this._motor;
    clone[Symbol('color')] = this._color;
    return clone;
  }
}

export default Car;
