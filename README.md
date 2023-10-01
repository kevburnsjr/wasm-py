# WASM demo: Javascript in Python 

Install esbuild for nodejs

```
npm install esbuild
```

Install wasmtime for python

```
pip install wasmtime
```

Bundle JS w/ esbuild

```
./node_modules/.bin/esbuild obfuscate.js --bundle --outfile=obfuscate.bundle.js --platform=browser --target=es6 --format=esm
```

Generate WASM from WIT + JS

```
node componentize.mjs
```

Generate Python bindings from WIT

```py
python3.10 -m wasmtime.bindgen obfuscate.component.wasm --out-dir obfuscate
```

Run it!

```py
python3.10 obfuscate.py socket.js
```

It works.

```
▶ make run
Python wasm: 0.198s
Node inner:  0.072s
Python node: 0.193s
```
