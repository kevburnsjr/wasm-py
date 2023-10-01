from obfuscate import Root
from wasmtime import Store
import sys
import time
import subprocess

def main():
    input = open("input/"+sys.argv[1], "r")
    store = Store()
    demo = Root(store)
    src = input.read()
    a = time.perf_counter()
    for x in range(10):
        out = demo.obfuscate(store, src)
    b = time.perf_counter()
    print(f"Python wasm: {(b - a)/10:0.3f}s")
    output = open("output/"+sys.argv[1], "w")
    output.write(out)
    a = time.perf_counter()
    subprocess.run(["node", "./test.js", "socket.js"])
    b = time.perf_counter()
    print(f"Python node: {b - a:0.3f}s")

if __name__ == '__main__':
    main()
