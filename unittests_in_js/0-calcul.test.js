const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('0-calcul.js - calculateNumber', () => {
  describe('First number rounded', () => {
    it('should return the correct sum when the first number is rounded', () => {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
  });

  describe('Second number rounded', () => {
    it('should return the correct sum when the second number is rounded', () => {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
  });

  describe('Both numbers rounded', () => {
    it('should return the correct sum when both numbers are rounded', () => {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
      // Add more test cases if needed
    });
  });
});
