class Currency {
  constructor(symbol, name) {
    this._symbol = symbol;
    this._name = name;
  }

  displayFullCurrency() {
    return `${this._name} (${this._symbol})`;
  }
}

export default Currency;
