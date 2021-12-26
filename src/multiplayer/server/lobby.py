from ...game_files.projectile import mayProjectile
from ...game_files.gameHandler import GameHandler
from ...game_files.collectables import *
from ...game_files.gameConsts import *
from ...game_files.floor import mayFloor
from ...game_files.player import player
from ...game_files.npc import mayNPC

import json

class gameLobby(GameHandler):
    def __init__(self, lobby_name:str, lobby_level:str):
        GameHandler.__init__(self)
        self.current_scene = SCENE_PLAYING
        self.lobby_name    = lobby_name
        self.lobby_level   = lobby_level
        self.map_data      = self._loadMap(self.levels, self.lobby_level)
        self.last_mapName  = self.lobby_level
        
        self.ent_count     = 0     
        self.obj_count     = 0 
        
        ## 'player_name' : (x,y,w,h,speed,direction,health)
        self.players:list[tuple[str,tuple[int]]] = []
        ## 'npc_name' : (x,y,w,h,speed,direction,health,damage,type)
        self.npcs:list[tuple[str,tuple[int]]]    = []
        
        with open(f"./levels/{lobby_name}.json", 'rb') as f:
            self.levels = json.load(f)
    
    def _loadMap(self, maps:dict, map_name:str) -> bytes:
        if map_name in maps:
            with open(map_name, 'rb') as f:
                byte_list = f.read()
                for (i, byte) in enumerate(byte_list):
                    if byte is not 0:
                        self.obj_count += 1
                    
                    if byte in [240, 201, 85, 154, 148]:
                        self.ent_count += 1
                
            return byte_list
        else:
            print("[ERROR] Map not found, map name: {} does not exist".format(map_name))
    
    def _packet(self) -> str:
        if self.last_mapName != self.lobby_level:
            packet = {
                'lobby_name' : self.lobby_name,
                'lobby_level': self.lobby_level,
                'new_level'  : True,
                'players'    : self.players,
                'npcs'       : self.npcs,
                'obj_count'  : self.obj_count,
                'ent_count'  : self.ent_count,
                'map'        : self.map_data
            }
            
        else:
            packet = {
                'lobby_name' : self.lobby_name,
                'lobby_level': self.lobby_level,
                'new_level'  : False,
                'players'    : self.players,
                'ent_count'  : self.ent_count,
                'obj_count'  : self.obj_count,
                'npcs'       : self.npcs,
            }
        
        return json.dumps(packet)