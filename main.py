from fastapi import FastAPI


app = FastAPI()

app.include_router(pioggia.router)
app.include_router(temperatura.router)
app.include_router(umidita.router)



@app.get("/{tipo}/{iniziofine}")
async def root(tipo:str,iniziofine:str):
    if tipo=="PR":
        tipo_stringa="PRECP_MIN"
    else:
        tipo_stringa="TEMP_30MIN"
    
    return {"tipo_dato": tipo_stringa}

