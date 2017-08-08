const ps = require('ps-node');

//will look up all processes currently happening

// ps.lookup({
//
// }, function(err, resultList) {
//   if (err) {
//     throw new Error(err);
//   }
//   resultList.forEach(function(process) {
//     if (process.command === '/Applications/Google') {
//       console.log("Found one!");
//     }
//   })
// })

function lookupAll(command, callback) {
  let found = false;
  ps.lookup({ }, (err, resultList) => {
    resultList.forEach((process) => {
      if (process.command === command && !found) {
        console.log("Found one!");
        found = true;
        callback();
      }
    })
  })
}

function lookupProcess(command, callback) {
  return ps.lookup({ command }, (err, resultList) => {
    const process = resultList[0];
    if (process) {
      callback();
    }
  })
}

module.exports = {
  lookupCommand,
  lookupAll
}
