from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from utils import is_cyclic

app = FastAPI()


@app.get("/")
async def root():
    return {is_cyclic([3, 0, 1, 2])}
