const DESIRED = [
  '/Applications/Google',
  '/Applications/RuneScape.app/Contents/MacOS/RuneScape',
];

function appToKeyword(app) {
  switch (app) {
    case '/Applications/RuneScape.app/Contents/MacOS/RuneScape':
      return '[rs]';
    case '/Applications/Google':
      return '[chrome]';
    default:
      return '';
  }
}

function appToName(app) {
  switch (app) {
    case '/Applications/RuneScape.app/Contents/MacOS/RuneScape':
      return 'RuneScape';
    case '/Applications/Google':
      return 'Google Chrome';
    default:
      return '';
  }
}

module.exports = {
  DESIRED,
  appToKeyword,
  appToName
}
