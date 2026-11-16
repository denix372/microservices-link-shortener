from fastapi import FastAPI, HTTPException
import redis
import hashlib
import os

app = FastAPI()

# connenct to DataBase
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"), 
    port=6379, 
    decode_responses=True
)

@app.post("/shorten")
def shorten_url(url: str):
    # generate a short ID for the first 6 characters for URL hash
    short_id = hashlib.md5(url.encode()).hexdigest()[:6]
    redis_client.set(short_id, url)
    return {"short_url": f"http://localhost/{short_id}"}

@app.get("/{short_id}")
def redirect(short_id: str):
    long_url = redis_client.get(short_id)
    if not long_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"redirect_to": long_url} # in a real up, we should return a RedirectResponse