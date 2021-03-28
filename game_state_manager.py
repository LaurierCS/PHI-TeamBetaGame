from state import State


    def update(self):
        self.current_state.update()
        self.clock.tick(self.target_fps)


