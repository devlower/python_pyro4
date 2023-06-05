import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class GamesInServer:
    def __init__(self, name):
        self.name = name
        self.players = []

    def get_name(self):
        return self.name

    def add_player(self, player):
        self.players.append(player)
        player.set_online(self)
        print(f"Player '{player.get_name()}' added to game '{self.name}'.")
        self.broadcast_player_status()

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            player.set_offline()
            print(f"Player '{player.get_name()}' removed from game '{self.name}'.")
            self.broadcast_player_status()
        else:
            print(f"Player '{player.get_name()}' is not in game '{self.name}'.")

    def list_players(self):
        player_names = []
        for player in self.players:
            player_name = player.get_name()
            current_game = player.get_current_game()
            if current_game == self.name:
                player_names.append(f"{player_name} (Online)")
            else:
                player_names.append(player_name)
        print(f"Players in game '{self.name}': {', '.join(player_names)}")

    def broadcast_player_status(self):
        for player in self.players:
            player_list = self.list_players()  # Get updated player list
            player.set_online(player_list)

    def list_players_status(self):
        player_names = []
        for player in self.players:
            player_name = player.get_name()
            current_game = player.get_current_game()
            if current_game == self.name:
                player_names.append(f"{player_name} (Online in {current_game})")
            else:
                player_names.append(player_name)
        return player_names
    
    def __str__(self):
        return self.name