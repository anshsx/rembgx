from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app.remove_bg import remove_background
import shutil
import os
import uuid

app = FastAPI()

# Enable CORS (Allow all origins for testing; restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://xapwerx.vercel.app"],  # Replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
RESULTS_DIR = "results"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

@app.post("/remove-bg/")
async def remove_bg(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    input_path = f"{UPLOAD_DIR}/{file_id}.png"
    output_path = f"{RESULTS_DIR}/{file_id}.png"
    
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    remove_background(input_path, output_path)
    
    return FileResponse(output_path, media_type="image/png")

@app.get("/")
def home():
    return {"message": "Background Remover API is running!"}
