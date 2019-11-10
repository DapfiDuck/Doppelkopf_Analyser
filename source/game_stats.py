def generate_game_stats(sheets):
    games = 0
    wins = [0, 0, 0] #Re, Contra, Tie

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

    return (wins, games)
