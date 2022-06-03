from fastapi import FastAPI
import webbrowser


app = FastAPI()


@app.get("/{tipo}/{iniziofine}")
async def root(tipo:str,iniziofine:str):
    if tipo=="PR":
        tipo_stringa="PRECP_MIN"
    else:
        tipo_stringa="TEMP_30MIN"
    
    return {"tipo_dato": tipo_stringa}

