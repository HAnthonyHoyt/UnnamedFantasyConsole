# The clock sends the clock notice to all the circuits, instructing them to act on one clock cycle


class Clock:
    def __index__(self):
        # The current 'tick'
        self.tick = 0
        # The list of components that we will call back
        self.components = []

    def bind(self, component: callable):
        self.components.append(component)

    # When the clock 'ticks' then all the components can act for that one tick
    def tick(self):
        self.tick += 1
        for component in self.components:
            component(self.tick)
