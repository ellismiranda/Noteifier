const env = require('node-env-file')(__dirname + '/.env');
const { checkFiles, contains } = require('./handlers/fileReader');
const { sendNotification } = require('./handlers/notifier');
const { execute, open } = require('./handlers/execution');

const pathToDocs = __dirname + '/Documents/';
console.log(pathToDocs);

const files = checkFiles((file) => contains(file, 'hi'));

console.log(files);

sendNotification('CLICK ME', 'I\'m great!', (res) => {
  console.log('ugh');
});
