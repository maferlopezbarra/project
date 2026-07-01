from fastapi import HTTPException, UploadFile


def run_validation(file: UploadFile):
    if not file.filename.endswith(".db"):
        raise HTTPException(status_code=400, detail="Only .db files are accepted")
