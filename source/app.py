from csv_reader import get_sheet as get
from user_stats import gen_user_stats

sheet_nr = int(input("Sheets: "))
sheets = []
games = 0
wins = [0, 0, 0] #Reh, Contra, Tie

def percent(float, decimals = 1):
    return round(float * (10 ** (decimals+2)))/(10**decimals)

for number in range(1, sheet_nr+1):
    sheets.append(get(f"./data/Game{number}.csv"))

# print(sheets)

for sheet in sheets:
    for row_int in range(1, len(sheet)):

        row = sheet[row_int]
        # print(row)

        if len(row) == 5:

            games += 1

            if int(row[4]) >= 1:
                wins[0] += 1
            elif int(row[4]) <= -1:
                wins[1] += 1
            else:
                wins[2] += 1

        # print(str(row)+"\n")
    # print("\n")

re = round(wins[0]/games*1000)/10
contra = round(wins[1]/games*1000)/10
ties = round(wins[2]/games*1000)/10

#print("\nStatistics: ")
print(f"Re: {re}%, Contra: {contra}%, Ties: {ties}%")
print("\n")

player_stats = gen_user_stats(sheets)

player_list = ["D", "A", "M", "P"]

for user in player_list:
    player_stat = player_stats[user]

    #Statistics for Re
    rgames = player_stat["r"]["played"]
    rwins = player_stat["r"]["won"]
    rrate = percent(rwins/rgames)
    rscore = round(100*player_stat["r"]["score"]/rgames)/100

    #Statistics for Contra
    cgames = player_stat["c"]["played"]
    cwins = player_stat["c"]["won"]
    crate = percent(cwins/cgames)
    cscore = round(100*player_stat["c"]["score"]/cgames)/100

    #Statistics for Overall
    total_games = player_stats["total"] # Total counted, valid games
    total_wins = rwins + cwins
    total_rate = percent(total_wins / total_games)

    print(f"""Statistics for {user}:
    Re:\t\t{rrate}% ({rwins} of {rgames})
    Contra:\t{crate}% ({cwins} of {cgames})
    Total:\t{total_rate}% ({total_wins} of {total_games})

    Average Scores:
    Re:\t\t{rscore}
    Contra:\t{cscore}
    """)
    #Full stats: {player_stat}
#print(f"Total Games: {player_stats['Total']}")
