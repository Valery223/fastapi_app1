from schemas.explorer import Explorer

_explorers = [
    Explorer(name="Claude Hande",
    country="FR",
    description="Scarce during full moons"),
Explorer(name="Noah Weiser",
    country="DE",
    description="Myopic machete man"),
]

def get_all() -> list[Explorer]:
    return _explorers

def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def create_explorer(explorer: Explorer) -> Explorer:
    """Create explorer"""
    return explorer

def modify(explorer: Explorer) -> Explorer:
    """Частное изменение записи исследователя"""
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """Replace исследователя"""
    return explorer

def delete(name: str) -> bool:
    """Delete explorer"""
    return None


