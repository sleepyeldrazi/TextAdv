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


def look_for_path(current_map, loc):
    if current_map[loc["y"] + 1][loc["x"]] != 0:
        print("You can go south")
    if current_map[loc["y"] - 1][loc["x"]] != 0:
        print("You can go north")
    if current_map[loc["y"]][loc["x"] + 1] != 0:
        print("You can go east")
    if current_map[loc["y"]][loc["x"] - 1] != 0:
        print("You can go west")


def map_info(current_map, pl):
    if current_map[pl.location["y"]][pl.location["x"]] == 1:
        print("Forest")
    elif current_map[pl.location["y"]][pl.location["x"]] == 0:
        print("You can't go there")
        pl.location = pl.oldLoc
    elif current_map[pl.location["y"]][pl.location["x"]] == 10:
        print("Crossroad")
    elif current_map[pl.location["y"]][pl.location["x"]] == 11:
        print("Farm")
    elif current_map[pl.location["y"]][pl.location["x"]] == 13:
        print("Dead end")
    elif current_map[pl.location["y"]][pl.location["x"]] == 2:
        print("Cave entrance")


def action(command, pl):
    available_actions = "take, move, hit, look around, look at, go"
    entered_command = command.split()
    if entered_command[0] in available_actions:
        if "go" in command:
            pl.oldLoc = pl.location
            if entered_command[1][0] == "n":
                pl.location["y"] = pl.location["y"] - 1
            elif entered_command[1][0] == "s":
                pl.location["y"] = pl.location["y"] + 1
            elif entered_command[1][0] == "e":
                pl.location["x"] = pl.location["x"] + 1
            elif entered_command[1][0] == "w":
                pl.location["x"] = pl.location["x"] - 1
            else:
                print("I don't understand")


playerOne = Player

while True:
    # print(playerOne.location)
    map_info(gameMap, playerOne)
    look_for_path(gameMap, playerOne.location)
    action(input("> "), playerOne)
