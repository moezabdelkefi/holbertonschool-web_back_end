const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('should return the sum of rounded numbers for integers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return the sum of rounded numbers for mixed integers and floats', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should return the sum of rounded numbers for floats', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  // Add more test cases for edge cases if needed
});
