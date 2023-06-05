from GameClient import GameClient

server_uri = "PYRO:obj_2b0dab42a1ac4fcaad1387515c1697af@localhost:54506"
client = GameClient(server_uri)

angelica = client.create_player("Angelica")
print(angelica)
hanna = client.create_player("Hanna")
leonardo = client.create_player("Leonardo")

valorant = client.create_game("Valorant")
league_of_legends = client.create_game("League of Legends")

client.add_player_to_game(angelica, valorant)
client.add_player_to_game(hanna, valorant)
client.add_player_to_game(leonardo, league_of_legends)

client.list_players_in_game(valorant)
client.list_players_in_game(league_of_legends)

client.list_players_status_in_game(valorant)
client.list_players_status_in_game(league_of_legends)

client.remove_player_from_game(leonardo, league_of_legends)
client.list_players_status_in_game(league_of_legends)
