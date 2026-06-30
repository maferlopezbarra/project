
# AutoPIPE Imposed Displacements Processor

A Python-based **ETL + API tool** to process AutoPIPE structural data using SQLite, compute seismic displacements, export results to CSV, and expose the pipeline via a FastAPI service.

The project provides:
- A CLI pipeline for local processing
- A FastAPI REST API for database upload and CSV download
- Automated tests for core modules

---

## Overview

This tool automates the extraction and transformation of structural support data from AutoPIPE databases to provide imposed displacements file.

Workflow:

1. Extracts support data from a SQLite database
2. Calculate seismic drift values
3. Generates formatted CSV output compatible with AutoPIPE

Pipeline:

SQLite (.db) → Extract → Transform → CSV Output

---

## Tech Stack

- Python
- SQLite
- FastAPI
- Pytest
- CSV processing
  
---

## Project Structure
project/
│
├── src/
│   ├── main.py                 # CLI Entry point
│   ├── api.py                  # FastAPI application
│   ├── database.py             # CLI configuration
│   ├── extractors.py           # SQLite data extraction
│   ├── processors.py           # Engineering calculations
│   ├── writers.py              # CSV generation
│   └── services/
│       ├── pipeline.py         # Pipeline orchestration
|       ├── temporary.py        # Temporary file handling
|       └── validation.py       # API file validation
├── tests/
│   ├── test_extractors.py
│   ├── test_processors.py
│   └── test_writers.py
│
├── data/
│   ├── input/                  # CLI input databases
│   └── output/                 # CLI generated files
│
└── README.md

---

## Installation

Create environment:

```bash
python -m venv .venv
```

Activate (Windows):

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## CLI Usage


The CLI processes databases located in:

```
data/input/
```

Run From the project root:

```bash
python -m src.main
```

Custom parameters:

```bash
python -m src.main --db my_database.db --elevation 10300 --factor 250
```

Output:

```
data/output/output.csv
```

---

## API Usage

Start server:

```bash
uvicorn src.api:app --reload
```

API documentation:

```
http://127.0.0.1:8000/docs
```
---

### Endpoint:

POST /displacements

Upload an AutoPIPE SQLite database and receive the generated CSV file.

Form parameters:

- file: SQLite .db file
- elevation: level 0 elevation
- factor: seismic factor

Example:

```bash
curl -X POST \
http://127.0.0.1:8000/displacements \
-F "file=@input.db" \
-F "elevation=10300" \
-F "factor=250"
```

Response:

```
output.csv
```

---

## Engineering Calculation

Drift calculation:

```python
drift = ceil((Z - elevation) / factor)
```

Negative values are limited to zero.

Generated load cases:

- E11
- E13
- E12
- E14

---

## Testing

Run:

```bash
pytest
```

Test cover:

- SQLite extraction
- Drift calculation
- CSV generation

---

## Purpose

This project demonstrates:
- ETL pipeline design
- SQLite data processing
- FastAPI backend development
- File upload handling
- Automated testing

---

## Author
Maria Fernanda Lopez Barra

