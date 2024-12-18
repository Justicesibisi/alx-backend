0x03. Queuing System in JS
About
Running Redis server locally
Caching data using redis and node-redis
Handling async operations with redis
Using Kue as queue system
Building an express app that interacts with a redis server
Building an express app that interacts with Redis server and queue
Tasks

## file 0: Install a Redis Instance

### Steps
- Downloaded and compiled Redis version 6.0.10.
- Started the Redis server and confirmed it was running using `ping`.
- Set the key `ALX` to the value `School`.
- Verified the value retrieval using `get ALX`.
- Stopped the Redis server and copied `dump.rdb` to the project root.

### Commands Used
```bash
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make
src/redis-server &
src/redis-cli
# Inside the Redis client:
# ping
# set ALX School
# get ALX
kill [PID_OF_Redis_Server]
cp dump.rdb ..

File: 1-redis_op.js
Extension of 1-redis_op.js that modifies displaySchoolValue function to work using promises.

File: 2-redis_op_async.js
Script that sets redis hashes using node-redis and prints the response using redis.print

File: 4-redis_advanced_op.js
Pub-Sub model in redis:

Script that creates a redis client and subscribes it to holberton school channel
Scripts that creates a redis client that published to holberton school channel
Files:
5-subscriber.js
5-publisher.js
Job creation using kue

File: 6-job_creator.js
Job processing using kue

File: [6-job_processor.js]
Tracking job progress and errors with kue - job creator

File: 7-job_creator.js
Tracking job progress and errors with kue - job processor

File: 7-job_processor.js
Job creation function createPushNotificationsJobs

File: 8-job.js
Unit tests for createPushNotificationsJobs

File: 8-job.test.js
Express orders API server that uses redis for caching:

Routes:
GET /list_products/: returns a list of all products.
GET /list_products/:itemId: returns information about products with specified id.
GET /list/reserve_product/:itemId: reservers one unit of product with given item id if present and in stock.
File: 9-stock.js
Express seat reservation API server that uses redis for job queues:

Routes:
GET /available_seats: returns the number of available seats.
GET /reserve_seat: seat reservation endpoint.
GET /process: reservation jobs processing endpoint.
Files: 100-seat.js
