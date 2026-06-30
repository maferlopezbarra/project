from fastapi import FastAPI, Form, File, UploadFile, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import tempfile
import os

from src.services.displacement_service import run_displacements
from src.writers import repeat

app = FastAPI()



@app.get("/")
def health():
    return {"status": "ok"}



@app.post("/displacements")
async def run_pipeline(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    elevation: float = Form(default=10300),
    factor: float = Form(default=250)
):
    if not file.filename.endswith(".db"):
        raise HTTPException(
            status_code=400,
            detail="Only .db files are accepted"
        )
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as tmp:
        tmp.write(await file.read())
        tmp.flush()
        tmp_path = tmp.name
    
    output_path = Path(tempfile.NamedTemporaryFile(delete=False, suffix=".csv").name)

    nodes = run_displacements(tmp_path, elevation, factor)
    
    repeat(nodes, output_path)
    background_tasks.add_task(os.remove,tmp_path)
    background_tasks.add_task(os.remove, output_path)
    
    
    return FileResponse(
        path=output_path,
        filename="output.csv",
        media_type="text/csv"
    )

    

