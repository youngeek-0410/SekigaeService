const glob = require('glob');
const path = require('path');

module.exports = function getEntries(entry) {
  let ret = {}
  const filePaths = glob.sync(`${entry}/*.tsx`)
  filePaths.forEach(filePath => { ret[path.basename(filePath, path.extname(filePath))] = filePath })
  return ret
}