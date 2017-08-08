const fs = require('fs');
const path  = require('path');

//this takes in a callback that checks for true or false and returns a list of files that meet that
function checkFiles(callback) {
  const files = fs.readdirSync(path.join(__dirname + '/../Documents/'));
  const filtered = files.filter(callback);
  return filtered;
}

//looks through a specific file for a keyword
function contains(file, keyword) {
  const p = path.join(__dirname + '/../Documents/') + file;
  const str = fs.readFileSync(p, 'utf8');
  const lowerCase = str.toLowerCase();
  return (lowerCase.includes(keyword));
}

module.exports = {
  checkFiles,
  contains,
}
