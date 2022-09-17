import json
from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel
import aiohttp
from sentry_sdk import capture_exception



import sentry_sdk

sentry_sdk.init(
    dsn="https://b3c4e45b0242471587666a6d6a971189@o1400416.ingest.sentry.io/6754593",
    traces_sample_rate=1.0,
)


app = FastAPI()





           
class CommonPostModel(BaseModel):
    body: Any
    headers: Any
    url: Any


class CommonGetModel(BaseModel):
    headers: Any
    url: str




@app.get("/")
async def index():
    return "Server is working!"


@app.get("/sentry-debug")
async def trigger_error():
    try:
        raise Exception("sentry debug error")
    except Exception as e:
        capture_exception(e)
    return {"result": "error", "RESPONSE" : f"sentry error test succesful"}


@app.post("/common_secure_post")
async def post_binder_meter_readings(item: CommonPostModel):
    try:
        url = item.url
        async with aiohttp.ClientSession(headers=item.headers) as session:
            async with session.post(url, data=json.dumps(item.body)) as resp:
                resp = await resp.content.read()

                if resp:
                    return json.loads(resp)
                return resp
    except Exception as e:
        capture_exception(e)
    return {"result": "error", "RESPONSE" : f"Error in FASTAPI, url  : {item.url}"}


@app.post("/common_secure_get")
async def common_secure_get(item: CommonGetModel):
    try:
        url = item.url
        async with aiohttp.ClientSession(headers=item.headers) as session:
            async with session.get(url) as resp:
                resp = await resp.content.read()
                if resp:
                    return json.loads(resp)
                return resp
    except Exception as e:
        capture_exception(e)
    return {"result": "error", "RESPONSE" : f"Error in FASTAPI, url  : {item.url}"}
