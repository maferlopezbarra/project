import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
file_output = BASE_DIR / "data/output/output.csv"


def repeat(nodes: list[dict], output=file_output):

    output.parent.mkdir(exist_ok=True)

    with open(output, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Support",
                "Case",
                "Support Group No.",
                "Translation-X",
                "Translation-Y",
                "Translation-Z",
                "Rotation-X",
                "Rotation-Y",
                "Rotation-Z",
            ],
        )
        writer.writeheader()

        for row in nodes:
            cases = [
                ("E11", row["drift"], 0),
                ("E13", -row["drift"], 0),
                ("E12", 0, row["drift"]),
                ("E14", 0, -row["drift"]),
            ]

            for case, x, y in cases:
                writer.writerow(
                    {
                        "Support": row["node"],
                        "Case": case,
                        "Support Group No.": "",
                        "Translation-X": x,
                        "Translation-Y": y,
                        "Translation-Z": 0,
                        "Rotation-X": 0,
                        "Rotation-Y": 0,
                        "Rotation-Z": 0,
                    }
                )
