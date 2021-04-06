# In JS we use function nameOfFunction(variables) {
# }
# In Python we use def nameOfFunction(variables):

class Game:
    # initializing the basics of the game
    def __init__(self, gameName, maxPlayers, gameDescription):
        self.gameName  = gameName
        self.maxPlayers = maxPlayers
        self.gameDescription = gameDescription
        self.gameRules = []

    def gameInfo(self):
        if self.maxPlayers == 1:
            print(f"{self.gameName} is a game that has {self.maxPlayers} player and is {self.gameDescription}")
        else:
            print(f"{self.gameName} is a game that can have up to {self.maxPlayers} players and is {self.gameDescription}")

    def addRule(self, rule):
        self.gameRules.append(rule)

    def theRules(self):
        if self.gameRules:
            print(f"{self.gameName} has the following rules {self.gameRules}")
        else:
            print(f"{self.gameName} currently has not set up any rules")

# Create New Games here

testing = Game("Test Game", 2, "a test game")
# creating var testing (how we will call the new game) saying we will use the class Game and () has the required variables about the game
treasures = Game("Hidden Treasures", 1, "Single Player Adventure game")

# Add the optional items to each game

testing.addRule("No Cheating")
testing.addRule("Test Rule")



# These actually print something to the terminal for the user to see
testing.gameInfo()
testing.theRules()

treasures.gameInfo()
treasures.theRules()

class NewGame:
    pass