from src.extractors import support_coordinates
from src.processors import displacements

def run_displacements(db: str, elevation: float, factor: float) -> list[dict]:
    supports: list[tuple] = support_coordinates(db)
    return displacements(supports, elevation, factor)