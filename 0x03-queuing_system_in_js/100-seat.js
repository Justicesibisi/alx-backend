import express from 'express';
import { createQueue } from 'kue';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const queue = createQueue();
const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

const PORT = 1245;
let reservationEnabled = true;

// Initialize Redis with 50 available seats
(async function initializeSeats() {
  await setAsync('available_seats', 50);
})();

// Helper to get current available seats
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10);
}

// Reserve a seat in Redis
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Route to get the current number of available seats
app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats.toString() });
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservations are blocked' });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

// Route to process the queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    if (availableSeats > 0) {
      await reserveSeat(availableSeats - 1);
      if (await getCurrentAvailableSeats() === 0) {
        reservationEnabled = false;
      }
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

