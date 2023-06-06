class GamesInServer(object):
    """
    Represents a game in the server.

    Attributes:
        name (str): The name of the game.
        players (list): A list of Player objects representing the players in the game.

    Methods:
        add_player(player): Adds a player to the game.
        remove_player(player): Removes a player from the game.
        list_players(): Lists the players in the game.
        list_players_status(): Lists the players and their status in the game.
        set_player_status(player, online): Sets the online status of a player in the game.
    """
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        """
        Adds a player to the game.

        Args:
            player: The player object to be added.
        """
        self.players.append(player)
        print(f"Player '{player.get_name()}' added to game '{self.name}'.")

    def remove_player(self, player):
        """
        Removes a player from the game.

        Args:
            player: The player object to be removed.
        """
        if player in self.players:
            self.players.remove(player)
            print(f"Player '{player.get_name()}' removed from game '{self.name}'.")
        else:
            print(f"Player '{player.get_name()}' not found in game '{self.name}'.")

    def list_players(self):
        """
        Lists the players in the game.
        """
        player_names = []
        for player in self.players:
            player_name = player.name
            current_game = player.current_game
            if current_game == self.name:
                player_names.append(f"{player_name} (Online)")
            else:
                player_names.append(player_name)
        print(f"Players in game '{self.name}': {', '.join(player_names)}")

    # def list_players_status(self):
    #     """
    #     Lists the players and their status in the game.
    #     """
    #     print(f"Players and their status in game '{self.name}':")
    #     for player in self.players:
    #         status = "Online" if player.is_online() else "Offline"
    #         print(f"{player.get_name()}: {status}")

    def set_player_status(self, player, online):
        """
        Sets the online status of a player in the game.

        Args:
            player: The player object for which the status should be set.
            online (bool): The online status (True or False).
        """
        pov_player = [p for p in self.players if p.name == player]
        if online:
            pov_player[0].set_online_in_game(self.name)
            print(f'Player {pov_player[0].name} is online on {self.name}')
        else:
            pov_player[0].set_offline_in_game(self.name)

    def __str__(self):
        return self.name