import redis from 'redis';

const publisher = redis.createClient({host: 'localhost', port: 6379});

publisher.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

publisher.on('connect', () => {
  console.log('Redis client connected to the server');
})

const CHANNEL = 'holberton school channel';

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish(CHANNEL, message);
  }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);