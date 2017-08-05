const notifier = require('node-notifier');
const path = require('path');

function sendNotification(title, msg, callback) {
  notifier.notify({
    title: title,
    message: msg,
    icon: path.join(__dirname + '../assets/icon.png'),
    sound: true,
    wait: true,
  }, (err, response) => {

  })

  notifier.on('click', function(notifierObject, options) {
    // Triggers if `wait: true` and user clicks notification
    console.log('click');
    callback();
  })

  notifier.on('timeout', function(notifierObject, options) {
    // Triggers if `wait: true` and notification closes
    console.log('timeout');
    callback();
  })
}

module.exports = {
  sendNotification,
}
