import random

class Player:
    def __init__(self, name, bowling, batting):
        """
        Represents a player info in the team.
        Args:
            name (str): The name of the player.
            bowling (float): The bowling skill of the player.
            batting (float): The batting skill of the player.
        """
        self.name = name
        self.bowling = bowling
        self.batting = batting


class Team:
    def __init__(self, name, players):
        """
        Represents the team.

        Args:
            name (str): The name of the team.
            players (list): The list of Player objects representing the team's players.
        """
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = [] #random selection of players
        self.bowlers = [] 
        self.scores = 0  # Total runs scored by the team
        self.wickets = 0  # Total wickets lost by the team
    
    def add_team_members(self, member):
        #Add a new member to the team's list of players
        ##Args: member (Player): The Player object representing the new member to be added to the team.
        self.players.append(member)

    def select_captain(self, captain):
        self.captain = random.choice(self.players)

    def choose_bowler(self):
        available_bowlers = [player for player in self.players if player not in self.bowlers]
        return random.choice(available_bowlers)
    
    def set_batting_order(self):
        """
    shuffles the list of players representing the team's batting order
    in a random order. Each player gets a chance to bat based on this order.
    It's called before starting the match to determine the batting order.

    """
        self.batting_order = random.sample(self.players, len(self.players))
    
    
    def sending_next_player(self):
        #Returns The next Player object from the batting order, or None if the batting order is empty.
        if self.batting_order:
            return self.batting_order.pop(0)
        return None
        
class Umpire:
    def __init__(self, field):
        """
        Args:
            field (Field): The Field object representing the field conditions.
        """
        self.field = field
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def update_score(self, runs): 
        #no. of runs decided by the umpire according to the ball
        self.scores += runs

    def update_wickets(self):
        self.wickets += 1

    def update_overs(self):
        self.overs += 1

    def update_no_ball(self):
        self.no_ball += 1
    
    def update_wide_ball(self):
        self.wide_ball += 1

    def calculate_probability(self,batsman, bowler):
        """
        Calculate the probability of the batsman getting out based on their batting skill and bowler's bowling skill.

        Args:
            batsman (Player): The Player object representing the batsman.
            bowler (Player): The Player object representing the bowler.

        Returns:
            float: The probability of the batsman getting out.
        """
        # Define a base probability of getting out.
        base_prob = 0.5

        # Adjust the base probability based on the batsman's batting skill and bowler's bowling skill.
        batting_factor = batsman.batting
        bowling_factor = 1 - bowler.bowling

        # Combine factors to calculate the adjusted probability.
        adjusted_prob = base_prob + (batting_factor - bowling_factor)

        # Apply a random factor to introduce variability.
        random_factor = random.uniform(0.8, 1.2)
        final_prob = adjusted_prob * random_factor

        # Ensure the probability is within a valid range.
        final_prob = max(0, min(1, final_prob))

        return final_prob
    

    def predict_outcome(self,batsman, bowler):
        """
        Calculate the outcome of a ball based on the probability of the batsman getting out.
        Returns:
            str: The outcome of the ball (either "OUT" or "NOT OUT").
        """
        # Calculate the probability of the batsman getting out.
        probability = self.calculate_probability(batsman, bowler)

        # Generate a random number to determine the outcome.
        random_number = random.random()

        if random_number <= probability:
            return "OUT"
        else:
            return "NOT OUT"

    


class Match:
    def __init__(self, team1, team2, field, total_overs):
        """
        Initialize a cricket match between two teams.

        Args:
            team1 (Team): The first team participating in the match.
            team2 (Team): The second team participating in the match.
            field (Field): The field conditions and settings for the match.
            total_overs (int): The total number of overs in the match.
        """
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.total_overs = total_overs
        self.umpire = Umpire(field) 
        self.commentator = Commentator(self.umpire)


    def start_match(self):
        self.team1.select_captain(self.team1)
        self.team2.select_captain(self.team2)

        self.team1.set_batting_order()  
        self.team2.set_batting_order()  

        self.commentator.describe_game(self.team1.captain.name, self.team2.captain.name, self.team1.name, self.team2.name, over=self.total_overs)

        self.play_innings(self.team1, self.team2)
        self.play_innings(self.team2, self.team1)

        self.commentator.describe_final_result(self.team1.name, self.team1.scores, self.team2.name, self.team2.scores)


    def play_innings(self, batting_team, bowling_team):
        ball_count = 1
        over = 0
        bowler = bowling_team.choose_bowler()
        batsman = batting_team.sending_next_player()

        while over < self.total_overs:
            if batsman is None:
                break

            self.commentator.current_info(ball_count)
            ball_description, runs = self.commentator.describe_ball(batsman, bowler)

            if ball_description.endswith("OUT!"):
                self.umpire.update_wickets()
                print(f"Wickets: {self.umpire.wickets}, Overs: {self.umpire.overs}")
                print(f"New player {batsman.name} is playing...")
                batsman = batting_team.sending_next_player()
            else:
                self.umpire.update_score(runs)

            if ball_count > 5:
                over += 1
                print(f"Over {over} Starting...")
                self.umpire.update_overs()
                bowler = bowling_team.choose_bowler()
                ball_count = 0

            ball_count += 1


class Commentator:
    def __init__(self, umpire):
        self.umpire = umpire

    def describe_game(self, captain1, captain2, country1, country2, over):
        print("--------- Game Information ---------")
        print(f"{country1} Vs {country2}")
        print(f"Captain 1: {captain1}, Captain 2: {captain2}")
        print(f"Over: {over}")
        print("-------------------------------------")

    def describe_start(self, team):
        print("------------- GAME STARTED ------------------")
        print(f"Team {team} is playing:")
    
    def current_info(self, ball_count):
        """
        Args:
            ball_count (int): The count of balls played in the current over.
        """
        print(f"Balls: {ball_count} Over: {self.umpire.overs} Run: {self.umpire.scores}  Wicket: {self.umpire.wickets}")

    def describe_ball(self, batsman, bowler):
        """
        Args:
            batsman (Player): The Player object representing the batsman.
            bowler (Player): The Player object representing the bowler.
            runs_scored (int): The runs scored in the ball.
        """
        outcome = self.umpire.predict_outcome(batsman, bowler)
        print("Outcome: ", outcome)
        if outcome == "OUT":
            description = f"{batsman.name} is OUT!"
            runs_scored = 0
        else:
            runs_scored = random.randint(0, 6)
            description = f"{batsman.name} plays the shot and scores {runs_scored} run(s)."

        return description, runs_scored

    def describe_out(self, batsman):
        print(f"{batsman} is OUT!")

    def describe_over(self, total_runs, wickets, overs_played):
        print(f"End of over {overs_played}. Total runs: {total_runs}, Wickets: {wickets}")

    def describe_end(self, total_runs, wickets):
        print(f"End of innings. Total runs: {total_runs}, Wickets: {wickets}")

    def describe_final_result(self, team1_name, team1_scores, team2_name, team2_scores):
        print(" Winner ")
        if team1_scores > team2_scores:
            print(f"TEAM: {team1_name} WON")
        else:
            print(f"TEAM: {team2_name} WON")
        print("---------------------------------------------")

    def predict_outcome(self, batsman, bowler):
        batting_prob = self.calculate_probability(batsman, bowler)
        if batting_prob > 0.5:
            return "OUT"
        return "NOT OUT"

    

class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        """
        Represents the field conditions for the match.

        Args:
            size (str): The size of the field.
            fan_ratio (float): The fan ratio of the field.
            pitch_conditions (float): The pitch conditions of the field.
            home_advantage (float): The home advantage of the field.
        """
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

# Starting a game
player1 = []
any = random.random()
for i in range(12):
    player1.append(Player("Player1_" + str(i+1), round(any, 1), round(any, 1)))
    
player2 = []
for i in range(12):
    player2.append(Player("Player2_" + str(i+1), round(any, 1), round(any, 1)))

# Adding players to team
team1 = Team("Country1", player1)
team2 = Team("Country2", player2)

# showing the field
field = Field("Large", 0.5, 0.6, 0.7)

# starting match simulation
total_overs = 50  
match = Match(team1, team2, field, total_overs)
match.start_match()