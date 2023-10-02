from obfuscate import Root
from wasmtime import Store
import sys
import time

def main():
    input = open("input/"+sys.argv[1], "r")
    store = Store()
    src = input.read()
    demo = Root(store)
    n = 40
    a = time.perf_counter()

    # Multiple runs, single instance (crashes)
    for x in range(n):
        out = demo.obfuscate(store, src)

    print(f"Python wasm crash:  {(time.perf_counter() - a)/n:0.3f}s")
    output = open("output/"+sys.argv[1], "w")
    output.write(out)

if __name__ == '__main__':
    main()
