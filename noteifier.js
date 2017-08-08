const env = require('node-env-file')(__dirname + '/.env');
const { checkFiles, contains } = require('./handlers/fileReader');
const { sendNotification } = require('./handlers/notifier');
const { execute, open, openManyFiles } = require('./handlers/execution');
const { lookupProcess } = require('./handlers/processes');

const { DESIRED, appToKeyword, appToName } = require('./models/constants');

const pathToDocs = __dirname + '/Documents/';

/*
[X] for each of the processes in the list
[X]   check processes
[X]   if the processes you're looking for are newly opened*
[X]     read through the files to check for keywords
[X]     if the file has the keyword add it to the list of files
[X]       if there are any files, send the notification
[X]         if the notification is clicked
[X]           open the files
*/

let accountedFor = [];

//initial load of all open applications
DESIRED.forEach((application) => {
  lookupProcess(application, function() {
    accountedFor.push(application);
  })
})

//main process on an interval loop
setInterval( function() {
  DESIRED.forEach((application) => {
    if (!accountedFor.includes(application)) {
      lookupProcess(application, function() {
        const name = appToName(application);
        const files = checkFiles(file => contains(file, appToKeyword(application)));
        if (files) {
          accountedFor.push(application);
          sendNotification('Noteifier', `Click on me to open your notes about ${name}!`, files, openManyFiles);
        }
      })
    }
  })
}, 10000)
