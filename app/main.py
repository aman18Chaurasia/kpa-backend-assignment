from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import bogie, wheel

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(bogie.router, prefix="/api/forms", tags=["Bogie"])
app.include_router(wheel.router, prefix="/api/forms/wheel", tags=["Wheel"])

@app.get("/")
def root():
    return {"message": "KPA backend API running"}
