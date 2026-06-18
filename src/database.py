import argparse
from pathlib import Path

BASE_DIR: str = Path(__file__).resolve().parent.parent


def get_database_path():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--db", "-d", default="input.db", help="Database file in project/data/input/"
    )
    args: str = parser.parse_args()
    return BASE_DIR / "data/input" / args.db
