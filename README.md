# Cricket-Game-Simulation
## A simulation code for a cricket  game using Python
#### The code simulates a simple cricket match.
## Classes:

### Class Player
  It starts with class Player that contains important information that should be known about them. no functions needs to be defined inside this class.\
arguments are: 
* name (str): The name of the player.
* bowling (float): The bowling skill of the player.
* batting (float): The batting skill of the player.
    


### Class Team
  represents the team and how it's structured.               
  functions within this class are for the purpose of adding members and assigning roles.\
  arguments are:
  * name (str): The name of the team.
  * players (list): The list of Player objects representing the team's players.


### Class Umpire
  This class simulates the rule of an umpire of a game and functions are surving those rules in terms of counting runs, wickets, overs and finally calculating the outcome to determine whether an LKW shot will kick the batsman out or not.\
arguments are:
* field (Field): The Field object representing the field conditions.


### Class Match
  It dispalys a simulation of the steps included to play a matc.\
it contains the folllowing functions:
* 1-play_innings:\
taking the arguments "batting_team" and "bowling_team" objects from Team calss.\
It starts counting balls at 1 with 0 overs completed, then selects a bowler and a batsman from predefined functions in Team class.\
goes over a loop on the number of overs completed whether they were 20 or 50 and as long as there are batsman in the team, the match displays the info of the current match and the description of the ball using a predefined function from Commentator class.\
depending on the returned value of the "describe_ball" function, the umpire object steps in and makes the decision, updates wickets, updates scores and increases ball count and over count if ball count is over 6.

* 2- start_match:
contains objects from Team, Commentator and Match class which call important functions to start a game.\
Startes with selecting teams captains, then setting batting order, then describing the game and finally play the innings.\


### Class Commentator
This calss dispalys a comment on every ball shot in the match to help umpire and audience track the scores of the match.\
This is atchieved through several functions like:
* "describe game" that describes the basic info about the game.
* "describe_start" showes which team will start batting.
* "current_info" keeps updating during the game to record each score.
* "describe_ball" s description of the ball played by the batsman, whether this ball will get the batsman out of game or it will increase the count of runs by 4 or 6.
* "describe_out", "describe_over", "describe_end" description for the excluded batsman, count of overs and declaration of the end of the game.
* "predict_outcome" it takes the bowler and the batsman as arguments and and calculates the batting prob by calling "calculate_probability" function from Umpire class.



### Class Field
  Describes the condition of the field and has no functions.\
arguments are:
* size (str): The size of the field.\
* fan_ratio (float): The fan ratio of the field.\
* pitch_conditions (float): The pitch conditions of the field.\
* home_advantage (float): The home advantage of the field.



## Game intialization 
* creating random data for the players in both teams.
* passing playes lists as arguments to Team class objects.
* describig the field with data passed on to the Field class object.
* setting the total overs for the game with 50.
* pass on both teams, field description, and number of total overs to match object form Match class.
* call "start_match" function.
