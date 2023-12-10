const redis = require('redis');

const subscriber = redis.createClient();

subscriber.on('connect', () => {
    console.log('Redis client connected to the server');

    subscriber.subscribe('holberton school channel');
})

subscriber.on('error', (error) => {
    console.log('Redis client not connected to the server: ERROR MESSAGE');
})

subscriber.on('messsage', (chnannel, message) => {
    console.log(`Received message on channel ${channel}: ${message}`);

    if (message == 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
});

