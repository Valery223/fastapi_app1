from schemas.creature import Creature

_creatures = [
    Creature(name="yeti",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="AbominaЫe Snowman",
),
    Creature(name="Bigfoot",
             aka="Sasquatch",
             description="New world Cousin Eddie of the yeti",
             country="US",
             area="*"),
    ]


def get_all() -> list[Creature]:
    """Return all creatures"""
    return _creatures

def get_one(name: str) -> Creature | None:
    """Return one creature"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

# The following are non-functional for now,
# so they just act like they work, without modifying
# the actual fakes list:
def create(creature: Creature) -> Creature:
    """Add a creature"""
    return creature

def modify(name: str, creature: Creature) -> Creature:
    """Partially modify a creature"""

    return creature

def delete(name: str) -> None:
    """Delete a creature"""
    return None