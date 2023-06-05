import Pyro4
from GamesInServer import GamesInServer
from Player import Player


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class GameServer(object):
    def __init__(self):
        self.players = []
        self.games = []

    def create_player(self, player_name):
        player = Player(player_name)
        # player = {"1": player_name}
        self.players.append(player)
        print(f"Player '{player_name}' created.")
        return player.name

    def delete_player(self, player):
        if player in self.players:
            self.players.remove(player)
            print(f"Player '{player.get_name()}' deleted.")
        else:
            print(f"Player '{player.get_name()}' not found.")

    def create_game(self, game_name):
        game = GamesInServer(game_name)
        self.games.append(game)
        print(f"Game '{game_name}' created.")
        return game.name
    
    def add_player_to_game(self, player, game):
        pov_player = [p for p in self.players if p.name == player]
        pov_game = [g for g in self.games if g.name == game]
        pov_game[0].add_player(pov_player[0])
    
    def list_players_in_game(self, game):
        pov_game = [g for g in self.games if g.name == game]
        pov_game[0].list_players

    def list_players_status_in_game(self, game):
        pov_game = [g for g in self.games if g.name == game]
        player_status = pov_game[0].list_players_status()
        print(f"Players in game '{pov_game[0].get_name()}': {', '.join(player_status)}")

    def remove_player_from_game(self, player, game):
        pov_player = [p for p in self.players if p.name == player]
        pov_game = [g for g in self.games if g.name == game]
        pov_game[0].remove_player(pov_player[0])


server = GameServer()
# server.create_player("Angie")
# Server setup
daemon = Pyro4.Daemon()
uri = daemon.register(server)

# Start the server
print("Server URI:", uri)
daemon.requestLoop()
