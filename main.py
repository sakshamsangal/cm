import glob
import os
import shutil
from typing import List
import uvicorn
from fastapi import UploadFile, File
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

base_path = ''
app = FastAPI()

script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")


class MoveFile(BaseModel):
    sf: str
    df: str
    fn: str


class MyPath(BaseModel):
    path: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/see-file")
async def see_file(item: MyPath):
    qu = []
    print(item)
    for name in glob.glob(f'static/img/{item.path}/*.jpg'):
        x = os.path.basename(name)
        qu.append(x)
    print(qu)
    return qu



@app.post("/move-file")
async def view(item: MoveFile):
    print(item)
    sf = f'static/img/{item.sf}'
    df = f'static/img/{item.sf}/{item.df}'
    os.makedirs(df, exist_ok=True)
    os.replace(sf + '/' + item.fn, df + '/' + item.fn)
    return {'success': True}



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
