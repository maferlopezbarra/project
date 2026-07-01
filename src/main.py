from src.extractors import support_coordinates
from src.processors import displacements
from src.writers import repeat
from src.database import get_config


def main():
    config: dict = get_config()
    supports: list = support_coordinates(config["db"])
    repeat(displacements(supports, config["elevation"], config["factor"]))


if __name__ == "__main__":
    main()
