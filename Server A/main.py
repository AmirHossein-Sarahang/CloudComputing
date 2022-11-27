import DB
import Sender
import requests
import shutil
import S3DB
from fastapi import FastAPI, File, UploadFile, Form
import DB2ndConection
app = FastAPI()

@app.post("/POST/")
async def handle_post(file: UploadFile = File(), Email: str = Form(), Description: str = Form(), URL: str = Form()):
    try:
        id = DB.Insert(Description, Email, URL)
        s1 = "Your ad was registered with ID : "
        if Sender.SendMessage(str(id)):
            s1 += str(id)

        s2 = "./data/"
        s2 += str(id)
        s2 += ".jpg"
        with open(s2, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        S3DB.Upload_to_s3(s2, str(id))
        return s1
    except():
        print()

@app.get("/GET/")
async def handle_post(id: str = Form()):
    return DB2ndConection.ShowState(id)

