# Pyro4 Game Server
This project demonstrates the usage of Pyro4 for building a simple game server with client-server interaction. Pyro4 is a powerful and flexible distributed object framework for Python, allowing objects to be accessed remotely and transparently. In this game server implementation, Pyro4 is used to facilitate communication between the client and the server.

## Introduction to Pyro4
Pyro4 is a distributed object technology library for Python that enables easy communication between processes. It allows Python objects to be accessed remotely, just as if they were local objects. Pyro4 provides a transparent and powerful way to build distributed systems, enabling seamless interaction between clients and servers.

## Project Structure
The project consists of the following files:

- `GameClient.py`: Defines the `GameClient` class, which represents the client interacting with the game server.
- `GameServer.py`: Defines the `GameServer` class, which represents the game server handling player and game management.
- `Player.py`: Defines the `Player` class, which represents a player in the game.
- `GamesInServer.py`: Defines the `GamesInServer` class, which represents the games hosted on the game server.
- `client_server_interaction.py`: Contains example code snippets that demonstrate the usage of the client-server interaction.

## Getting Started
To run the game server and interact with it using the provided client code, follow these steps:

1) Install Pyro4 by running:
``` python
pip install Pyro4
```
2) Start the game server by running python3 GameServer.py. This will start the server and display its URI.
3) Update the server_uri variable in client_server_interaction.py with the URI of the game server obtained in the previous step.
4) Run python3 client_server_interaction.py to execute the example code snippets and interact with the game server.

## Example Code Snippets
The `client_server_interaction.py` file contains example code snippets that demonstrate various interactions with the game server. These snippets include creating players, creating games, adding players to games, setting player status, and listing players in games. You can modify and expand upon these snippets to suit your specific requirements.

## Conclusion
The Pyro4 Game Server project provides a basic implementation of a game server using Pyro4 for client-server communication. It showcases the power and flexibility of Pyro4 for building distributed systems in Python. Feel free to explore the code, experiment with different interactions, and extend the functionality to suit your needs.

Please refer to the Pyro4 documentation for more detailed information on Pyro4 and its capabilities.