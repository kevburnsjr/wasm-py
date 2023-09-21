# WASM demo: Javascript in Python 

Install esbuild

```
npm install esbuild
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

It fails.

```
▶ python3.10 obfuscate.py socket.js
Traceback (most recent call last):
  File "/mnt/f/web/junk/wasm-py/obfuscate.py", line 14, in <module>
    main()
  File "/mnt/f/web/junk/wasm-py/obfuscate.py", line 9, in main
    out = demo.obfuscate(store, input.read())
  File "/mnt/f/web/junk/wasm-py/obfuscate/__init__.py", line 26, in obfuscate
    ret = self.lift_callee0(caller, ptr, len0)
  File "/home/kev/.local/lib/python3.10/site-packages/wasmtime/_func.py", line 91, in __call__
    with enter_wasm(store) as trap:
  File "/usr/lib/python3.10/contextlib.py", line 142, in __exit__
    next(self.gen)
  File "/home/kev/.local/lib/python3.10/site-packages/wasmtime/_func.py", line 264, in enter_wasm
    raise trap_obj
wasmtime._trap.Trap: error while executing at wasm backtrace:
    0: 0x57fbec - <unknown>!<wasm function 6688>
    1: 0x582661 - <unknown>!<wasm function 7282>
    2: 0x33719c - <unknown>!<wasm function 603>
    3: 0x57f91f - <unknown>!obfuscate

Caused by:
    wasm trap: wasm `unreachable` instruction executed
```