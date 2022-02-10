import os
import json

from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sc2util import get_replay_data

BASE_PATH = os.path.dirname(__file__)

templates = Jinja2Templates(directory=os.path.join(BASE_PATH, "templates"))

app = FastAPI(title="SC2 BBR")
app.mount("/s", StaticFiles(directory="static"), name="static")

@app.get("/", status_code=200)
def root(request: Request) -> dict:
    """
    Root GET
    """

    return templates.TemplateResponse(
        "index.html",
        {"request": request},
    )

@app.get("/credits", status_code=200)
def root(request: Request) -> dict:
    """
    Root GET
    """

    return templates.TemplateResponse(
        "credits.html",
        {"request": request},
    )

@app.post("/play")
async def create_file(request: Request, replay: UploadFile):
    data = get_replay_data(replay.file)

    nouns = set()
    for event in data['events']:
        nouns.add(event.noun)

    return templates.TemplateResponse(
        "play.html",
        {"title": f"Play {replay.filename}", "request": request, "replay_file": replay,
            "replay": data, "nouns": nouns, "replay_json": json.dumps(data)},
    )
