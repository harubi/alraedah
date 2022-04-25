from json import JSONDecodeError
from fastapi import FastAPI, WebSocket, Request, HTTPException
from fastapi.responses import HTMLResponse
from typing import Literal, Any
from utils import is_cyclic

app = FastAPI()

html: Literal = """
<!DOCTYPE html>
<html>
  <head>
    <title>Alraedah</title>
    <link rel="shortcut icon" type="image/jpg" href="https://elevatus-production.s3.eu-central-1.amazonaws.com/career_portal/2022/02/bd54436b-8125-430b-aca8-28f81ac52ded/original/RNGp4ux1BV26kDeEB6qM5XFeDIxDXpzxSvzQm0CA.png"/>
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
        width: 32rem;
        height: 13rem;
    }
    </style>
  </head>
  <h1>Alraedah</h1>
  <form>
    <label for="textarea">Please enter a JSON object</label>
    <textarea required id="textarea">
{
"list1":[1, 2, 3],
"list2":[0, 2 , 5],
"list3":[3, 0, 1, 2]
}</textarea>
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

    function sendJSON(data) {
      fetch("http://localhost:8000/upload", {
        method: "POST",
        headers: {
          Accept: "application/json, text/plain, */*",
          "Content-Type": "application/json",
        },
        body: data,
      })
        .then((res) => res.json())
        .then((res) => console.log(res));
    }
    
    let button = document.querySelector("form button")

    button.addEventListener("click", (event, textarea) => {
        sendJSON(document.querySelector("form textarea").value);
        event.preventDefault();
    })
  </script>
</html>

"""

@app.post("/upload", status_code=202)
async def get_body(request: Request): 
    try:
        json_body = await request.json()
        return is_cyclic(json_body)
    except JSONDecodeError:
        raise HTTPException(status_code=415, detail="An issue with JSON decoding occured.")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> Any:
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


@app.get("/")
async def main() -> Any:
    return HTMLResponse(html)
