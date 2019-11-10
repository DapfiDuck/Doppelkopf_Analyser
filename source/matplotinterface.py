from matplotlib import pyplot as plt
from game_stats import generate_game_stats as generate

help_msg = """
help        - show help message
exit        - close program
plot game   - plot game statistics as pie chart
plot player - plot player data.
              Parameters: Player Name
generate    - Generate and display a subset of the data.
              Parameters: First Sheet, Last Sheet
list        - Lists players.
"""

def percent(float, decimals = 1):
    return round(float * (10 ** (decimals+2)))/(10**decimals)

def load_data(game, player, all_sheets, player_list):

    global gamedata, playerdata, sheets, players

    gamedata = game
    playerdata = player
    sheets = all_sheets
    players = player_list

def plot_command():
    while True:
        command = input("DKA > ").split(" ")

        if command[0] == "exit":
            exit()
        elif command[0] == "help":
            print(help_msg)
        elif command[0] == "list":
            print(players)
        elif command[0] == "plot":
            cmd_plot(command)
        elif command[0] == "generate" or command[0] == "gen":
            if(len(command)<3):
                print("Insufficient Parameters\nUsage: generate start end")
            else:
                genstart = int(command[1])
                genend = int(command[2])
                generate_subset(genstart, genend)
    return

def cmd_plot(command):

    if(len(command) == 1):
        return

    if(command[1] == "game"):
        plot_game(gamedata[0])
    elif command[1] == "player":

        if(len(command) < 3):
            print("Insufficient Parameters\nUsage: plot player [player short name]")
            return

        if(not command[2] in players):
            print("Player not found. Check Players with \"list\"")
            return
        else:
            print("Player found")

        data = playerdata[command[2]]
        plot_player(data, command[2])

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
