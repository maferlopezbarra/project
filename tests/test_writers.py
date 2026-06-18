import pytest
import csv
from src.writers import repeat


def test_repeat(tmp_path):

    file_output= tmp_path / "output.csv"

    nodes = [{"node": "A10", "drift": 21}]

    repeat(nodes,file_output)

    with open(file_output) as file:
        reader = list(csv.DictReader(file))

        assert len(reader) == 4
        assert reader[0]["Support"] == "A10"
        assert reader[1]["Case"] == "E13"
        assert reader[2]["Translation-Y"] == "21"