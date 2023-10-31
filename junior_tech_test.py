import csv

def read_csv_file(file_path):
    """
    Read a CSV file and return its content as a list of dictionaries.
    """
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        list_of_dicts = list(reader)

    return list_of_dicts

def get_unique_teams(data):
    """
    Return a set of unique team names from the provided data.
    """
    unique_team_names = set()
    for player in data:
        unique_team_names.add(player['team_name'])
    return unique_team_names

def get_most_common_event_type(data):
    """
    Return the most common event type name from the provided data.
    """
    event_types = []
    for event_type in data:
        event_types.append(event_type['event_type_name'])
    unique_events = list(set(event_types))
    event_count = []
    for event in unique_events:
        event_count.append(event_types.count(event))
    most_common_idx = event_count.index(max(event_count))

    return unique_events[most_common_idx]

def filter_by_team(data, team_name):
    """
    Filter the data by the provided team name and return the filtered data.
    """
    filtered_data = []
    for player in data:
        if team_name == player['team_name']:
            filtered_data.append(player)
    return filtered_data

def count_event_type_by_team(data, team_name, event_type_name):
    """
    Count the number of events of a specific type for a given team.
    """
    filtered_team = filter_by_team(data, team_name)
    count = 0
    for player in filtered_team:
        if event_type_name in player['event_type_name']:
            count += 1
    return count

def average_pass_length_by_team(data, team_name):
    """
    Calculate the average pass length for the provided team to 1 decimal place
    """
    total_pass_length = 0
    count = 0
    filtered_team = filter_by_team(data, team_name)
    for player in filtered_team:
        if len(player['pass_length']) > 0:
            count += 1
            total_pass_length += float(player['pass_length'])
    average_pass_length = total_pass_length / count
    return round(average_pass_length,1)

def filter_players_by_position(data, position_name):
    """
    Return a list of player names who play at the provided position.
    """
    filtered_data = set()
    for player in data:
        if position_name == player['player_position_name']:
            filtered_data.add(player['player_name'])
            #returning a list fails test
    return filtered_data 

def count_successful_passes(data):
    """
    Count the number of successful passes (not considering pass outcome).
    """
    pass_count = 0
    for player in data:
        if len(player['pass_success_probability']) > 0 and float(player['pass_success_probability']) > 0.55:
            pass_count += 1

    return pass_count

def filter_by_period(data, period):
    """
    Return a list of events that occurred in the provided period (e.g., 1 or 2).
    """
    filtered_data = []
    for player in data:
        if period == player['period']:
            filtered_data.append(player)
    return filtered_data

def count_shots_by_player(data, player_name):
    """
    Count the number of shots taken by the provided player.
    """
    shot_count = 0
    for player in data:
        if player['player_name'] == player_name and player['event_type_name'] == 'Shot':
            shot_count += 1
            
    return shot_count


# print(read_csv_file('sample_data.csv')[4])