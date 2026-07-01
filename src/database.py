import argparse
from pathlib import Path

BASE_DIR: str = Path(__file__).resolve().parent.parent


def get_database(file):
    return BASE_DIR / "data/input" / file


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--db", "-d", default="input.db", help="Database file in project/data/input/"
    )
    parser.add_argument(
        "--elevation", "-e", default="10300", help="Level 0 elevation", type=float
    )
    parser.add_argument(
        "--factor", "-f", default="250", help="Seismic factor", type=float
    )
    args = parser.parse_args()
    return {
        "db": get_database(args.db),
        "elevation": args.elevation,
        "factor": args.factor,
    }
