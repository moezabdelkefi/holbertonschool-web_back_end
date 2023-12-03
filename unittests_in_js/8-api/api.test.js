const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
    let server;

    before((done) => {
        server = require('./api');
        done();
    });

    after((done) => {
        server.close(done);
    });

    it('responds with status 200', (done) => {
        request.get('http://localhost:7865/', (error, response) => {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('responds with correct message', (done) => {
        request.get('http://localhost:7865/', (error, response, body) => {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });

});
