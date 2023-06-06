import Pyro4
from GamesInServer import GamesInServer
from Player import Player


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class GameServer(object):
    """
    Represents a game server.

    Attributes:
        players (list): A list of Player objects representing the players on the server.
        games (list): A list of GamesInServer objects representing the games on the server.

    Methods:
        create_player(player_name): Creates a new player on the server.
        delete_player(player): Deletes a player from the server.
        create_game(game_name): Creates a new game on the server.
        add_player_to_game(player, game): Adds a player to a game on the server.
        remove_player_from_game(player, game): Removes a player from a game on the server.
        list_players_in_game(game): Lists the players in a game on the server.
        list_players_status_in_game(game): Lists the players and their status in a game on the server.
        set_player_status_on_server(player, online): Sets the online status of a player on the server.
        set_player_status_in_game(player, game, online): Sets the online status of a player in a game on the server.
    """
    def __init__(self):
        self.players = []
        self.games = []

    def create_player(self, player_name):
        """
        Creates a new player on the server.

        Args:
            player_name (str): The name of the player.

        Returns:
            str: The name of the created player.
        """
        player = Player(player_name)
        self.players.append(player)
        print(f"Player '{player_name}' created.")
        return player.name

    def delete_player(self, player):
        """
        Deletes a player from the server.

        Args:
            player: The player object to be deleted.
        """
        if player in self.players:
            self.players.remove(player)
            print(f"Player '{player.get_name()}' deleted.")
        else:
            print(f"Player '{player.get_name()}' not found.")

    def create_game(self, game_name):
        """
        Creates a new game on the server.

        Args:
            game_name (str): The name of the game.

        Returns:
            str: The name of the created game.
        """
        game = GamesInServer(game_name)
        self.games.append(game)
        print(f"Game '{game_name}' created.")
        return game.name
    
    def add_player_to_game(self, player, game):
        """
        Adds a player to a game on the server.

        Args:
            player: The player object to be added.
            game: The game object to which the player should be added.
        """
        pov_player = [p for p in self.players if p.name == player]
        pov_game = [g for g in self.games if g.name == game]
        pov_game[0].add_player(pov_player[0])
    
    def list_players_in_game(self, game):
        """
        Lists the players in a game on the server.

        Args:
            game: The game object for which the player list should be retrieved.
        """
        pov_game = [g for g in self.games if g.name == game]
        pov_game[0].list_players()

    def list_players_status_in_game(self, game):
        """
        Lists the players and their status in a game on the server.

        Args:
            game: The game object for which the player status should be retrieved.
        """
        pov_game = [g for g in self.games if g.name == game]
        pov_game[0].list_players_status()

    def remove_player_from_game(self, player, game):
        """
        Removes a player from a game on the server.

        Args:
            player: The player object to be removed.
            game: The game object from which the player should be removed.
        """
        pov_player = [p for p in self.players if p.name == player]
        pov_game = [g for g in self.games if g.name == game]
        pov_game[0].remove_player(pov_player[0])

    def set_player_status_on_server(self, player, online):
        """
        Sets the online status of a player on the server.

        Args:
            player: The player object for which the status should be set.
            online (bool): The online status (True or False).
        """
        pov_player = [p for p in self.players if p.name == player]
        if online:
            pov_player[0].set_online_on_server()
        else:
            pov_player[0].set_offline_on_server()

    def set_player_status_in_game(self, player, game, online):
        """
        Sets the online status of a player in a game on the server.

        Args:
            player: The player object for which the status should be set.
            game: The game object for which the player status should be set.
            online (bool): The online status (True or False).
        """
        pov_game = [g for g in self.games if g.name == game]
        pov_game[0].set_player_status_on_game(player, online)


server = GameServer()
daemon = Pyro4.Daemon()
uri = daemon.register(server)

# Start the server
print("Server URI:", uri)
daemon.requestLoop()