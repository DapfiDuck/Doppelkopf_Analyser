from csv_reader import get_sheet as get

other_party = {
    "r":"c",
    "c":"r"
}

def gen_user_stats(sheets):

    games = {
        "D" : {
            "r": {"played":0, "won":0, "score":0},
            "c": {"played":0, "won":0, "score":0},
            "prev": 0
        },
        "A" : {
            "r": {"played":0, "won":0, "score":0},
            "c": {"played":0, "won":0, "score":0},
            "prev": 0
        },
        "M" : {
            "r": {"played":0, "won":0, "score":0},
            "c": {"played":0, "won":0, "score":0},
            "prev": 0
        },
        "P" : {
            "r": {"played":0, "won":0, "score":0},
            "c": {"played":0, "won":0, "score":0},
            "prev": 0
            },
        "total": 0
    }
    # For every player define for each party [played, won, score] and previous
    # And define Total Games

    # Keep Track of current position for data error alerts
    sheet_nr = 0

    for sheet in sheets:

        sheet_nr += 1
        reset_previous(games)

        player = sheet[0]

        for row_int in range(1, len(sheet)-1):

            # For every row in the sheet:
            # 1. Verify that the round does not imply any special case (Trumpfarmut, Solo, etc)
            # 2. Determine winning Party
            # 3. Count wins and participations for each player in loop
            # 4. Verify data integrity

            total_wins = 0  # Counts the winning players for every round to verify data integrity

            #Read row and round value from sheet
            row = sheet[row_int]
            game_score = int(row[4])

            if len(row) != 5 or int(row[4]) == 0: # Skip row if special game
                # print(f"=== Scipping game (Sheet {sheet_nr}, Row {row_int}) ===")
                update_previous(row, games, player)
                continue

            games["total"] += 1


            if game_score >= 1:
                winning_party = "r"
            elif game_score <= -1:
                winning_party = "c"
            else:
                continue

            loosing_party = other_party[winning_party]

            for cell in range(0, 4):

                # For player of any given round:
                # 1. Load score from this and the previous round
                # 2. Count a win in the winning party
                # 3. Count participation in both parties
                # 4. Check sum and winner count

                current_player = player[cell]
                previous_round = games[current_player]["prev"] # Score after previous round -> Example games["D"][p]
                score = int(row[cell])

                if score > previous_round:

                    # if score for player increased, add 1 to winning party's wins
                    games[current_player] [winning_party] ["won"] += 1
                    games[current_player] [winning_party] ["played"] += 1
                    games[current_player] [winning_party] ["score"] += abs(game_score) #Count up winning points
                    total_wins += 1
                elif score < previous_round:
                    games[current_player] [loosing_party] ["played"] += 1
                else:
                    print(f"=== ALERT (Unexpected static: Sheet {sheet_nr}, Row {row_int}, Player {current_player}) ALERT ===")
                    exit()

                #Update Previous Game to current for next iteration
                games[current_player]["prev"] = int(row[cell])


            if total_wins != 2 or not check_sum_right(row):
                print(f"===ALERT (Sheet {sheet_nr}, Row {row_int}) ALERT===")

            if games[current_player]["r"]["played"] + games[current_player]["c"]["played"] != games["total"]:
                print(f"=== ALERT (Game count does not align: Sheet {sheet_nr}, Row {row_int}, Score {row[4]}) ALERT ===")
                exit()

    return games


def reset_previous(games):
    players = ["D", "A", "M", "P"]

    for player in players:
        games[player]["prev"] = 0

def update_previous(row, games, player):
    for cell in range(0, 4):
        games[player[cell]]["prev"] = int(row[cell]) # update cells

def check_sum_right(row):
    return int(row[0])+int(row[1])+int(row[2])+int(row[3]) == 0
    #Summ of all players needs to be 0

def win_sum_right(rwin, cwin, twin): #Re-Win, Contra-Win and Total-win
    return int(rwin) + int(cwin) == int(twin)



#print(get_map(["A", "D", "M", "P", "S"]))
