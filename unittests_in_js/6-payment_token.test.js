const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
    it('should resolve with a successful response when success is true', (done) => {
        getPaymentTokenFromAPI(true).then((response) => {
            expect(response).toEqual({ data: 'Successful response from the API' });
            done();
        });
    });

    it('should not resolve when success is false', (done) => {
        getPaymentTokenFromAPI(false).then((response) => {
            expect(response).toBeUndefined();
            done();
        });
    });
});
