import sqlite3
from pathlib import Path


def support_coordinates(file: Path) -> list[tuple]:
    if not Path(file).exists():
        raise FileNotFoundError("Database not found")
    try:
        conn = sqlite3.connect(file)
        query = """
        SELECT DISTINCT 
            support.point, point."Global Z (mm)" 
        FROM support 
        INNER JOIN point 
            ON support.point = point."to"
        """
        rows: list = conn.execute(query).fetchall()
    except (sqlite3.OperationalError, sqlite3.DatabaseError):
        raise ValueError("Database format not allowed")
    finally:
        if conn is not None:
            conn.close()

    return rows
