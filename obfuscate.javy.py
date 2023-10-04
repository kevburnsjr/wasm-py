from wasmtime import Engine, Store, Module, Linker, WasiConfig, Instance
import sys
import time

engine = Engine()

def main():
    module = Module.from_file(engine, "obfuscate.javy.wasm")

    store = Store(engine)
    wasi = WasiConfig()
    wasi.inherit_stdout()
    wasi.inherit_stdin()
    store.set_wasi(wasi)
    linker = Linker(engine)
    linker.define_wasi()
    
    a = time.perf_counter()
    instance = linker.instantiate(store, module)
    exports = instance.exports(store)
    exports["_start"](store)
    # print(list(exports.keys()))

    '''
    engine = Engine()

    linking1 = Module.from_file(engine, "obfuscate.d.javy.wasm")
    linking2 = Module.from_file(engine, "provider.d.javy.wasm")

    linker = Linker(engine)
    linker.define_wasi()

    store = Store(engine)
    wasi = WasiConfig()
    wasi.inherit_stdout()
    wasi.inherit_stdin()
    store.set_wasi(wasi)
    
    linking2 = linker.instantiate(store, linking2)
    linker.define_instance(store, "linking2", linking2)

    linking1 = linker.instantiate(store, linking1)
    # run = linking1.exports(store)["run"]
    # run(store)
    exports = linking1.exports(store)
    print(exports)
    # run(store)
    '''

    print(f"Python wasm javy:     {time.perf_counter() - a:0.3f}s")

if __name__ == '__main__':
    main()
