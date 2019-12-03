# Doppelkopf Analyser
Write an analysis for each player in the game of Doppelkopf accross multiple sheets.

[GitHub Pages](http://DapfiDuck.github.io/Doppelkopf_Analyser)

## Requirements
- Python 3.8
- matplotlib ```pip install matplotlib```

## License
This project is licensed under the MIT License - see the LICENSE file for details

## How to add your own files
 Sheets are to be placed into the ``data`` folder in a csv format.

 |Player 1|Player 2|Player 3|Player 4|Game|
 |--------|--------|--------|--------|----|
 |Values P1|Values P2|Values P3|Values P4|Values Game|
 |...|...|...|...|...|

 The filename must follow the following format:
 > Game[Nr].csv

Starting to count at 1. For example: Game1.csv
Also you must adjust the corresponding list of expected player names in the app.py:

```
9: player_list = ["D", "A", "M", "P"]
```

Currently the script is expecting the players D, A, M, and P at the top of each sheet. You can adjust that to your player-names. The dataset must be consistent in this.
The Player names do not have to be in order.

## Functions
- Calculating and plotting of game statistics (Win probability for each team)
- Calculation of player statistcs
  - Win Probability for each team
  - Average Score per party
  - Average win-probability at the end of sheet
- Generation of game statistics

[Documentation (German)](./documentation/Klausurersatzleistung.html)
