from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .config import settings
from .database import init_db
from .routes import posts_router, tags_router

from os import path, mkdir

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    docs_url='/api/docs',
    redoc_url='/api/redoc'
)

# CORS для Vue
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not path.exists(settings.static_dir):
    mkdir(settings.static_dir)

app.mount('/static', StaticFiles(directory=settings.static_dir), name='static')

# Routes
app.include_router(posts_router)
app.include_router(tags_router)

@app.on_event('startup')
def on_startup():
    init_db()

@app.get('/')
def root():
    return {
        'message': 'Welcome my PET project',
        'docs': 'api/docs'
    }

@app.get('/health')
def health_check():
    return {'status': 'OK'}