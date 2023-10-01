from obfuscate import _decode_utf8, _encode_utf8, _load
import ctypes
import pathlib
import wasmtime

class Obfuscator:

    def __init__(self) -> None:
        path = pathlib.Path(__file__).parent / ('obfuscate/root.core0.wasm')
        self._store = wasmtime.Store()
        self._module = wasmtime.Module.from_file(self._store.engine, path)
    def obfuscate(self, src: str) -> str:
        instance = wasmtime.Instance(self._store, self._module, []).exports(self._store)
        memory = instance["memory"]
        realloc = instance["cabi_realloc"]
        lift_callee = instance["obfuscate"]
        ptr, len0 = _encode_utf8(src, realloc, memory, self._store)
        ret = lift_callee(self._store, ptr, len0)
        load = _load(ctypes.c_int32, memory, self._store, ret, 0)
        load1 = _load(ctypes.c_int32, memory, self._store, ret, 4)
        ptr2 = load
        len3 = load1
        list = _decode_utf8(memory, self._store, ptr2, len3)
        del instance
        return list
