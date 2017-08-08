

function accountForSpaces(str) {
  const splitStr = str.split(' ');
  let fixed = splitStr[0];
  for (let i = 1; i < splitStr.length; i++) {
    fixed += '\\ ' + splitStr[i];
  }
  return fixed;
}


module.exports = {
  accountForSpaces,
}
