import argparse
from pathlib import Path

BASE_DIR: str = Path(__file__).resolve().parent.parent


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
    args: str = parser.parse_args()
    return {"db": BASE_DIR / "data/input" / args.db, "elevation": args.elevation, "factor": args.factor}
