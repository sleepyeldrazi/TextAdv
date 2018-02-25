map = [
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


def look_for_path(mp, loc):
    if mp[loc["y"] + 1][loc["x"]] != 0:
        print("You can go south")
    if mp[loc["y"] - 1][loc["x"]] != 0:
        print("You can go north")
    if mp[loc["y"]][loc["x"] + 1] != 0:
        print("You can go east")
    if mp[loc["y"]][loc["x"] - 1] != 0:
        print("You can go west")


def map_info(mp, pl):
    if mp[pl.location["y"]][pl.location["x"]] == 1:
        print("Forest")
    elif mp[pl.location["y"]][pl.location["x"]] == 0:
        print("You can't go there")
        pl.location = pl.oldLoc
    elif mp[pl.location["y"]][pl.location["x"]] == 10:
        print("Crossroad")
    elif mp[pl.location["y"]][pl.location["x"]] == 11:
        print("Farm")
    elif mp[pl.location["y"]][pl.location["x"]] == 13:
        print("Dead end")
    elif mp[pl.location["y"]][pl.location["x"]] == 2:
        print("Cave entrance")

def action(command, pl):
    available_actions = "take, move, hit, look around, look at, go"
    compass = "north, east, south, west, n, e, s, w"
    entered_command = command.split()
    if entered_command[0] in available_actions:
        if "go" in command:
            pl.oldLoc = pl.location
            if "n" == entered_command[1][0]:
                pl.location["y"] = pl.location["y"] - 1
            elif "s" == entered_command[1][0]:
                pl.location["y"] = pl.location["y"] + 1
            elif "e" == entered_command[1][0]:
                pl.location["x"] = pl.location["x"] + 1
            elif "w" == entered_command[1][0]:
                pl.location["x"] = pl.location["x"] - 1
            else:
                print("I don't understand")


playerOne = Player

while True:
    #print(playerOne.location)
    map_info(map, playerOne)
    look_for_path(map, playerOne.location)
    action(input("> "), playerOne)
