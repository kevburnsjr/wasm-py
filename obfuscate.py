from obfuscate import Root
from wasmtime import Store
import sys

def main():
    input = open("input/"+sys.argv[1], "r")
    store = Store()
    demo = Root(store)
    out = demo.obfuscate(store, input.read())
    output = open("output/"+sys.argv[1], "w")
    output.write(out)

if __name__ == '__main__':
    main()
