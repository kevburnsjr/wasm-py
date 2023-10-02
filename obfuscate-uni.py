from obfuscate import Root
from wasmtime import Store
import sys
import time

def main():
    input = open("input/"+sys.argv[1], "r")
    store = Store()
    src = input.read()
    demo = Root(store)
    a = time.perf_counter()

    # Single run, single instance (works but slow)
    out = demo.obfuscate(store, src)

    print(f"Python wasm module:   {time.perf_counter() - a:0.3f}s")
    output = open("output/"+sys.argv[1], "w")
    output.write(out)

if __name__ == '__main__':
    main()
