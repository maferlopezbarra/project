from src.extractors import support_coordinates
from src.processors import displacements
from src.writers import repeat
from pathlib import Path


def run_pipeline(db: Path, elevation: float, factor: float, output_path: Path):
    supports: list[tuple] = support_coordinates(db)
    nodes = displacements(supports, elevation, factor)
    repeat(nodes, output_path)
    return None
