import csv


def read_players():
    with open('players.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        players = []
        for row in csv_reader:
            try:
                d = {
                    'name': row[0],
                    'team': row[1],
                    'position': row[2],
                    'height': row[3],
                    'weight': row[4],
                    'age': float(row[5])
                }
                players.append(d)
            except Exception:
                print(row)
    return players


def find_oldest_player(players):
    max_age = 0
    oldest_name = None
    for p in players:
        if p['age'] > max_age:
            max_age = p['age']
            oldest_name = p['name']
    return oldest_name, max_age


def find_most_outfielders_team(players):
    outfielders_map = {}
    for p in players:
        if p['position'] == 'Outfielder':
            p_team = p['team']
            if p_team in outfielders_map:
                outfielders_map[p_team] += 1
            else:
                outfielders_map[p_team] = 1
    most_outfielders = 0
    most_team = None
    for t, n in outfielders_map.items():
        if n > most_outfielders:
            most_outfielders = n
            most_team = t
    return most_team, most_outfielders


def find_players_position(players, name):
    return next((p['position'] for p in players if p['name'] == name), None)


if __name__ == '__main__':
    players = read_players()
    oldest_name, oldest_age = find_oldest_player(players)
    find_most_outfielders_team(players)
    most_team, number_of_outfielders = find_most_outfielders_team(players)
    kenny_position = find_players_position(players, 'Kenny Lofton')
    pass