import os
from fastapi import FastAPI, Depends, Header, HTTPException
from .db import engine, SessionLocal
from .models import Base  
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
from .deps import get_store, Store
from .schemas import TodoIn, TodoOut
from .seed import seed_if_empty
from dotenv import load_dotenv

load_dotenv(os.getenv("ENV_FILE", None))

app = FastAPI(title=os.getenv("APP_NAME", "tp05-api"))

origins = os.getenv("CORS_ORIGINS", "").split(",") if os.getenv("CORS_ORIGINS") else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# Seed opcional en el primer arranque
if settings.SEED_ON_START.lower() == "true":
    with SessionLocal() as db:
        seed_if_empty(db)

@app.post("/admin/seed")
def run_seed(x_seed_token: str = Header(default="")):
    if not settings.SEED_TOKEN or x_seed_token != settings.SEED_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    with SessionLocal() as db:
        result = seed_if_empty(db)
    return {"ok": True, "env": settings.ENV, **result}

@app.get("/")
def root():
    return {"status": "ok", "message": "tp05-api running"}

@app.get("/readyz")
def readyz(store: Store = Depends(get_store)):
    return store.health()

@app.get("/healthz")
def healthz(store: Store = Depends(get_store)):
    return store.health()

@app.get("/api/todos", response_model=list[TodoOut])
def list_todos(store: Store = Depends(get_store)):
    return store.list()

@app.post("/api/todos", response_model=TodoOut, status_code=201)
def create_todo(payload: TodoIn, store: Store = Depends(get_store)):
    todo = store.add(title=payload.title, description=payload.description)
    return todo

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("API_PORT", 8080)))
