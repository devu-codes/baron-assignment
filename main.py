from fastapi import FastAPI
from database import init_db
from routes import auth

app = FastAPI()

# Initialize DB
@app.on_event("startup")
def on_startup():
    init_db()

# Register routes
app.include_router(auth.router)
