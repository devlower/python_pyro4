from GameClient import GameClient

server_uri = "PYRO:obj_4d78d1c8903c4b3f98f910b40b921fd4@localhost:50684"
client = GameClient(server_uri)

angelica = client.create_player("Angelica")
hanna = client.create_player("Hanna")
leonardo = client.create_player("Leonardo")
otto = client.create_player("Otto")

valorant = client.create_game("Valorant")
league_of_legends = client.create_game("League of Legends")

client.set_player_status_on_server(angelica, True)
client.set_player_status_on_server(hanna, True)
client.set_player_status_on_server(leonardo, True)
client.set_player_status_on_server(otto, True)

client.add_player_to_game(angelica, valorant)
client.add_player_to_game(hanna, valorant)
client.add_player_to_game(leonardo, league_of_legends)
client.add_player_to_game(otto, league_of_legends)

client.set_player_status_in_game(angelica, valorant, True)
client.set_player_status_in_game(hanna, valorant, True)
client.set_player_status_in_game(leonardo, league_of_legends, True)
client.set_player_status_in_game(otto, league_of_legends, True)

client.list_players_in_game(valorant)
client.list_players_in_game(league_of_legends)

client.remove_player_from_game(leonardo, league_of_legends)
client.list_players_in_game(league_of_legends)

client.set_player_status_in_game(hanna, valorant, False)

client.list_players_in_game(valorant)
client.list_players_in_game(league_of_legends)

client.set_player_status_on_server(angelica, False)
client.set_player_status_on_server(hanna, False)
client.set_player_status_on_server(leonardo, False)
client.set_player_status_on_server(otto, False)
