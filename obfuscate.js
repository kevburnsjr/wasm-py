const JavaScriptObfuscator = require('./javascript-obfuscator.js');

export const obfuscate = (src) => {
  return JavaScriptObfuscator.obfuscate(src).getObfuscatedCode();
}
