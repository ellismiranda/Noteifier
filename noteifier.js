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
} , 10000)


//COMMENTED OUT FOR LATER IF NEEDED
// function singleApplication(application, title, msg) {
//   lookupCommand(application, function() {
//     const files = checkFiles(file => contains(file, appToKeyword(application)));
//     if (files) {
//       sendNotification(title, msg, files, openManyFiles);
//     }
//   })
// }

//COMMENTED OUT FOR LATER IF NEEDED
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
