import kue from 'kue';

const queue = kue.createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

/**
 * Sends notification and tracks job progress.
 * @param {string} phoneNumber - The recipient's phone number.
 * @param {string} message - The message content.
 * @param {object} job - The job object.
 * @param {function} done - The callback function to mark job as complete.
 */
function sendNotification(phoneNumber, message, job, done) {
  // Set the job progress to 0%
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    // Mark job as failed if the phone number is blacklisted
    console.log(`Notification job ${job.id} failed: Phone number ${phoneNumber} is blacklisted`);
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Update the job progress to 50%
  job.progress(50, 100);

  // Log the notification being sent
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Mark job as complete
  console.log(`Notification job ${job.id} completed`);
  return done();
}

// Process jobs in the queue with a concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

