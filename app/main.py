from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

class Array12(BaseModel):
    myKey: List[int]

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/sort", response_model=Array12)
def sort_array(req_array:Array12):
    req_array.myKey.sort()
    return Array12(myKey=req_array.myKey)