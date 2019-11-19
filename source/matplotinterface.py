from matplotlib import pyplot as plt
from game_stats import generate_game_stats as generate

help_msg = """
help        - Show help message
exit        - Close program
plot game   - Plot game statistics as pie chart
plot player - Plot player data.
              Parameters: [Player]
plot dev    - Plot development of a players win percentage over the sheets
              Parameters: [Player] or \"-all\"
generate    - Generate and display a subset of the data.
              Parameters: [First Sheet] [Last Sheet]
list        - Lists players.
"""

alias = {}

def percent(float, decimals = 1):
    return round(float * (10 ** (decimals+2)))/(10**decimals)

def load_data(game, player_data, all_sheets, player_list):

    global gamedata, playerdata, sheets, players

    gamedata = game
    playerdata = player_data
    sheets = all_sheets
    players = player_list

def plot_command():

    print("Starting console. Type \"help\" for help")

    while True:
        command = input("DKA > ").split(" ")

        if command[0] == "exit":
            exit()
        elif command[0] == "help":
            print(help_msg)
        elif command[0] == "list":
            print("--Players--")
            for player in players:
                print(player, end=", ")

            print("\n\n--Aliases--")
            for name in alias:
                print(name+": "+alias[name])

        elif command[0] == "alias":
            add_alias(command)
        elif command[0] == "plot":
            cmd_plot(command)
        elif command[0] == "generate" or command[0] == "gen":
            if(len(command)<3):
                print("Insufficient Parameters\nUsage: generate [start] [end]")
            else:
                genstart = int(command[1])
                genend = int(command[2])
                generate_subset(genstart, genend)
    return


def add_alias(command):
    if(not len(command) >= 3):
        print("Insufficient Parameters\nUsage: alias [player] [alias]")
    elif(not command[1] in players):
        print("Player not found. Check Players with \"list\"")
    else:
        alias[command[2]] = command[1]
        print(f"Added Alias {alias[command[2]]}: {command[2]}")

def cmd_plot(command):

    if(len(command) == 1):
        return

    if command[1] == "game":
        plot_game(gamedata[0])
    elif command[1] == "player":

        player = ""

        if(len(command) < 3):
            print("Insufficient Parameters\nUsage: plot player [player]")
            return

        if(not command[2] in players):

            if(command[2] in alias):
                print("Alias Found")
                player = alias[command[2]]
            else:
                print("Player not found. Check Players with \"list\"")
                return

        else:
            print("Player found")
            player = command[2]


        data = playerdata[player]
        plot_player(data, player)


    elif command[1] == "dev" or "development":

        if(len(command) < 3):
            print("Insufficient Parameters\nUsage: plot development [player]")
            return

        if(command[2] == "-all"):
            print("Plotting All")
            plot_all_developments()
        elif(not command[2] in players):
            print("Player not found. Check Players with \"list\"")
            return
        else:
            print("Player found")
            plot_development(command[2])


def plot_development(player):

    x = []
    y = []

    raw_data = playerdata[player]["sheet_stats"]

    count_x = 1
    for data_point in raw_data:
        x.append(count_x)
        y.append(data_point[0]/data_point[1])

        count_x += 1

    plt.plot(x, y)
    plt.xlabel("Sheet")
    plt.ylabel("Win Percentage")

    plt.title(f"Win Percentage Development For {player}")
    plt.show()

def plot_all_developments():

    x = []

    length = len(playerdata[players[0]]["sheet_stats"])
    x = range(length)

    for player in players:
        y = []
        raw_data = playerdata[player]["sheet_stats"]

        count_x = 1
        for data_point in raw_data:
            y.append(data_point[0]/data_point[1])

            count_x += 1

        plt.plot(x, y, label=player)


    plt.xlabel("Sheet")
    plt.ylabel("Win Percentage")

    plt.title("Development of all players")
    plt.legend()
    plt.show()


    pass

def plot_player(stats, player):

    re = stats["r"]
    contra = stats["c"]

    x = ["Re", "Contra", "Total"]
    y = [re["won"]/re["played"], contra["won"]/contra["played"],
        (re["won"]+contra["won"])/(re["played"]+contra["played"])]
    plt.bar(x, y, color="#777777")

    plt.grid(True, axis="y")
    plt.ylabel("Winrate")
    plt.title(f"Statistics of player {player}")

    plt.show()

    return


def plot_game(stats):

    labels = [f"Re ({stats[0]} Wins)", f"Contra ({stats[1]} Wins)", f"Tie ({stats[2]} Ties)"]
    plt.pie(stats, labels = labels)

    plt.title("Win Statistics For Parties")
    plt.show()

    return

def generate_subset(start, end):
    sheet_statistics = generate(sheets[start:end])

    wins = sheet_statistics[0]
    games = sheet_statistics[1]

    re = percent(wins[0]/games)
    contra = percent(wins[1]/games)
    ties = percent(wins[2]/games)

    print(f"Re: {re}%, Contra: {contra}%, Ties: {ties}%")

    plot_game(sheet_statistics[0])
