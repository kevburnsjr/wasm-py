build:
	@./node_modules/.bin/esbuild obfuscate.js --outfile=obfuscate.bundle.js --format=esm --bundle --minify
	@./node_modules/.bin/jco componentize obfuscate.bundle.js --wit obfuscate.wit -n obfuscate -o obfuscate.component.wasm
	@python3.10 -m wasmtime.bindgen obfuscate.component.wasm --out-dir obfuscate

run: run-tiny run-small run-med run-large run-huge

run-tiny:
	@echo ""
	@echo "Running tiny sample: 2KB"
	@python3.10 obfuscate-node.py socket.js
	@python3.10 obfuscate-uni.py socket.js
	@# python3.10 obfuscate-crash.py socket.js
	@python3.10 obfuscate-multi.py socket.js

run-small:
	@echo ""
	@echo "Running small sample: 17KB"
	@python3.10 obfuscate-node.py react-router.min.js
	@python3.10 obfuscate-uni.py react-router.min.js
	@# python3.10 obfuscate-crash.py react-router.min.js
	@python3.10 obfuscate-multi.py react-router.min.js

run-med:
	@echo ""
	@echo "Running medium sample: 55KB"
	@python3.10 obfuscate-node.py fullpage.min.js
	@python3.10 obfuscate-uni.py fullpage.min.js
	@# python3.10 obfuscate-crash.py fullpage.min.js
	@python3.10 obfuscate-multi.py fullpage.min.js

run-large:
	@echo ""
	@echo "Running large sample: 400KB"
	@python3.10 obfuscate-node.py chart.js
	@python3.10 obfuscate-uni.py chart.js
	@# python3.10 obfuscate-crash.py chart.js
	@python3.10 obfuscate-multi.py chart.js

run-huge:
	@echo ""
	@echo "Running huge sample: 1.9MB"
	@python3.10 obfuscate-node.py obfuscate.bundle.js
	@python3.10 obfuscate-uni.py obfuscate.bundle.js
	@# python3.10 obfuscate-crash.py obfuscate.bundle.js
	@python3.10 obfuscate-multi.py obfuscate.bundle.js
