import pytest
import sqlite3
from src.extractors import support_coordinates


def test_errors():
    with pytest.raises(FileNotFoundError):
        support_coordinates("none")
    with pytest.raises(ValueError):
        support_coordinates("src/main.py")

    
        