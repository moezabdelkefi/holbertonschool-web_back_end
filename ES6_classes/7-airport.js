class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  toString() {
    return `[object ${this._code}]`;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  inspect() {
    return `Airport [${this._code}] { _name: '${this._name}', _code: '${this._code}' }`;
  }
}

export default Airport;
