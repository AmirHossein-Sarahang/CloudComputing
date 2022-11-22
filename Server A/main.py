from fastapi import FastAPI, Form
from pydantic import BaseModel
import DB
import Sender
import requests
import json

app = FastAPI()

class adv(BaseModel):
    URL: str
    Email: str
    Description: str

class id_(BaseModel):
    ID: str


@app.post("/POST/")
async def login(ad: adv):
    try:
        id = DB.Insert(ad.Description, ad.Email, ad.URL)
        if Sender.SendMessage(str(id)):
            s = "Your ad was registered with ID : "
            s += str(id)
            return s
        else:
            if Sender.SendMessage(str(id)):
                s = "Your ad was registered in 2nd try with ID : "
                s += str(id)
                return s
    except():
        return "Error in inserting Data or Send id to Server B!"


@app.get("/GET/")
async def login(i: id_):
    s = "Your ad state : "
    s += str(DB.ShowState(i.ID))
    return s