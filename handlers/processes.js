const ps = require('ps-node');

//will look up all processes currently happening

ps.lookup({

}, function(err, resultList) {
  if (err) {
    throw new Error(err);
  }
  resultList.forEach(function(process) {
    if (process.command === '/Applications/Google') {
      console.log("Found one!");
    }
  })
})
