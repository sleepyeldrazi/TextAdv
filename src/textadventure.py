from src.gameFunc import *

gameMap = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 10, 13, 0],
    [0, 0, 0, 11, 0, 0],
    [0, 2, 1, 10, 1, 0],
    [0, 0, 0, 0, 0, 0]
]


class Player:
    location = {"x": 1, "y": 1}
    oldLoc = {"x": 1, "y": 1}


playerOne = Player

while True:

    map_info(gameMap, playerOne)
    look_for_path(gameMap, playerOne.location)
    action(input("> "), playerOne)
