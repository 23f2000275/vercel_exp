from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Optional
from pathlib import Path
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load data.json
data_path = Path(__file__).parent / "data.json"
with data_path.open() as f:
    marks_data: Dict[str, int] = json.load(f)

@app.get("/api")
def get_marks(request: Request)
    parameters=list()
    for par_name in request.query_params.getlist("name"):
        parameters.append(par_name)
    marks = []
    for n in par_name:
        if n not in marks_data:
            return {"marks": []}
        marks.append(marks_data[n])
    return {"marks": marks}

