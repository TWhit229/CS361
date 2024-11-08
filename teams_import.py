from flask import Flask, jsonify

# Defining the Player class
class Player:
    def __init__(self, first_name, last_name, number, position, stats):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.position = position
        self.stats = stats

# Defining the Team class
class Team:
    def __init__(self, name, wins, losses, head_coach, location):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.head_coach = head_coach
        self.location = location
        self.players = []  # Initialize an empty list for players

    def add_player(self, player):
        self.players.append(player)

# Function to load team data from a text file
def load_team_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Extract team info
        team_name = lines[0].strip()
        wins = int(lines[1].strip())
        losses = int(lines[2].strip())
        head_coach = lines[3].strip()
        location = lines[4].strip()

        # Create Team object
        team = Team(name=team_name, wins=wins, losses=losses, head_coach=head_coach, location=location)

        # Extract player info
        for line in lines[6:]:  # Start from line 6, skipping the 'Players:' line
            if line.strip():  # Ignore empty lines
                player_data = line.strip().split(', ')
                if len(player_data) >= 5:  # Ensure there are enough elements
                    first_name = player_data[0]
                    last_name = player_data[1]
                    number = int(player_data[2])
                    position = player_data[3]
                    stats = player_data[4]

                    # Create Player object and add to team
                    player = Player(first_name, last_name, number, position, stats)
                    team.add_player(player)

        return team

# Load all teams from their respective text files
def load_all_teams(file_paths):
    teams = []
    for file_path in file_paths:
        team = load_team_from_file(file_path)
        teams.append(team)
    return teams

# Example usage
file_paths = [
    'Teams/arizona_cardinals.txt',
    'Teams/atlanta_falcons.txt',
    'Teams/carolina_panthers.txt',
    'Teams/chicago_bears.txt',
    'Teams/dallas_cowboys.txt',
    'Teams/detroit_lions.txt',
    'Teams/green_bay_packers.txt',
    'Teams/los_angeles_rams.txt',
    'Teams/minnesota_vikings.txt',
    'Teams/new_orleans_saints.txt',
    'Teams/new_york_giants.txt',
    'Teams/philadelphia_eagles.txt',
    'Teams/san_francisco_49ers.txt',
    'Teams/seattle_seahawks.txt',
    'Teams/tampa_bay_buccaneers.txt',
    'Teams/washington_commanders.txt',
    'Teams/baltimore_ravens.txt',
    'Teams/buffalo_bills.txt',
    'Teams/cincinnati_bengals.txt',
    'Teams/cleveland_browns.txt',
    'Teams/denver_broncos.txt',
    'Teams/houston_texans.txt',
    'Teams/indianapolis_colts.txt',
    'Teams/jacksonville_jaguars.txt',
    'Teams/kansas_city_chiefs.txt',
    'Teams/las_vegas_raiders.txt',
    'Teams/los_angeles_chargers.txt',
    'Teams/miami_dolphins.txt',
    'Teams/new_england_patriots.txt',
    'Teams/new_york_jets.txt',
    'Teams/pittsburgh_steelers.txt',
    'Teams/tennessee_titans.txt'
]

teams = load_all_teams(file_paths)

# Create a Flask app to serve the teams data
app = Flask(__name__)

# Custom function to convert team and player objects to a serializable dictionary
def serialize_team(team):
    return {
        'name': team.name,
        'wins': team.wins,
        'losses': team.losses,
        'head_coach': team.head_coach,
        'location': team.location,
        'players': [
            {
                'first_name': player.first_name,
                'last_name': player.last_name,
                'number': player.number,
                'position': player.position,
                'stats': player.stats
            } for player in team.players
        ]
    }

# Define a route to get all teams
@app.route('/teams', methods=['GET'])
def get_teams():
    teams_dict = [serialize_team(team) for team in teams]
    return jsonify(teams_dict)

if __name__ == '__main__':
    app.run(port=5000)
