// 1-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
    describe('SUM operation', () => {
        it('should return the rounded sum of two numbers', () => {
            assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        });
    });

    describe('SUBTRACT operation', () => {
        it('should return the rounded subtraction of two numbers', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        });
    });

    describe('DIVIDE operation', () => {
        it('should return the rounded division of two numbers if the denominator is not zero', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        });

        it('should return "Error" when dividing by zero', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
        });
    });

    describe('Invalid operation', () => {
        it('should throw an error for an invalid operation type', () => {
            assert.throws(() => {
                calculateNumber('INVALID', 1.4, 4.5);
            }, Error);
        });
    });
});
