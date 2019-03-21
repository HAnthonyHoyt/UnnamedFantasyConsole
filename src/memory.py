import hexdump


def hex2int(hex_value: str) -> int:
    return int(hex_value, 16)


class Memory:
    _MEMORY_SIZE = 64 * 1024

    class MODES:
        HEX = 1
        BIN = 2

    def __init__(self):
        self.memory = bytearray(self._MEMORY_SIZE + 1)

    def load(self, data, offset):
        self.memory[offset:offset+len(data)] = data
    
    def mem_print(self, offset, length):
        hexdump.hexdump(self.memory[offset:offset+length])
