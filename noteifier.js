const env = require('node-env-file')(__dirname + '/.env');
const { checkFiles, contains } = require('./handlers/fileReader');
const { sendNotification } = require('./handlers/notifier');
const { execute, open } = require('./handlers/execution');
const { lookupCommand } = require('./handlers/processes');

const { DESIRED } = require('./models/constants');

const pathToDocs = __dirname + '/Documents/';

/*
for each of the processes in the list
  check processes
  if the processes you're looking for are newly opened
    read through the files to check for keywords
    if the file has the keyword add it to the list of files
      if there are any files, send the notification
        if the notification is clicked
          open the files

DESIRED.forEach(//do something);


sendNotification('CLICK ME', 'I\'m great!', (res) => {
  console.log('ugh');
});
