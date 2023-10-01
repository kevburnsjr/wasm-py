from obfuscate import Root
from obfuscator import Obfuscator
from wasmtime import Store
import sys
import time
import subprocess

def main():
    input = open("input/"+sys.argv[1], "r")
    store = Store()
    src = input.read()
    demo = Root(store)
    demo2 = Obfuscator()
    a = time.perf_counter()

    #########################################################
    #
    #   Single run, single instance (works but slow)
    #
    out = demo.obfuscate(store, src)
    t = time.perf_counter() - a

    #########################################################
    #
    #   Multiple runs, single instance (crashes)
    #
    # for x in range(40):
    #     out = demo.obfuscate(store, src)
    # t = (time.perf_counter() - a)/40

    #########################################################
    #
    #   Multiple runs, multiple instances (works and fast)
    #
    # for x in range(40):
    #     out = demo2.obfuscate(src)
    # t = (time.perf_counter() - a)/40

    print(f"Python wasm: {t:0.3f}s")
    output = open("output/"+sys.argv[1], "w")
    output.write(out)
    a = time.perf_counter()
    subprocess.run(["node", "./test.js", "socket.js"])
    b = time.perf_counter()
    print(f"Python node: {b - a:0.3f}s")

if __name__ == '__main__':
    main()
