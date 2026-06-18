
# AutoPIPE Imposed Displacements Processor

A Python-based ETL (Extract–Transform–Load) tool to process AutoPIPE data using SQLite, compute displacements, and export results to CSV.

---

## Overview

This project extracts structural support data from a SQLite database, processes it to compute drift values, and generates formatted output for further engineering use.

The workflow follows a clean pipeline:

- **Extract**: Read support nodes and coordinates from a database
- **Transform**: Calculate drift values in accordance with seismic structural requirements
- **Load**: Export results to CSV format compatible with AutoPIPE

---
## Project Structure
project/
│
├── src/
│   ├── main.py           # Entry point
│   ├── database.py       # CLI + database path handling
│   ├── extractors.py     # SQLite queries
│   ├── processors.py     # Data processing and calculations
│   └── writers.py        # CSV output generation
│
├── tests/
│   ├── test_extractors.py
│   ├── test_processors.py
│   └── test_writers.py
│
├── data/
│   ├── input/            # Input database files
│   └── output/           # Generated CSV files
│
└── README.md

---

## Requirements

- Python 3.9+

Optional (for testing):

```bash
pip install pytest
```
---

## Usage

### Run the program

From the project root:

```bash
python -m src.main
```
### Specify a custom database file
```bash
python -m src.main --db my_database.db
```
- The database must be located in: data/input

## Output
- The script generates a CSV file: data/output/output.csv
- Each support includes drift values for 4 load cases:
  - E11
  - E13
  - E12
  - E14

## How It Works

### Extract
Retrieves node coordinates from the SQLite database using a JOIN between support and point tables.

### Transform
Dirft is calculated using:
```bach
drift = ceil((Z - 10300) / 250)
```
- Parameters 10300 and 250 have been implemented per default and can be costumized.
- Negative values are clamped to 0

### Load
Writes results into a CSV file formatted for AutoPIPE import.

## Features
- Clean modular design
- CLI support with argparse
- SQLite integration
- No external dependencies
- Fully testable pipeline
- Automatic output directory creation

## Autor
Maria Fernanda Lopez Barra

## License
This project is for educational and engineering automation purposes.
