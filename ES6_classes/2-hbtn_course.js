class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this._validateString(name, 'Name');
    this._length = this._validateNumber(length, 'Length');
    this._students = this._validateStudents(students);
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = this._validateString(newName, 'Name');
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    this._length = this._validateNumber(newLength, 'Length');
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    this._students = this._validateStudents(newStudents);
  }

  _validateString(value, propName) {
    if (typeof value !== 'string') {
      throw new TypeError(`${propName} must be a string`);
    }
    return value;
  }

  _validateNumber(value, propName) {
    if (typeof value !== 'number' || Number.isNaN(value)) {
      throw new TypeError(`${propName} must be a number`);
    }
    return value;
  }

  _validateStudents(value) {
    if (!Array.isArray(value) || !value.every((item) => typeof item === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    return value;
  }
}

export default HolbertonCourse;
