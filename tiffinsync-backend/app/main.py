from fastapi import FastAPI
from .database import Base, engine
from .routers import auth, meals, providers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Create tables automatically
Base.metadata.create_all(bind=engine)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(meals.router)
app.include_router(providers.router)

@app.get("/")
def root():
    return {"message": "TiffinSync API running!"}

