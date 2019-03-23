import hexdump

from .logger import logger


def hex2int(hex_value: str) -> int:
    return int(hex_value, 16)


class Memory:
    _MEMORY_SIZE = 64 * 1024

    def __init__(self):
        self.memory = bytearray(self._MEMORY_SIZE + 1)

    def load(self, data, offset=0):
        self.memory[offset:offset+len(data)] = data
    
    def mem_print(self, offset, length):
        logger.debug("Mem Dump from {} for {} bytes".format(offset, length))
        hex_gen = hexdump.hexdump(self.memory[offset:offset + length], result='generator')
        [logger.debug(x) for x in hex_gen]


memory = Memory()
