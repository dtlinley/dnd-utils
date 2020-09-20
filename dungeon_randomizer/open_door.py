import dungeon_traits
import dungeon_randomizer
import pprint

def createDungeon():
    return dungeon_randomizer.pickTrait(dungeon_traits.areas_beyond_doors)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(createDungeon())
