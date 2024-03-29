
## sprite sheet 0 is for living entities
## sprite sheet 1 is for game objects

IS_LIVING_ENTITY = 0
IS_GAME_OBJECT   = 1

## for getting textures
## All tiles are 8x8 pixels
TILEOFFSET = 8

## Player Stuff
PLAYER_DEFAULT_HEALTH     = 100
PLAYER_DEFAULT_MAX_HEALTH = 150

## for facing directions
DIRECTION_FRONT = 0
DIRECTION_LEFT  = 1
DIRECTION_RIGHT = 2

MAKE_BLOB_SMALL = 10

DEFAULT_SPEED       = 1
DEFAULT_FALL_RATE   = -1.2
DEFAULT_JUMP_HEIGHT = 20

## for game id
GAME_ENTITY = 0
GAME_OBJECT = 1

## for scene types
SCENE_TITLE   = 0
SCENE_PLAYING = 1
SCENE_END     = 2
SCENE_WIN     = 3

## Game Scoring
GAME_SCORE_PER_COIN = 10
GAME_SCORE_PER_BLOB = 100

## coin location
COIN_SPRITE_IMG = 1
COIN_X_OFFSET   = 0
COIN_Y_OFFSET   = 16

## health kit img location
HEALTH_KIT_X_OFFSET = 8
HEALTH_KIT_Y_OFFSET = 16

## Level End img location
LEVEL_END_X_OFFSET = 32
LEVEL_END_Y_OFFSET = 0

## anything higher than 120 breaks things
## recommended is to be 30 or 60
DEFAULT_FPS = 60

NPC_SIMPLE_ENEMY = 0
NPC_RANGED_ENEMY = 1

NPC_TYPE_ENEMY = [NPC_SIMPLE_ENEMY, NPC_RANGED_ENEMY]

JUMP_CHANCE = 0.5
WAIT_CHANCE = 0.99

NPC_WAITING_ENABLED = True