from fastapi import FastAPI
from routers_primo_livello import finestra_temporale
from datetime import datetime

app = FastAPI()

app.include_router(finestra_temporale.router)

@app.get("/")
def root():
  return "Hello world!"







