from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn

app = FastAPI()

@app.get("/")
async def get_ip(request: Request):
    client_ip = request.client.host

    # Check if the request is coming from a browser
    user_agent = request.headers.get("User-Agent", "")
    if "curl" in user_agent.lower():
        return PlainTextResponse(client_ip)
    else:
        return JSONResponse({"ip": client_ip})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
