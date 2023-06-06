class Player:
    """
    Represents a player in the game.

    Args:
        name (str): The name of the player.

    Attributes:
        name (str): The name of the player.
        online_in_game (bool): Indicates if the player is currently online in a game.
        current_game: The game in which the player is currently playing.
        online_on_server (bool): Indicates if the player is currently online on the server.

    Methods:
        set_online_on_server(): Sets the player's online status to True on the server.
        set_offline_on_server(): Sets the player's online status to False on the server.
        set_online_in_game(game=None): Sets the player's online status to True in the specified game.
        set_offline_in_game(game=None): Sets the player's online status to False in the specified game.
    """
    def __init__(self, name: str):
        self.name = name
        self.online_in_game = False
        self.current_game = None
        self.online_on_server = False

    def set_online_on_server(self):
        """
        Sets the player's online status to True on the server.
        """
        self.online_on_server = True
        print(f'Player {self.name} is online on Server')

    def set_offline_on_server(self):
        """
        Sets the player's online status to False on the server.
        """
        self.online_on_server = False
        print(f'Player {self.name} is offline from Server')

    def set_online_in_game(self, game=None):
        """
        Sets the player's online status to True in the specified game.

        Args:
            game: The game in which the player is currently playing.
        """
        self.online_in_game = True
        self.current_game = game
        print(f'Player {self.name} is currently playing {game}')

    def set_offline_in_game(self, game=None):
        """
        Sets the player's online status to False in the specified game.

        Args:
            game: The game from which the player is leaving.
        """
        self.online_in_game = False
        print(f'Player {self.name} left {game}')
        self.current_game = None

    def __str__(self):
        return self.name
