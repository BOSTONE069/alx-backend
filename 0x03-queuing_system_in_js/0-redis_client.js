import redis from 'redis';

const client = redis.createClient({host: 'localhost', port: 6379});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
    console.log('Redis client connected to the server')
});