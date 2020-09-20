import dungeon_traits
import dungeon_randomizer
import pprint

def createDungeon():
    return dungeon_randomizer.pickTrait(dungeon_traits.starting_areas)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(createDungeon())
