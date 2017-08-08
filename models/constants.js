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
      return 'safaszcxa';
  }
}

module.exports = {
  DESIRED,
  appToKeyword,
}
