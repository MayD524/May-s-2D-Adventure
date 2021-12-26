from lobby import gameLobby
from _thread import *
import traceback
import socket
import psutil
import json
import sys
import os

class gameServer:
    def __init__(self, hostName:str, port:int, name:str, max_lobbies:int) -> None:
        self.hostName    = hostName
        self.port        = port
        self.name        = name
        self.max_lobbies = max_lobbies
        
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.lobbies     = {}
        """
            player_name : {
                'lobby_name' : lobby_name,
                'address'    : (ip, port),
                'connection' : connection
            }
        """
        self.players     = {}
        
        
        try:
            self.serverSock.bind((self.hostName, self.port))
        except socket.error as e:
            print(f"[ERROR] Could not bind to {self.hostName}:{self.port}")
            traceback.print_exc()
            print(e)
            sys.exit(1)
    def threadedClient(self, connection, address) -> None:
        pass        