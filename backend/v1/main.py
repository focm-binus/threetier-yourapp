from typing import Optional
import logging
logger = logging.getLogger(__name__)

from fastapi import FastAPI, Header
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
)
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


app = FastAPI(
        title="backend",
        description="backend: Documentation",
        version="0.1.0",
        docs_url=None,
        redoc_url=None,
        root_path="/api/v1/backend"
        )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="/app/app/static"), name="static")

@app.on_event("startup")
async def startup_event():
    try:
        import pymongo
        from app.constant import kfc
        from app.constant import shawarma
        myclient = pymongo.MongoClient("mongodb://mongo:27017/")

        mydb = myclient["data"]
        mycol = mydb["card"]

        mylist = [
            { 
            'id':0,
            'image': kfc,
            'tagline': "KFC, who doesn't like it?",
            'title': "KFC",
            'badge': "FAV",
            'like': "1k",
            'view': "10k",
            },
            { 
            'id':1,
            'image': shawarma,
            'tagline': "Shawarma, hmm?",
            'title': "Shawarma",
            'badge': "UH",
            'like': "1",
            'view': "1k",
            },
        ]

        message = mycol.insert_many(mylist)

        logger.info("[INFO] populating during startup successful")

    except Exception as e:
        logger.warning(f"[WARN] populating during startup failed: {str(e)}")

# openapi_url=app.openapi_url,
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/api/v1/backend/openapi.json",
        title=app.title,
        swagger_favicon_url="/static/logo.png",
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url="/api/v1/backend/openapi.json",
        title=app.title + " - ReDoc",
        redoc_favicon_url="/static/logo.png",
    )

@app.get("/", include_in_schema=False)
async def root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>First Service</title>
    </head>
    <body>
        <h1>This could be the landing page for the first servicesss</h1>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/populate")
async def populate():
    try:
        import pymongo
        from app.constant import kfc
        from app.constant import shawarma
        myclient = pymongo.MongoClient("mongodb://mongo:27017/")

        mydb = myclient["data"]
        mycol = mydb["card"]

        mylist = [
            { 
            'id':0,
            'image': kfc,
            'tagline': "KFC, who doesn't like it?",
            'title': "KFC",
            'badge': "FAV",
            'like': "1k",
            'view': "10k",
            },
            { 
            'id':1,
            'image': shawarma,
            'tagline': "Shawarma, hmm?",
            'title': "Shawarma",
            'badge': "UH",
            'like': "1",
            'view': "1k",
            },
        ]

        message = mycol.insert_many(mylist)

        return {'status': 'success', 'ack': message.acknowledged} 
    except Exception as e:
        return {"status":"failed", "message": str(e)}

@app.get("/retrieve")
async def retrieve():
    try:
        import pymongo
        myclient = pymongo.MongoClient("mongodb://mongo:27017/")

        mydb = myclient["data"]
        mycol = mydb["card"]

        data = [x for x in mycol.find({},{'_id':0})]

        return {'status': 'success', 'data': data} 
    except Exception as e:
        return {"status":"failed", "message": str(e)}
