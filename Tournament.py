import pandas as pd 
import player
import random
#set some basic variables. reading the CSV file, getting how many players there are
playersinput = pd.read_csv("players.csv", dtype={'playerID':'str'})
playercount = len(playersinput)
playerspergame = 2
playerlist = []
i=0

#creates the players
while i < playercount:
    firstname = playersinput["FirstName"].loc[[i]]
    lastname = playersinput["LastName"].loc[[i]]
    id = playersinput["playerID"].loc[[i]]
    new_player = player.Player(id, firstname, lastname)
    playerlist.append(new_player)
    #print(new_player.lastname)

    i = i+1

teir1games = playercount/playerspergame
random.shuffle(playerlist)

print(playerlist[0].firstname)



