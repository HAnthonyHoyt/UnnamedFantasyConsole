import argparse

from src.cpu import CPU
from src.memory import Memory


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

    cpu.a = 32
    cpu.b = 32 * 2 + 1
    cpu.c = 32 * 3 + 1
    cpu.d = 32 * 4 + 1
    cpu.e = 32 * 5 + 1
    cpu.f = 32 * 6 + 1
    cpu.g = 32 * 7 + 1
    cpu.h = 32 * 8 + 1

    cpu.dump()

    cpu.ab = 32 * 9
    cpu.cd = 32 * 10
    cpu.ef = 32 * 11
    cpu.gh = 32 * 12
    cpu.pc = 32 * 13
    cpu.st = 32 * 14

    cpu.dump()


if __name__ == '__main__':
    main()
