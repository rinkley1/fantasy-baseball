import csv

# This class is the container that organizes the data from the CSV into something a little easier to process: a list
# The teams are sorted alphabetically
class CSV_Cleanup:
    def __init__(self):
        self.teams_linebyline = []

    def organize_team_and_score(self, week_data):
        for team, score in sorted(week_data):
            self.teams_linebyline.append([team, score])

# This class is a container for the week-by-week team records and winning percentage
class Team:
    def __init__(self, name: str):
        self.name = name
        self.scores = [] # List of scores (e.g., ["4-5-1", "6-2-2"])
        # We're starting these off at 0, and we'll add to them
        self.wins = 0
        self.losses = 0
        self.ties = 0

    # We're breaking down the results into wins, losses, and ties
    # We'll use "4-5-1" as the example result data
    # We then aggregate the results
    def update_record(self, score):
        try:
            # For some reason the ties were give a prefix of '200', so I remove that here
            # So technically I lied about the result data we would use. It actually said "4-5-2001".
            score = score.replace("200", "")
            # '.split' splits the result data into three pieces, using the '-' as the spot where we split
            # '.split' turns the result data into a list of strings: "4", "5", and "1"
            # 'map' lets me apply a function to each item in that list. 'int' is that function. Now every item is a number.
            # 'list' then creates a list of those ints, which are numbers that we can apply some math too
            score_parts = list(map(int, score.split("-")))
            # Each of these add the numbers to the corresponding container we set up in __init__
            # 'x += y' basically means making x = x+y
            self.wins += score_parts[0]
            self.losses += score_parts[1]
            self.ties += score_parts[2]
        except ValueError:
            pass

    # Here we go, people! We're calculating the win percentage based on the updated values in the container.
    def calculate_winning_percentage(self):
        total_games = self.wins + self.losses + self.ties
        # To cover the first week
        if total_games == 0:
            return 0.0
        # The formula!
        percentage = (self.wins + (self.ties / 2)) / total_games
        # We only want the results up to 3 decimal points
        return f"{percentage:.3f}"

def main():
    """
    Reads team names and their corresponding scores for a given week from a CSV file.

    Args:
        filename (str): The path to the CSV file.
        column_index (int): The column index to extract data for each team.

    Writes:
        list of tuples: A list where each tuple contains a team name and its updated winning percentage.
    """

    filename = 'FantasySeason_Sheet.csv'
    cleanup = CSV_Cleanup()

    # Loop through each of the 22 weeks. You have to say '(1, 23)' because it goes up to but not including 23.
    # It loops through all 10 teams in the column, then moves to the next
    for week_number in range(1, 23):
        # Adjust column_index based on week number, using '- 1' because we want column_index to start at 0, the first column.
        week_data = read_week_data(filename, column_index=week_number - 1)
        cleanup.organize_team_and_score(week_data)
    write_to_csv(cleanup.teams_linebyline)

def read_week_data(filename, column_index):
    """
    We are reading the CSV file, and adding the team name to a list, and scores to a list.
    This is just so we have something more digestible for adding to the Classes.
    """
    teams = []
    scores = []

    with open(filename) as file:
        reader = csv.reader(file)
        # 'enumerate' makes it so each row is numbered
        # 'row_index' is the line number, and 'row' helps us access the actualy data
        for row_index, row in enumerate(reader):
            # '% 2' asks for the remainder when divided by 2, so basically this asks if the row is even numbered
            # The teams are on the odd rows but in programming, the first line indexes as 0
            if row_index % 2 == 0:
                # Append team names from the specified column index
                teams.append(row[column_index])
            else:
                # The "else" means this looks at odd numbered rows
                # Append scores from the specified column index
                scores.append(row[column_index])

    # Combine teams and scores into a list of tuples
    return list(zip(teams, scores))

def write_to_csv(cleanup):
    # The name of the file we're creating!
    output_name = 'record_weekbyweek.csv'

    # This makes a list with all the teams from the Class "Team"
    teams = [
        Team(name="Big Bats Bigger... Fielders"),
        Team(name="Daniel's Daring Team"),
        Team(name="Idaho Can Of Corn"),
        Team(name="If You Ain't First, You're Last"),
        Team(name="Kevin's Top-Notch Team"),
        Team(name="No Acuna Matata"),
        Team(name="Shohei's Fried Chicken"),
        Team(name="Team Brock"),
        Team(name="Team Roy Hobbs"),
        Team(name="Witt or Without Yu"),
    ]

    # Making an empty list for all the results
    team_weekly_results = [

    ]

    # Here we are creating the function that will create (write to) a new CSV!
    with open(output_name, mode='a', newline='') as outfile:
        writer = csv.writer(outfile)
        # Access the organized list from the CSV_cleanup Class, and process each row
        for row_team, score in cleanup:
            # Check if the current team is the team we're tracking, since we go through each team alphabetically 22 times
            for team in teams:
                if row_team == team.name:
                    # Update record using Class function
                    team.update_record(score)
                    # Adds to 'team_weekly_results' list with two keys: name and winning percentage
                    team_weekly_results.append([team.name, team.calculate_winning_percentage()])
        # 'sorted' expects a function for the second input, so we use lambda
        # 'key=lambda x: x[0]' lets us sort by the first item (x[0]) in the team_weekly_results list
        # The first item is the team names
        teams_sorted = sorted(team_weekly_results, key=lambda x: x[0])
        # Now we write! One team and winning percentage, 22 times for each week, then the next team. 220 rows.
        for team_name, winning_percentage in teams_sorted:
            writer.writerow([team_name, winning_percentage])

if __name__ == "__main__":
    main()