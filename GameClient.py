import Pyro4
from Player import Player


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class GameClient(object):
    """
    Represents a client for interacting with the game server.

    Args:
        server_uri (str): The URI of the game server.

    Attributes:
        server: The proxy object for the game server.

    Methods:
        create_player(player_name): Creates a new player on the game server.
        delete_player(player): Deletes a player from the game server.
        create_game(game_name): Creates a new game on the game server.
        add_player_to_game(player, game): Adds a player to a game on the game server.
        remove_player_from_game(player, game): Removes a player from a game on the game server.
        list_players_in_game(game): Lists the players in a game on the game server.
        list_players_status_in_game(game): Lists the players and their status in a game on the game server.
        set_player_status_on_server(player, online): Sets the online status of a player on the game server.
        set_player_status_in_game(player, game, online): Sets the online status of a player in a game on the game server.
    """
    def __init__(self, server_uri):
        self.server = Pyro4.Proxy(server_uri)

    def create_player(self, player_name):
        """
        Creates a new player on the game server.

        Args:
            player_name (str): The name of the player.

        Returns:
            str: The name of the created player.
        """
        player = self.server.create_player(player_name)
        return player

    def delete_player(self, player):
        """
        Deletes a player from the game server.

        Args:
            player: The player object to be deleted.
        """
        self.server.delete_player(player)

    def create_game(self, game_name):
        """
        Creates a new game on the game server.

        Args:
            game_name (str): The name of the game.

        Returns:
            str: The name of the created game.
        """
        game = self.server.create_game(game_name)
        return game

    def add_player_to_game(self, player, game):
        """
        Adds a player to a game on the game server.

        Args:
            player: The player object to be added.
            game: The game object to which the player should be added.
        """
        self.server.add_player_to_game(player, game)

    def remove_player_from_game(self, player, game):
        """
        Removes a player from a game on the game server.

        Args:
            player: The player object to be removed.
            game: The game object from which the player should be removed.
        """
        self.server.remove_player_from_game(player, game)

    def list_players_in_game(self, game):
        """
        Lists the players in a game on the game server.

        Args:
            game: The game object for which the player list should be retrieved.
        """
        self.server.list_players_in_game(game)

    def list_players_status_in_game(self, game):
        """
        Lists the players and their status in a game on the game server.

        Args:
            game: The game object for which the player status should be retrieved.
        """
        self.server.list_players_status_in_game(game)

    def set_player_status_on_server(self, player, online: bool):
        """
        Sets the online status of a player on the game server.

        Args:
            player: The player object for which the status should be set.
            online (bool): The online status (True or False).
        """
        self.server.set_player_status_on_server(player, online)
    
    def set_player_status_in_game(self, player, game, online: bool):
        """
        Sets the online status of a player in a game on the game server.

        Args:
            player: The player object for which the status should be set.
            game: The game object for which the player status should be set.
            online (bool): The online status (True or False).
        """
        self.server.set_player_status_in_game(player, game, online)
