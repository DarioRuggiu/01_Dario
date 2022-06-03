from fastapi import FastAPI
from routers import pioggia,temperatura,umidita

app = FastAPI()

app.include_router(pioggia.router)
app.include_router(temperatura.router)
app.include_router(umidita.router)


@app.get("/")
def root():
  return "Hello world!"



