import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Player:
    def __init__(self, name: str):
        self.name = name
        self.online = False
        self.current_game = None

    def get_name(self):
        return self.name

    def is_online(self):
        return self.online

    def set_online(self, game=None):
        self.online = True
        self.current_game = game

    def set_offline(self):
        self.online = False
        self.current_game = None

    def get_current_game(self):
        if self.current_game:
            return self.current_game.get_name()
        return None

    def __str__(self):
        return self.name