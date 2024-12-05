import { createClient } from 'redis';

// Create the Redis client
const client = createClient();

// Handle connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connect to the Redis server
client.connect();
