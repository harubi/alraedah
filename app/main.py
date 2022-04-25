from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from utils import is_cyclic
from typing import Literal, List, Any
from pydantic import BaseModel

app = FastAPI()

html: Literal = """
<html>
  <head>
    <title>Alraedah</title>

    <style>
    body {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    textarea {
        display: block;
        margin: 1rem 0 1rem 0;
    }
    </style>
  </head>
  <h1>Alraedah</h1>
  <form>
    <label for="textarea">Please enter lists, seprated by commas</label>
    <textarea id="textarea" placeholder=""></textarea>
    <button>Send</button>
  </form>
  <ul id="messages"></ul>
  <script>
    let ws = new WebSocket("ws://localhost:8000/ws");
    ws.onmessage = function (event) {
      let messages = document.getElementById("messages");
      let message = document.createElement("li");
      let content = document.createTextNode(event.data);
      message.appendChild(content);
      messages.appendChild(message);
    };
    function sendMessage(event) {
      let input = document.getElementById("messageText");
      ws.send(input.value);
      input.value = "";
      event.preventDefault();
    }
    function sendJSON(event) {
      console.log(event)
      event.preventDefault();
      fetch("http://localhost:8000/upload", {
        method: "POST",
        headers: {
          Accept: "application/json, text/plain, */*",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
        .then((res) => res.json())
        .then((res) => console.log(res));
    }
    
    
    let textarea = document.querySelector("form textarea").value
    let button = document.querySelector("form button")

    button.addEventListener("click", sendJSON(event))
  </script>
</html>

"""

@app.post("/upload", status_code=202)
async def get_body(request: Request):
    return await request.json()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send_text(data)

@app.get("/")
async def main() -> Any:
    return HTMLResponse(html)
