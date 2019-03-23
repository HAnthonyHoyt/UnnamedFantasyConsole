# The graphics board, which will render the display
import pyxel


class Graphics:
    def __init__(self):
        pyxel.init(160, 160, caption="Unnamed Fantasy Portable Console")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, "This is the beginning", 7)

    def clock(self, ticks: int):
        pass
