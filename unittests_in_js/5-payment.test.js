const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
    let consoleLogStub;

    beforeEach(() => {
        consoleLogStub = sinon.stub(console, 'log');
    });

    afterEach(() => {
        consoleLogStub.restore();
    });

    it('should log the correct message for 100 and 20', () => {
        sendPaymentRequestToApi(100, 20);

        sinon.assert.calledOnce(consoleLogStub);
        sinon.assert.calledWithExactly(consoleLogStub, 'The total is: 120');
    });

    it('should log the correct message for 10 and 10', () => {
        sendPaymentRequestToApi(10, 10);

        sinon.assert.calledOnce(consoleLogStub);
        sinon.assert.calledWithExactly(consoleLogStub, 'The total is: 20');
    });
});
