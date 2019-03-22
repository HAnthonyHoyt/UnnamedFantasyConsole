# The core CPU, which will run the game

from .memory import memory


def _get_top_8(value: int) -> int:
    return (value & 0xFF00) >> 8


def _get_8(value: int) -> int:
    return value & 0x00FF


def _get_16(value: int) -> int:
    return value & 0xFFFF


def _create_16(upper_8: int, lower_8: int):
    return (_get_8(upper_8) << 8) | _get_8(lower_8)


class CPU:
    class FLAGS:
        ZERO = 0x01
        CARRY = 0x02

    def __init__(self):
        self._a = 0
        self._b = 0
        self._c = 0
        self._d = 0
        self._e = 0
        self._f = 0
        self._g = 0
        self._h = 0

        # Bit flags
        self._fl = 0
        # Program Counter
        self._pc = 0
        # Stack pointer
        self._st = 0

        self.opcodes = [
            self.nop,

            self.add_a,
            self.add_b,
            self.add_c,
            self.add_d,
            self.add_e,
            self.add_f,
            self.add_g,
            self.add_h,

            self.sub_a,
            self.sub_b,
            self.sub_c,
            self.sub_d,
            self.sub_e,
            self.sub_f,
            self.sub_g,
            self.sub_h,

            self.lsh_a,
            self.lsh_b,
            self.lsh_c,
            self.lsh_d,
            self.lsh_e,
            self.lsh_f,
            self.lsh_g,
            self.lsh_h,

            self.rsh_a,
            self.rsh_b,
            self.rsh_c,
            self.rsh_d,
            self.rsh_e,
            self.rsh_f,
            self.rsh_g,
            self.rsh_h,
        ]

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = _get_8(value)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = _get_8(value)

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = _get_8(value)

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        self._d = _get_8(value)

    @property
    def e(self):
        return self._e

    @e.setter
    def e(self, value):
        self._e = _get_8(value)

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        self._f = _get_8(value)

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        self._g = _get_8(value)

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = _get_8(value)

    @property
    def ab(self):
        return _create_16(self._a, self._b)

    @ab.setter
    def ab(self, value):
        self._a = _get_top_8(value)
        self._b = _get_8(value)

    @property
    def cd(self):
        return _create_16(self._c, self._d)

    @cd.setter
    def cd(self, value):
        self._c = _get_top_8(value)
        self._d = _get_8(value)

    @property
    def ef(self):
        return _create_16(self._e, self._f)

    @ef.setter
    def ef(self, value):
        self._e = _get_top_8(value)
        self._f = _get_8(value)

    @property
    def gh(self):
        return _create_16(self._g, self._h)

    @gh.setter
    def gh(self, value):
        self._g = _get_top_8(value)
        self._h = _get_8(value)

    @property
    def fl(self):
        return self._fl

    @property
    def pc(self):
        return self._pc

    @pc.setter
    def pc(self, value):
        self._pc = _get_16(value)

    @property
    def st(self):
        return self._st

    @st.setter
    def st(self, value):
        self._st = _get_16(value)

    def dump(self):
        print("A  B  C  D  E  F  G  H  FL   PC   ST")
        print("{:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:04X} {:04X} {:04X}".format(
            self.a, self.b, self._c, self._d, self._e, self._f, self._g, self._h, self._fl, self._pc, self._st))

    def clock(self, ticks: int):
        # Be allowed one clock cycle to tick
        opcode = self.get_value_inc()
        command = self.opcodes[opcode]
        command()

    def get_mem_pc(self) -> int:
        # Get memory at the current program counter
        return _get_8(memory.memory[self.pc])

    def get_value_inc(self) -> int:
        # Get a value at the current position and increment the pc counter
        value = self.get_mem_pc()
        self.pc += 1

        return value

    def nop(self):
        # No-operation
        pass

    def add_a(self):
        # Add the value to the A register
        value = self.get_value_inc()
        self.a += value

    def add_b(self):
        # Add the value to the B register
        value = self.get_value_inc()
        self.b += value

    def add_c(self):
        # Add the value to the C register
        value = self.get_value_inc()
        self.c += value

    def add_d(self):
        # Add the value to the D register
        value = self.get_value_inc()
        self.d += value

    def add_e(self):
        # Add the value to the E register
        value = self.get_value_inc()
        self.e += value

    def add_f(self):
        # Add the value to the F register
        value = self.get_value_inc()
        self.f += value

    def add_g(self):
        # Add the value to the G register
        value = self.get_value_inc()
        self.g += value

    def add_h(self):
        # Add the value to the H register
        value = self.get_value_inc()
        self.h += value

    def sub_a(self):
        # Subtract the value to the A register
        value = self.get_value_inc()
        self.a -= value

    def sub_b(self):
        # Subtract the value to the B register
        value = self.get_value_inc()
        self.b -= value

    def sub_c(self):
        # Subtract the value to the C register
        value = self.get_value_inc()
        self.c -= value

    def sub_d(self):
        # Subtract the value to the D register
        value = self.get_value_inc()
        self.d -= value

    def sub_e(self):
        # Subtract the value to the E register
        value = self.get_value_inc()
        self.e -= value

    def sub_f(self):
        # Subtract the value to the F register
        value = self.get_value_inc()
        self.f -= value

    def sub_g(self):
        # Subtract the value to the G register
        value = self.get_value_inc()
        self.g -= value

    def sub_h(self):
        # Subtract the value to the H register
        value = self.get_value_inc()
        self.h -= value

    def lsh_a(self):
        # Shift to the left once the value to the A register
        self.a <<= 1

    def lsh_b(self):
        # Shift to the left once the value to the B register
        self.b <<= 1

    def lsh_c(self):
        # Shift to the left once the value to the C register
        self.c <<= 1

    def lsh_d(self):
        # Shift to the left once the value to the D register
        self.d <<= 1

    def lsh_e(self):
        # Shift to the left once the value to the E register
        self.e <<= 1

    def lsh_f(self):
        # Shift to the left once the value to the F register
        self.f <<= 1

    def lsh_g(self):
        # Shift to the left once the value to the G register
        self.g <<= 1

    def lsh_h(self):
        # Shift to the left once the value to the H register
        self.h <<= 1

    def rsh_a(self):
        # Shift to the right once the value to the A register
        self.a >>= 1

    def rsh_b(self):
        # Shift to the right once the value to the B register
        self.b >>= 1

    def rsh_c(self):
        # Shift to the right once the value to the C register
        self.c >>= 1

    def rsh_d(self):
        # Shift to the right once the value to the D register
        self.d >>= 1

    def rsh_e(self):
        # Shift to the right once the value to the E register
        self.e >>= 1

    def rsh_f(self):
        # Shift to the right once the value to the F register
        self.f >>= 1

    def rsh_g(self):
        # Shift to the right once the value to the G register
        self.g >>= 1

    def rsh_h(self):
        # Shift to the right once the value to the H register
        self.h >>= 1
