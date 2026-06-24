from typing import Annotated
from fastapi import FastAPI, Query
from src.services.displacement_service import run_displacements

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/displacements")
async def run_pipeline(
    db: Annotated[str, Query(description="Path to SQLite database")],
    elevation: Annotated[float, Query()] = 10300,
    factor: Annotated[float, Query()] = 250
    ) -> list[dict]:
    
    return run_displacements(db, elevation, factor)
    

    

