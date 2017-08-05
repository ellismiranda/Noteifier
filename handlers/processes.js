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

function lookupCommand(command, callback) {
  let found = false;
  return ps.lookup({ }, (err, resultList) => {
    resultList.forEach((process) => {
      if (process.command === command && !found) {
        console.log("Found one!");
        callback();
      }
    })
  })
}

module.exports = {
  lookupCommand
}
