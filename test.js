const fs = require('fs');
const JavaScriptObfuscator = require('./javascript-obfuscator.js');
const arg = process.argv

try {
  const data = fs.readFileSync('./input/' + arg[2], 'utf8');
  var a = performance.now();
  var c = JavaScriptObfuscator.obfuscate(data).getObfuscatedCode();
  var b = performance.now();
  console.log("Node internal call:   " + (Math.round(b - a) / 1000).toFixed(3) + "s");
} catch (err) {
  console.error(err);
}
