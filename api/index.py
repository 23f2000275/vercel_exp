from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Optional
import json

app = FastAPI()

# Enable CORS for all origins and GET methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load data from JSON file
with open("data.json") as f:
    marks_data: Dict[str, int] = json.load(f)

@app.get("/api")
def get_marks(name: Optional[List[str]] = Query(None)) -> Dict[str, List[int]]:
    if name is None:
        raise HTTPException(status_code=400, detail="Query parameter 'name' is required")

    marks = []
    for n in name:
        if n not in marks_data:
            raise HTTPException(status_code=404, detail=f"Name '{n}' not found in data")
        marks.append(marks_data[n])

    return {"marks": marks}
