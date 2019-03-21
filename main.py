import argparse

from src.memory import Memory
from src.cpu import CPU


def main():
    parser = argparse.ArgumentParser(description='Unnamed Fantasy Console')
    parser.add_argument('--rom', type=str, help='The rom you wish to load')

    args = parser.parse_args()
    print("Loading rom '{}'".format(args.rom))

    memory = Memory()
    with open(args.rom, mode="rb") as rom_file:
        memory.load(rom_file.read(), 10)

    memory.mem_print(0, 20)

    cpu = CPU()

    cpu.a = 8
    cpu.b = 257
    cpu.cd = 0xf66f

    cpu.dump()


if __name__ == '__main__':
    main()
