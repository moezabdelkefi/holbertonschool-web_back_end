// 0-calcul.test.js
const assert = require('assert');
const mocha = require('mocha');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function () {
  it('should round and sum two numbers', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should round and sum two numbers with decimals', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should round and sum two decimal numbers', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should round and sum two decimal numbers (another case)', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  // Add more test cases as needed
});