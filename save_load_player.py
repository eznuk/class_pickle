from RC import Table
import pickle

tbl = Table(5, stat_msg=False,
            min_prec=0.9, max_prec=0.9,
            min_speed=0.9, max_speed=0.9)
tbl.players[0].precision = 0.3
tbl.players[0].speed = 0.8
tbl.run_game(1000)
tbl.plot_drink_hist()

# Beispiel für das Speichern und Laden mit pickle:
with open("tbl.pickle", "wb") as file:
    pickle.dump(tbl, file)
with open("tbl.pickle", "rb") as file:
    loaded_tbl = pickle.load(file)

player_0 = tbl.players[0]    
# Nun: speichert nur den player_0 mit pickle
# (siehe oben für die Syntax)
# [...]  

# Hier erstellen wir einen neuen Tisch: 
new_tbl = Table(5, stat_msg=False,
            min_prec=0.9, max_prec=0.9,
            min_speed=0.9, max_speed=0.9)

# nun wollen wir den Spieler von eben laden und nennen in "loaded_pl" ...
# (siehe oben für die Syntax)
# [...]

# ... und setzen ihn an den neuen Tisch:
new_tbl.players[0] = loaded_pl

new_tbl.run_game(1000)
new_tbl.plot_drink_hist()
