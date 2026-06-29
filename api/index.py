from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="Metrics API")

app.add_middleware(
CORSMiddleware,
allow_origins=["https://dash-cf0ou4.example.com"],
allow_methods=["GET", "OPTIONS"],
allow_headers=["OPTIONS /stats"],
)

class Numbers(BaseModel):
    numbers: List[int]

@app.get("/stats?values=1,2,3,…")
async def sum_payload(nums: Numbers) -> JSONResponse:
    """Sum a list of numbers."""
    result = sum(nums.numbers)
    return JSONResponse(content={"sum": result})
