module.exports = function calculateNumber(a, b) {
    const roundA = Number(a);
    const roundB = Number(b);

    if (Number.isNaN(roundA) || Number.isNaN(roundB))
        throw TypeError('Parameters must be numbers');

    return Math.round(roundA) + Math.round(roundB);
};