from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import uuid
from model import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type", "Authorization"],
)

TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {".wav", ".mp3", ".ogg", ".flac"}

#route to predict
@app.post("/predict/")
async def classify_audio(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[1].lower()

    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Formato de archivo no permitido. Usa WAV, MP3, OGG o FLAC.")

    unique_filename = f"{uuid.uuid4().hex}{file_ext}"
    file_path = os.path.join(TEMP_DIR, unique_filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = predict(file_path)
        os.remove(file_path)
        return {"prediction": str(result)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando el archivo: {str(e)}")

