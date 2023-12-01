// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  describe('first number rounded', () => {
    it('should return the rounded sum of two numbers when the first number is rounded', () => {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
  });

  describe('second number rounded', () => {
    it('should return the rounded sum of two numbers when the second number is rounded', () => {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });

  describe('both numbers rounded', () => {
    it('should return the rounded sum of two numbers when both numbers are rounded', () => {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
  });
});
