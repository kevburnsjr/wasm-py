from obfuscator import Obfuscator
import sys
import time

def main():
    input = open("input/"+sys.argv[1], "r")
    src = input.read()
    demo = Obfuscator()
    n = 1
    a = time.perf_counter()

    # Multiple runs, multiple instances (works and fast)
    for x in range(n):
        out = demo.obfuscate(src)

    print(f"Python wasm instance: {(time.perf_counter() - a)/n:0.3f}s")
    output = open("output/"+sys.argv[1], "w")
    output.write(out)

if __name__ == '__main__':
    main()
