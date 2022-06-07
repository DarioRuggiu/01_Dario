from fastapi import FastAPI
from routers_primo_livello import codice_stazione

app = FastAPI()

app.include_router(codice_stazione.router)

@app.get("/")
def root():
  return "Benvenuti nel server ARPA Sardegna!"



@app.post("/")
def root():
  x=50
  return x



