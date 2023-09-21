import { componentize } from '@bytecodealliance/componentize-js';
import { readFile, writeFile } from 'node:fs/promises';

const jsSource = await readFile('obfuscate.bundle.js', 'utf8');
const witSource = await readFile('obfuscate.wit', 'utf8');

const { component } = await componentize(jsSource.replace('self', 'this'), witSource);

await writeFile('obfuscate.component.wasm', component);
