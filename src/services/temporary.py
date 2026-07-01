from fastapi import File
import tempfile
from pathlib import Path


async def temp_write(file: File) -> str:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as tmp:
        tmp.write(await file.read())
        tmp.flush()
        return Path(tmp.name)


def temp_output() -> Path:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as output:
        return Path(output.name)
