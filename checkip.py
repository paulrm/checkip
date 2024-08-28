from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()

# Middleware to simulate rate limiting
RATE_LIMIT_SECONDS = 10
last_request_time = {}

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()

        # Check if rate limit should be bypassed
        if request.headers.get("X-Test-Bypass-Rate-Limit") == "true":
            return await call_next(request)

        # Check rate limiting
        if client_ip in last_request_time:
            elapsed_time = current_time - last_request_time[client_ip]
            if elapsed_time < RATE_LIMIT_SECONDS:
                return JSONResponse({"detail": "Rate limit exceeded"}, status_code=429)
        
        last_request_time[client_ip] = current_time
        response = await call_next(request)
        return response

app.add_middleware(RateLimitMiddleware)

@app.get("/")
async def get_ip(request: Request):
    return {"ip": request.client.host}
