var exec = require('child_process').exec;
var path = require('path');
const { accountForSpaces } = require('./tools');

function puts(error, stdout, stderr) { console.log(stdout) }

function execute(command) {
  exec(command, puts);
}

function open(path) {
  const cmd = `open ${path}`;
  execute(cmd);
}

function openManyFiles(files) {
  files.forEach((file) => {
    const p = path.join(__dirname + '/../Documents/') + accountForSpaces(file);
    console.log(p);
    open(p);
  })
}

module.exports = {
  execute,
  open,
  openManyFiles
}
