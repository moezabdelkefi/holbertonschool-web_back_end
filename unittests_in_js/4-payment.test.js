const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
    let consoleLogStub;
    let calculateNumberStub;

    beforeEach(() => {
        consoleLogStub = sinon.stub(console, 'log');
        calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    });

    afterEach(() => {
        consoleLogStub.restore();
        calculateNumberStub.restore();
    });

    it('should call Utils.calculateNumber with correct arguments using stub', () => {
        sendPaymentRequestToApi(100, 20);

        sinon.assert.calledOnceWithExactly(
            calculateNumberStub,
            'SUM',
            100,
            20
        );
    });

    it('should log the correct message with the stubbed result', () => {
        sendPaymentRequestToApi(100, 20);

        sinon.assert.calledOnceWithExactly(
            consoleLogStub,
            'The total is: 10'
        );
    });
});
