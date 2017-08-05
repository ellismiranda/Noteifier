var util = require('util')
var exec = require('child_process').exec;

function puts(error, stdout, stderr) { util.puts(stdout) }

function execute(command) {
  exec(command, puts);
}

function open(path) {
  const cmd = `open ${path}`;
  execute(cmd);
}

module.exports = {
  execute,
  open
}
