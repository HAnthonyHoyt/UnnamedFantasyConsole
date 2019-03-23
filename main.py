import argparse

from src.cpu import CPU
from src.logger import logger
from src.memory import memory


def main():
    parser = argparse.ArgumentParser(description='Unnamed Fantasy Console')
    parser.add_argument('--rom', type=str, required=True, help='The rom you wish to load')

    args = parser.parse_args()
    logger.info("Loading rom '{}'".format(args.rom))

    with open(args.rom, mode="rb") as rom_file:
        memory.load(rom_file.read())

    memory.mem_print(0, 20)

    cpu = CPU()

    for _ in range(1, 5):
        cpu.clock(_)

    cpu.dump()


if __name__ == '__main__':
    main()
