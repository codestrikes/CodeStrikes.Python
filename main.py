from bots.boxer import Boxer
from bots.kickboxer import Kickboxer
from playerBot import PlayerBot
from sdk.fight import Fight
from sdk.standardGameLogic import StandardGameLogic

playerBot = PlayerBot()
kickboxer = Kickboxer()
boxer = Boxer()

print("Executing fight: %s vs %s" % (playerBot, kickboxer))
fight = Fight(playerBot, kickboxer, StandardGameLogic())
result = fight.execute()

print("Result: %s" % result)
print()

print("Executing fight: %s vs %s" % (playerBot, boxer))
fight = Fight(playerBot, kickboxer, StandardGameLogic())
result = fight.execute()

print("Result: %s" % result)
print()
