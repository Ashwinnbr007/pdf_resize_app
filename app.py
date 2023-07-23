from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
from pathlib import Path
import os
from pdf_service import split_pdf

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process_pdf/")
async def process_pdf(pdf: UploadFile = File(...)):
    file_path = f"uploaded_files/{pdf.filename}"
    os.makedirs("uploaded_files", exist_ok=True) 
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(pdf.file, buffer)
        
    dimension = 3480
    split_pdf(file_path, dimension)

    output_file_path = f"uploaded_files/resized_{pdf.filename}"
    with open(output_file_path, "wb") as output_file:
        shutil.copyfile(file_path, output_file_path)

    return FileResponse(output_file_path, headers={"Content-Disposition": f"attachment; filename=resized_{pdf.filename}"})
