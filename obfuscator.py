from obfuscate import _decode_utf8, _encode_utf8, _load
import ctypes
import pathlib
import math
import wasmtime

class Obfuscator:

    def __init__(self) -> None:
        path = pathlib.Path(__file__).parent / ('obfuscate/root.core0.wasm')
        self._store = wasmtime.Store()
        self._module = wasmtime.Module.from_file(self._store.engine, path)
    def obfuscate(self, src: str) -> str:
        instance = wasmtime.Instance(self._store, self._module, [])
        exports = instance.exports(self._store)
        memory = exports["memory"]
        realloc = exports["cabi_realloc"]
        lift_callee = exports["obfuscate"]
        # print(f"Mem Size:   {memory.size(self._store)}")
        # print(f"Mem Len:    {memory.data_len(self._store)}")
        # print(f"Src Len:    {len(src)}")
        # print(f"Src Pages:  {math.ceil(len(src) / 65536)}")
        # memory.grow(self._store, math.ceil((len(src)) / 65536)*4)
        # exports = instance.exports(self._store)
        # memory = exports["memory"]
        # print(f"Mem Size:   {memory.size(self._store)}")
        # print(f"Mem Len:    {memory.data_len(self._store)}")
        ptr, sz = _encode_utf8(src, realloc, memory, self._store)
        ret = lift_callee(self._store, ptr, sz)
        ptr = _load(ctypes.c_int32, memory, self._store, ret, 0)
        sz = _load(ctypes.c_int32, memory, self._store, ret, 4)
        list = _decode_utf8(memory, self._store, ptr, sz)
        # print(f"Mem Size:   {memory.size(self._store)}")
        # print(f"Mem Len:    {memory.data_len(self._store)}")
        del instance
        return list
