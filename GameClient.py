import Pyro4
from Player import Player


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class GameClient(object):
    def __init__(self, server_uri):
        self.server = Pyro4.Proxy(server_uri)

    def create_player(self, player_name):
        player = self.server.create_player(player_name)
        return player

    def delete_player(self, player):
        self.server.delete_player(player)

    def create_game(self, game_name):
        game = self.server.create_game(game_name)
        return game

    def add_player_to_game(self, player, game):
        self.server.add_player_to_game(player, game)

    def remove_player_from_game(self, player, game):
        self.server.remove_player_from_game(player, game)

    def list_players_in_game(self, game):
        self.server.list_players_in_game(game)

    def list_players_status_in_game(self, game):
        self.server.list_players_status_in_game(game)
