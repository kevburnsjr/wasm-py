import { JavaScriptObfuscator } from 'javascript-obfuscator';

export const obfuscate = (src) => {
  console.log(src)
  return JavaScriptObfuscator.obfuscate(src);
}
