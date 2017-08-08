const notifier = require('node-notifier');
const path = require('path');

function sendNotification(title, msg, files, callback) {
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
    callback(files);
  })

  notifier.on('timeout', function(notifierObject, options) {
    // Triggers if `wait: true` and notification closes
  })
}

module.exports = {
  sendNotification,
}
