const env = require('node-env-file')(__dirname + '/.env');
const { checkFiles, contains } = require('./handlers/fileReader');
const { sendNotification } = require('./handlers/notifier');
const { execute, open, openManyFiles } = require('./handlers/execution');
const { lookupCommand } = require('./handlers/processes');

const { DESIRED, appToKeyword } = require('./models/constants');

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

FOR A SINGLE PROCESS:
 *checks if they're currently open
*/

function singleApplication() {
  lookupCommand(DESIRED[0], function() {
    const files = checkFiles(file => contains(file, appToKeyword(DESIRED[0])));
    console.log(files);
    if (files) {
      sendNotification('click on me!', 'I have some files for you!', files, openManyFiles);
    }
  })
}

//FOR LATER IF NEEDED
// function multipleApplications() {
//   DESIRED.forEach((application) => {
//     lookupCommand(DESIRED[0], function() {
//       const files = checkFiles(file => contains(file, appToKeyword(DESIRED[0])));
//       console.log(files);
//       if (files) {
//         sendNotification('click on me!', 'I have some files for you!', files, openManyFiles);
//       }
//     })
//   })
// }

multipleApplications();
