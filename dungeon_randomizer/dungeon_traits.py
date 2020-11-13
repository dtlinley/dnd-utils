doors = [
    {'attribute': 'Wooden', 'weight': 12, 'subtraits': []},
    {'attribute': 'Wooden, barred', 'weight': 1, 'subtraits': []},
    {'attribute': 'Wooden, locked', 'weight': 1, 'subtraits': []},
    {'attribute': 'Stone', 'weight': 8, 'subtraits': []},
    {'attribute': 'Stone, barred', 'weight': 1, 'subtraits': []},
    {'attribute': 'Stone, locked', 'weight': 1, 'subtraits': []},
    {'attribute': 'Iron', 'weight': 4, 'subtraits': []},
    {'attribute': 'Iron, barred', 'weight': 1, 'subtraits': []},
    {'attribute': 'Iron, locked', 'weight': 1, 'subtraits': []},
    {'attribute': 'Portcullis', 'weight': 2, 'subtraits': []},
    {'attribute': 'Portcullis, locked in place', 'weight': 1, 'subtraits': []},
    {'attribute': 'Secret door', 'weight': 2, 'subtraits': []},
    {'attribute': 'Secret door, barred', 'weight': 1, 'subtraits': []},
    {'attribute': 'Secret door, locked', 'weight': 1, 'subtraits': []},
]

chamber_exits = [
    {'attribute': 'Door', 'weight': 1, 'subtraits': [doors]},
    {'attribute': 'Corridor, 10 ft long', 'weight': 1, 'subtraits': []},
]

small_chamber_exits = [
    {'attribute': 'None', 'weight': 5, 'subtraits': []},
    {'attribute': 'One exit', 'weight': 6, 'subtraits': [chamber_exits]},
    {'attribute': 'Two exits', 'weight': 4, 'subtraits': [chamber_exits, chamber_exits]},
    {'attribute': 'Three exits', 'weight': 3, 'subtraits': [chamber_exits, chamber_exits, chamber_exits]},
    {'attribute': 'Four exits', 'weight': 2, 'subtraits': [chamber_exits, chamber_exits, chamber_exits, chamber_exits]},
]

large_chamber_exits = [
    {'attribute': 'None', 'weight': 1, 'subtraits': []},
    {'attribute': 'One exit', 'weight': 6, 'subtraits': [chamber_exits]},
    {'attribute': 'Two exits', 'weight': 6, 'subtraits': [chamber_exits, chamber_exits]},
    {'attribute': 'Three exits', 'weight': 4, 'subtraits': [chamber_exits, chamber_exits, chamber_exits]},
    {'attribute': 'Four exits', 'weight': 1, 'subtraits': [chamber_exits, chamber_exits, chamber_exits, chamber_exits]},
    {'attribute': 'Five exits', 'weight': 1, 'subtraits': [chamber_exits, chamber_exits, chamber_exits, chamber_exits, chamber_exits]},
    {'attribute': 'Six exits', 'weight': 1, 'subtraits': [chamber_exits, chamber_exits, chamber_exits, chamber_exits, chamber_exits, chamber_exits]},
]

chamber_contents = [
    {'attribute': 'Monster (dominant inhabitant)', 'weight': 16, 'subtraits': []},
    {'attribute': 'Monster (dominant inhabitant) with treasure', 'weight': 14, 'subtraits': []},
    {'attribute': 'Monster (pet or allied creature)', 'weight': 10, 'subtraits': []},
    {'attribute': 'Monster (pet or allied creature) guarding treasure', 'weight': 6, 'subtraits': []},
    {'attribute': 'Monster (random creature)', 'weight': 9, 'subtraits': []},
    {'attribute': 'Monster (random creature) with treasure', 'weight': 8, 'subtraits': []},
    {'attribute': 'Dungeon hazard with incidental treasure', 'weight': 8, 'subtraits': []},
    {'attribute': 'Obstacle', 'weight': 5, 'subtraits': []},
    {'attribute': 'Trap', 'weight': 10, 'subtraits': []},
    {'attribute': 'Trap protecting treasure', 'weight': 3, 'subtraits': []},
    {'attribute': 'Trick', 'weight': 4, 'subtraits': []},
    {'attribute': 'Empty room', 'weight': 8, 'subtraits': []},
    {'attribute': 'Empty room with dungeon hazard', 'weight': 6, 'subtraits': []},
    {'attribute': 'Empty room with treasure', 'weight': 6, 'subtraits': []},
]

chambers = [
    {'attribute': 'Square, 20x20 ft', 'weight': 2, 'subtraits': [chamber_contents, small_chamber_exits]},
    {'attribute': 'Square, 30x30 ft', 'weight': 2, 'subtraits': [chamber_contents, small_chamber_exits]},
    {'attribute': 'Square, 40x40 ft', 'weight': 2, 'subtraits': [chamber_contents, small_chamber_exits]},
    {'attribute': 'Rectangle, 15x30 ft', 'weight': 2, 'subtraits': [chamber_contents, small_chamber_exits]},
    {'attribute': 'Rectangle, 20x30 ft', 'weight': 2, 'subtraits': [chamber_contents, small_chamber_exits]},
    {'attribute': 'Rectangle, 30x40 ft', 'weight': 2, 'subtraits': [chamber_contents, small_chamber_exits]},
    {'attribute': 'Rectangle, 30x60 ft', 'weight': 2, 'subtraits': [chamber_contents, small_chamber_exits]},
    {'attribute': 'Rectangle, 50x80 ft', 'weight': 1, 'subtraits': [chamber_contents, large_chamber_exits]},
    {'attribute': 'Circle, 30 ft diameter', 'weight': 1, 'subtraits': [chamber_contents, small_chamber_exits]},
    {'attribute': 'Circle, 50 ft diameter', 'weight': 1, 'subtraits': [chamber_contents, large_chamber_exits]},
    {'attribute': 'Octagon, 40x40 ft', 'weight':0, 'subtraits': [chamber_contents, large_chamber_exits]},
    {'attribute': 'Octagon, 60x60 ft', 'weight': 0, 'subtraits': [chamber_contents, large_chamber_exits]},
    {'attribute': 'Trapezoid, 40x60 ft', 'weight': 0, 'subtraits': [chamber_contents, large_chamber_exits]},
]

passage_widths = [
    {'attribute': '5 ft wide', 'weight': 2, 'subtraits': []},
    {'attribute': '10 ft wide', 'weight': 10, 'subtraits': []},
    {'attribute': '15 ft wide', 'weight': 2, 'subtraits': []},
    {'attribute': '20 ft wide', 'weight': 2, 'subtraits': []},
    {'attribute': '30 ft wide', 'weight': 1, 'subtraits': []},
    {'attribute': '40 ft wide, with row of pillars down the middle', 'weight': 1, 'subtraits': []},
    {'attribute': '40 ft wide, with double row of pillars', 'weight': 1, 'subtraits': []},
    {'attribute': '40 ft wide, 20 ft high', 'weight': 1, 'subtraits': []},
    {'attribute': '40 ft wide, 20 ft high, gallery 10 ft above floor allows access to level above', 'weight': 1, 'subtraits': []},
]

branched_passages = [
    {'attribute': 'Continue straight 30 ft, no doors or side passages', 'weight': 2, 'subtraits': [passage_widths[0:2]]},
    {'attribute': 'Continue straight 20 ft, door to the right, then an additional 10 ft ahead', 'weight': 1, 'subtraits': [passage_widths[0:2], doors]},
    {'attribute': 'Continue straight 20 ft, door to the left, then an additional 10 ft ahead', 'weight': 1, 'subtraits': [passage_widths[0:2], doors]},
    {'attribute': 'Continue straight 20 ft, passage ends in a door', 'weight': 1, 'subtraits': [passage_widths[0:2], doors]},
    {'attribute': 'Continue straight 20 ft, side passage to the right, then an additional 10 ft ahead', 'weight': 0.5, 'subtraits': [passage_widths[0:2]]},
    {'attribute': 'Continue straight 20 ft, side passage to the left, then an additional 10 ft ahead', 'weight': 0.5, 'subtraits': [passage_widths[0:2]]},
    {'attribute': 'Continue straight 20 ft, comes to a dead end', 'weight': 0.5, 'subtraits': [passage_widths[0:2]]},
    {'attribute': 'Continue straight 20 ft, comes to a dead end with a secret door', 'weight': 0, 'subtraits': [passage_widths[0:2]]},
    {'attribute': 'Continue straight 20 ft, then the passage turns left and continues 10 ft', 'weight': 0.5, 'subtraits': [passage_widths[0:2]]},
    {'attribute': 'Continue straight 20 ft, then the passage turns right and continues 10 ft', 'weight': 0.5, 'subtraits': [passage_widths[0:2]]},
    {'attribute': 'Chamber', 'weight': 5, 'subtraits': [chambers]},
    {'attribute': 'Stairs', 'weight': 1, 'subtraits': []},
    {'attribute': 'Continue straight 15 ft, passage ends in a door', 'weight': 1, 'subtraits': [passage_widths[0:2], doors]},
]
branched_passages[1]['subtraits'] = [passage_widths[0:2], doors, branched_passages]
branched_passages[2]['subtraits'] = [passage_widths[0:2], doors, branched_passages]
branched_passages[4]['subtraits'] = [passage_widths[0:2], branched_passages]
branched_passages[5]['subtraits'] = [passage_widths[0:2], branched_passages]
branched_passages[8]['subtraits'] = [passage_widths[0:2], branched_passages]
branched_passages[9]['subtraits'] = [passage_widths[0:2], branched_passages]

passages = [
    {'attribute': 'Continue straight 30 ft, no doors or side passages', 'weight': 2, 'subtraits': [passage_widths]},
    {'attribute': 'Continue straight 15 ft, passage ends in a door', 'weight': 2, 'subtraits': [passage_widths, doors]},
    {'attribute': 'Continue straight 20 ft, door to the right, then an additional 10 ft ahead', 'weight': 1, 'subtraits': [passage_widths, doors]},
    {'attribute': 'Continue straight 20 ft, door to the left, then an additional 10 ft ahead', 'weight': 1, 'subtraits': [passage_widths, doors]},
    {'attribute': 'Continue straight 20 ft, passage ends in a door', 'weight': 1, 'subtraits': [passage_widths, doors]},
    {'attribute': 'Continue straight 20 ft, side passage to the right, then an additional 10 ft ahead', 'weight': 2, 'subtraits': [passage_widths, branched_passages]},
    {'attribute': 'Continue straight 20 ft, side passage to the left, then an additional 10 ft ahead', 'weight': 2, 'subtraits': [passage_widths, branched_passages]},
    {'attribute': 'Continue straight 20 ft, comes to a dead end', 'weight': 0.5, 'subtraits': [passage_widths]},
    {'attribute': 'Continue straight 20 ft, comes to a dead end with a secret door', 'weight': 0.5, 'subtraits': [passage_widths]},
    {'attribute': 'Continue straight 20 ft, then the passage turns left and continues 10 ft', 'weight': 2, 'subtraits': [passage_widths, branched_passages]},
    {'attribute': 'Continue straight 20 ft, then the passage turns right and continues 10 ft', 'weight': 2, 'subtraits': [passage_widths, branched_passages]},
    {'attribute': 'Chamber', 'weight': 5, 'subtraits': [chambers]},
    {'attribute': 'Stairs', 'weight': 1, 'subtraits': []},
]

chamber_exits[1]['subtraits'] = [passages]

starting_areas = [
    {'attribute': 'Square, 20x20 ft; passage on each wall', 'weight': 1, 'subtraits': [passages, passages, passages]},
    {'attribute': 'Square, 20x20 ft; door on two walls, passage on third wall', 'weight': 1, 'subtraits': [doors, doors, passages]},
    {'attribute': 'Square, 40x40 ft; doors on three walls', 'weight': 1, 'subtraits': [doors, doors, doors]},
    {'attribute': 'Rectangle, 80x20 ft, with row of pillars down the middle; two passages leading from each long wall, doors on each short wall', 'weight': 1, 'subtraits': [passages, passages, doors]},
    {'attribute': 'Rectangle, 20x40 ft; passage on each wall', 'weight': 1, 'subtraits': [passages, passages, passages]},
    {'attribute': 'Circle, 40 ft diameter; one passage at each cardinal direction', 'weight': 1, 'subtraits': [passages, passages, passages]},
    {'attribute': 'Circle, 40 ft diameter; one passage in each cardinal direction; well in middle of room', 'weight': 1, 'subtraits': [passages, passages, passages]},
    {'attribute': 'Square, 20x20 ft; door on two walls, passage on third wall, secret door on fourth wall', 'weight': 1, 'subtraits': [passages, doors, doors]},
    {'attribute': 'Passage, 10 ft wide; T intersection', 'weight': 1, 'subtraits': [passages, passages]},
    {'attribute': 'Passage, 10 ft wide; four-way intersection', 'weight': 1, 'subtraits': [passages, passages, passages]},
]

areas_beyond_doors = [
    {'attribute': 'Passage extending 10 ft, then T intersection extending 10 ft to the right and left', 'weight': 2, 'subtraits': [passages, passages]},
    {'attribute': 'Passage 20 ft straight ahead', 'weight': 6, 'subtraits': [passages]},
    {'attribute': 'Chamber', 'weight': 10, 'subtraits': [chambers]},
    {'attribute': 'Stairs', 'weight': 1, 'subtraits': []},
    {'attribute': 'False door with trap', 'weight': 1, 'subtraits': []},
]
