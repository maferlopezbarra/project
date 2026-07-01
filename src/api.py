from fastapi import FastAPI, Form, File, UploadFile, BackgroundTasks
from fastapi.responses import FileResponse
from pathlib import Path

import os

from src.services.pipeline import run_pipeline
from src.services.validation import run_validation
from src.services.temporary import temp_write, temp_output


app = FastAPI()



@app.get("/")
def health():
    return {"status": "ok"}



@app.post("/displacements")
async def calculate_displacements(
    background_tasks: BackgroundTasks,
    file: UploadFile,
    elevation: float = Form(default=10300),
    factor: float = Form(default=250)
):
    
    run_validation(file)

    tmp_path = await temp_write(file)
    output_path = temp_output()

    run_pipeline(tmp_path, elevation, factor, output_path)
    
    background_tasks.add_task(os.remove,tmp_path)
    background_tasks.add_task(os.remove, output_path)
    
    
    return FileResponse(
        path=output_path,
        filename="output.csv",
        media_type="text/csv"
    )

    

