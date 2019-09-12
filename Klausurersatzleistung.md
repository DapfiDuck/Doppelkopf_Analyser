# Klausurersatzleistung Informatik
David J. Kowalk

# Das Spiel
Doppelkopf ist ein Kartenspiel in dem es darum geht las spiel von zwei Personen die größte Anzahl der 240 zu vergebenden Punkten in Form von Karten zu ergattern. Diese Punkte werden dann zu Abrechnungspunkten, abhängig von der Gewinnstufe (120, 90, 60, 30 Schwarz) und der Vorhersage der Spieler, umgerechnet und dem gewinnenden Team positiv, und dem verlierenden Team negativ aufgerechnet. Zudem wird der Wert des Spiels positiv notiert, wenn die Re-Partei gewinnt, und negativ, wenn die Contra Partei gewinnt.

**Beispiel:**

|S1|S2|S3|S4|Game
|--|--|--|--|--|
|2 | 2|-2|-2|+2|
|5 |-1| 1|-5|-3|
|6 | 0| 0|-6|-1|
|2 | 4|-4|-2|+4|


# Aufgabe
Es ist für jeden Spieler, wie auch für das Spiel insgesammt pro Partei die Gewinnchance zu ermitteln. Zudem soll die durchschnittliche Wertigkeit eines gewonnen Spiels für jeden Spieler errechnet werden.

# Durchführung

Die einzelnen Spiele werden im csv-Format gespeichert und vom Programm beim Start eingelesen.

## Auswertung des Gesamt-Spiels
Für jede Zeile wird gezählt, welche Partei gewonnen hat. Ist der Wert des Spiels positiv, hat die Re-Partei gewonnen, ist er negativ die Contra-Partei und andererseits liegtist es ein Unentschieden vor. Sonderspiele (Hochzeit, Trumpfarmut, Solor, etc.) werden hierbei nicht gezählt. Sind die Daten erhoben kann berechnet werden:

> f: Gewinnrate 
> w: Anzahl der gewonnenen Spiele
> p: Anzahl der gespielten Spiele

$$
f_{Partei} = \frac{w_{Partei}}{p_{Partei}}
$$

## Auswertung der Spieler-Statistiken
Zunächst wird die Datenstruktur definiert, in der die Spielerstatistiken notiert werden. Hierfür can in Python ein Dictionary verwendet werden:
```
{
	"S1":{
		"r":{"played":0, "won":0, "value":0},
		"c":{"played":0, "won":0, "value":0},
		"total_games":0,
		"total_value":0
	},
	[...]
	"S4":{
		"r":{"played":0, "won":0, "value":0},
		"c":{"played":0, "won":0, "value":0},
		"total_games":0,
		"total_value":0
	}
}
```

Es wird nun zunächst pro Runde bestimmt, welche Partei gewonnen hat und welche Partei der jeweilige Spieler angehört hat.

```
if gamescore > 0:
	winning_party = "re"
elif gamescore < 0:
	winning_party = "contra"

loosing_party = other_party[winning_party]

if playerscore > previous_playerscore:
	player_party = winning_party
else:
	player_party = loosing_party
``` 

Hat der Spieler die jeweilige Runde gewonnen, so wird auf seine Gewinnrunden und die Teilnahmen für die jeweilige Partei einen aufgezählt, sonst nur auf die Teilnahmen der verlierenden Partei.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMzM1NjU0NDcsLTE3ODEyNzc1NjUsNz
Y1MDEwMTk3LDE1MTY2NTMxMDddfQ==
-->