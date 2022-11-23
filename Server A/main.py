import DB
import Sender
import requests
import shutil
from fastapi import FastAPI, File, UploadFile, Form

app = FastAPI()

@app.post("/POST/")
async def handle_post(file: UploadFile = File(), Email: str = Form(), Description: str = Form(),URL: str = Form()):
    try:
        id = DB.Insert(Description, Email, URL)
        if Sender.SendMessage(str(id)):
            s = "Your ad was registered with ID : "
            s += str(id)
            return s
        s = "./data/"
        s += file.filename

        with open(s, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    except():
        print()

@app.get("/GET/")
async def handle_post(id: str = Form()):
    return DB.ShowState(id)