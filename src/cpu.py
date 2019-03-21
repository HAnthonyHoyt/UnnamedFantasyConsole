# The core CPU, which will run the game


class CPU:
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

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value & 0xFF

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value & 0xFF

    @property
    def ab(self):
        return (self._a << 8) | self._b

    @ab.setter
    def ab(self, value):
        self._a = value >> 8
        self._b = value & 0x00FF

    @property
    def cd(self):
        return (self._c << 8) | self._d

    @cd.setter
    def cd(self, value):
        self._c = value >> 8
        self._d = value & 0x00FF

    @property
    def ef(self):
        return (self._e << 8) | self._f

    @ef.setter
    def ef(self, value):
        self._e = value >> 8
        self._f = value & 0x00FF

    @property
    def gh(self):
        return (self._g << 8) | self._h

    @gh.setter
    def gh(self, value):
        self._g = value >> 8
        self._h = value & 0x00FF

    @property
    def fl(self):
        return self._fl

    @property
    def pc(self):
        return self._pc

    @pc.setter
    def pc(self, value):
        self._pc = value & 0xFFFF

    @property
    def st(self):
        return self._st

    @st.setter
    def st(self, value):
        self._st = value & 0xFFFF

    def dump(self):
        pass
        print("A  B  C  D  E  F  G  H  FL PC ST")
        print("{:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X}".format(
            self.a, self.b, self._c, self._d, self._e, self._f, self._g, self._h, self._fl, self._pc, self._st))
