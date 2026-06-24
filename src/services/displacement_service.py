from src.extractors import support_coordinates
from src.processors import displacements
from src.database import get_database

def run_displacements(db: str, elevation: float, factor: float) -> list[dict]:
    supports: list[tuple] = support_coordinates(get_database(db))
    return displacements(supports, elevation, factor)