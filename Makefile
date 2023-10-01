build:
	@./node_modules/.bin/esbuild obfuscate.js --outfile=obfuscate.bundle.js --format=esm --bundle --minify
	@node componentize.mjs
	@python3.10 -m wasmtime.bindgen obfuscate.component.wasm --out-dir obfuscate

run:
	@python3.10 obfuscate.py socket.js
