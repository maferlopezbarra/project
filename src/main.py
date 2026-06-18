from extractors import support_coordinates
from processors import displacements
from writers import repeat
from database import get_database_path




def main():

    repeat(displacements(support_coordinates(get_database_path())))


if __name__ == "__main__":
    main()
