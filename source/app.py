from csv_reader import get_sheet as get
from user_stats import gen_user_stats
from user_stats import get_win_percentage_for_game as win_percentage
from matplotinterface import plot_command as run_interface
from matplotinterface import load_data as stage_interface
import game_stats


player_list = ["D", "A", "M", "P"]

sheet_nr = int(input("Sheets: "))
sheets = []

def main():

    # Load sheets
    for number in range(1, sheet_nr+1):
        sheets.append(get(f"./data/Game{number}.csv"))


    # Get Game Stats
    print("\n|"+"-"*40+"|\n")
    game_statistics = game_stats.generate_game_stats(sheets)
    print_game_stats(game_statistics)

    # Generate Player Stats
    player_statistics = gen_user_stats(sheets)
    print_player_stats(player_statistics)

    # Open Console
    print("\n|"+"-"*40+"|\n")
    stage_interface(game_statistics, player_statistics, sheets, player_list)
    run_interface()

    return


def percent(float, decimals = 1):
    return round(float * (10 ** (decimals+2)))/(10**decimals)


def print_game_stats(game_statistics):

    wins = game_statistics[0]
    games = game_statistics[1]

    re = percent(wins[0]/games)
    contra = percent(wins[1]/games)
    ties = percent(wins[2]/games)

    #print("\nStatistics: ")
    print(f"Re: {re}%, Contra: {contra}%, Ties: {ties}%")
    print("\n")
    return


def print_player_stats(player_statistics):

    for user in player_list:
        player = player_statistics[user]

        #Statistics for Re
        rgames = player["r"]["played"]
        rwins = player["r"]["won"]
        rrate = percent(rwins/rgames)
        rscore = round(100*player["r"]["score"]/rgames)/100

        #Statistics for Contra
        cgames = player["c"]["played"]
        cwins = player["c"]["won"]
        crate = percent(cwins/cgames)
        cscore = round(100*player["c"]["score"]/cgames)/100

        #Statistics for Overall
        total_games = player_statistics["total"] # Total counted, valid games
        total_wins = rwins + cwins
        total_rate = percent(total_wins / total_games)

        print(f"""Win Percentage for {user} (Rounds):
        Re:\t{rrate}% ({rwins} of {rgames})
        Contra:\t{crate}% ({cwins} of {cgames})
        Total:\t{total_rate}% ({total_wins} of {total_games})

        Average Scores:
        Re:\t{rscore}
        Contra:\t{cscore}
        """)

    player_win_percentage = win_percentage(sheets)

    print("Win Percentage over all sheets:")
    for player in player_list:
        print(f"{player}: {percent(player_win_percentage[player])}")

    return

main()
