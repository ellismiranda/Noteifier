const DESIRED = [
  '/Applications/RuneScape.app/Contents/MacOS/RuneScape'
];

function appToKeyword(app) {
  switch (app) {
    case '/Applications/RuneScape.app/Contents/MacOS/RuneScape':
      return '[rs]';
    default:
      return 'safaszcxa';
  }
}

module.exports = {
  DESIRED,
  appToKeyword,
}
