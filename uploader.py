from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from tempfile import SpooledTemporaryFile
import os

app = FastAPI()

UPLOAD_DIRECTORY = r"C:\Users\saura\OneDrive\Desktop\Project\uploader\uploaded_files"

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Save the file temporarily
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    
    with open(file_path, "wb") as f:
        contents = await file.read()
        f.write(contents)
#    get_file_size(file_path)
    file_size = os.path.getsize(file_path)
    file_size_mb = file_size / (1024 * 1024)
    return {"filename": file.filename, "content_type": file.content_type, "total size": file_size_mb}
